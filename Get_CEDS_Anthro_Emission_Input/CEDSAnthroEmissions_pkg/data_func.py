import numpy as np
import netCDF4 as nc
from CEDSAnthroEmissions_pkg.iostream import *
from CEDSAnthroEmissions_pkg.utils import *
from TrainingData_pkg.interpolation import *

def get_anthro_emi_indices():
    NA_GeoLAT, NA_GeoLON = load_NA_GeoLatLon()
    NA_GeoLAT_Map, NA_GeoLON_Map = load_NA_GeoLatLon_Map()
    GC_LAT, GC_LON = load_CEDS_Coarse_LatLon()
    lat_nearest_array,lat_ceil_array,lat_floor_array,lon_nearest_array,lon_ceil_array,lon_floor_array,dx,dy = get_BilinearInterpolate_Index(fine_Lat=NA_GeoLAT,fine_Lon=NA_GeoLON,fine_Lat_map=NA_GeoLAT_Map,
                                                                                                                                            fine_Lon_map=NA_GeoLON_Map,coarse_Lat=GC_LAT,coarse_Lon=GC_LON)
    save_Anthro_Emi_interpolate_indices(outdir=Anthropogenic_Emission_outdir,lat_nearest_array=lat_nearest_array,lat_ceil_array=lat_ceil_array,lat_floor_array=lat_floor_array,
                                   lon_nearest_array=lon_nearest_array,lon_ceil_array=lon_ceil_array,lon_floor_array=lon_floor_array,dx=dx,dy=dy)

    return


def get_Concentration4Interpolation(init_mapdata,lat_ceil_array,lat_floor_array,lon_ceil_array,lon_floor_array,ix):
    Cxfyf = init_mapdata[lat_floor_array[ix],lon_floor_array[:]]
    Cxfyc = init_mapdata[lat_floor_array[ix],lon_ceil_array[:]]
    Cxcyf = init_mapdata[lat_ceil_array[ix],lon_floor_array[:]]
    Cxcyc = init_mapdata[lat_ceil_array[ix],lon_ceil_array[:]]
    return Cxcyc,Cxcyf,Cxfyc,Cxfyf




def interpolate_anthro_emi_map(GeoLAT,GeoLON,lat_ceil_array,lat_floor_array,lon_ceil_array,lon_floor_array,dx,dy,YEAR,nametag,Area):
    MM = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
    init_total_emi = load_Anthro_Emi_data(nametag=nametag,YEAR=YEAR)
    for imonth in range(len(MM)):
        interpolated_monthly_data = np.zeros((len(GeoLAT),len(GeoLON)),dtype=np.float128)
        for ix in range(len(GeoLAT)):
            Cxcyc,Cxcyf,Cxfyc,Cxfyf = get_Concentration4Interpolation(init_mapdata=init_total_emi[imonth,:,:],lat_ceil_array=lat_ceil_array,lat_floor_array=lat_floor_array,
                                                                      lon_ceil_array=lon_ceil_array,lon_floor_array=lon_floor_array,ix=ix)
            interpolated_monthly_data[ix,:] = Bilinearinterpolate_GC_concentraion(Cxfyf=Cxfyf,Cxfyc=Cxfyc,Cxcyf=Cxcyf,Cxcyc=Cxcyc,delta_x=delta_x,delta_y=delta_y,dx=dx[ix,:],dy=dy[ix,:])
        save_Anthro_Emi_interpolated_mapdata(interpolated_monthly_data,nametag,YEAR, MM[imonth],Area)
    return
