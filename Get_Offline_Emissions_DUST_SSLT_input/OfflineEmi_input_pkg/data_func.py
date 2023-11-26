import numpy as np
import netCDF4 as nc
from OfflineEmi_input_pkg.iostream import *
from OfflineEmi_input_pkg.utils import *
from TrainingData_pkg.interpolation import *




def get_offline_emi_indices():
    fine_Lat, fine_Lon = load_NA_GeoLatLon()
    fine_Lat_map, fine_Lon_map = load_NA_GeoLatLon_Map()
    coarse_Lat, coarse_Lon = load_Coarse_LatLon(indir=Offline_EMI_outdir)
    Coarse_Lat_Delta = coarse_Lat[2]-coarse_Lat[1]
    Coarse_Lon_Delta = coarse_Lon[2]-coarse_Lon[1]
    Coarse_Lat_min = -89.75
    Coarse_Lon_min = coarse_Lon[0]

    lat_floor_array = np.floor((fine_Lat - Coarse_Lat_min)/Coarse_Lat_Delta)
    lat_ceil_array  = np.ceil((fine_Lat - Coarse_Lat_min)/Coarse_Lat_Delta)
    lat_nearest_array = np.round((fine_Lat - Coarse_Lat_min) / Coarse_Lat_Delta)
    lon_floor_array = np.floor((fine_Lon - Coarse_Lon_min)/Coarse_Lon_Delta)
    lon_ceil_array  = np.ceil((fine_Lon - Coarse_Lon_min)/Coarse_Lon_Delta)
    lon_nearest_array = np.round((fine_Lon - Coarse_Lon_min) / Coarse_Lon_Delta)

    lat_floor_array = lat_floor_array.astype(int)
    lat_ceil_array = lat_ceil_array.astype(int)
    lat_nearest_array = lat_nearest_array.astype(int)
    lon_floor_array = lon_floor_array.astype(int)
    lon_ceil_array  = lon_ceil_array.astype(int)
    lon_nearest_array = lon_nearest_array.astype(int)

    dx = np.zeros((len(fine_Lat),len(fine_Lon)),dtype=np.float32)
    dy = np.zeros((len(fine_Lat),len(fine_Lon)),dtype=np.float32)
    for ix in range(len(fine_Lat)):
        print('ix: ',ix)
        dy[ix,:] = fine_Lon_map[ix,:]-coarse_Lon[lon_floor_array]
    for iy in range(len(fine_Lon)):
        print('iy: ',iy)
        dx[:,iy] = fine_Lat_map[:,iy]-coarse_Lat[lat_floor_array]
    save_OFFLINE_Emi_interpolate_indices(outdir=Offline_EMI_outdir,lat_nearest_array=lat_nearest_array,lat_ceil_array=lat_ceil_array,lat_floor_array=lat_floor_array,
                                         lon_nearest_array=lon_nearest_array,lon_ceil_array=lon_ceil_array,lon_floor_array=lon_floor_array,
                                         dx=dx,dy=dy)
    return

def get_Concentration4Interpolation(init_mapdata,lat_ceil_array,lat_floor_array,lon_ceil_array,lon_floor_array,ix):
    Cxfyf = init_mapdata[lat_floor_array[ix],lon_floor_array[:]]
    Cxfyc = init_mapdata[lat_floor_array[ix],lon_ceil_array[:]]
    Cxcyf = init_mapdata[lat_ceil_array[ix],lon_floor_array[:]]
    Cxcyc = init_mapdata[lat_ceil_array[ix],lon_ceil_array[:]]
    return Cxcyc,Cxcyf,Cxfyc,Cxfyf

def interpolate_offline_emi_map(init_monthly_mapdata,GeoLAT,GeoLON,lat_ceil_array,lat_floor_array,lon_ceil_array,lon_floor_array,dx,dy,YEAR,MONTH,nametag,Area):
    interpolated_monthly_data = np.zeros((len(GeoLAT),len(GeoLON)),dtype=np.float64)
    for ix in range(len(GeoLAT)):
        Cxcyc,Cxcyf,Cxfyc,Cxfyf = get_Concentration4Interpolation(init_mapdata=init_monthly_mapdata,lat_ceil_array=lat_ceil_array,lat_floor_array=lat_floor_array,
                                                                      lon_ceil_array=lon_ceil_array,lon_floor_array=lon_floor_array,ix=ix)
        interpolated_monthly_data[ix,:] = Bilinearinterpolate_GC_concentraion(Cxfyf=Cxfyf,Cxfyc=Cxfyc,Cxcyf=Cxcyf,Cxcyc=Cxcyc,delta_x=delta_x,delta_y=delta_y,dx=dx[ix,:],dy=dy[ix,:])
    save_OFFLINE_EMI_interpolated_mapdata(interpolated_monthly_data,nametag,YEAR, MONTH,Area)
    return