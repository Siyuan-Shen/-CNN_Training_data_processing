from CEDSAnthroEmissions_pkg.data_func import *


def calculate_save_anthro_emi_interpolate_indices():
    get_anthro_emi_indices()
    return

def interpolate_anthro_emi_mapdata(YYYY, nametags, Area):
    GC_LAT, GC_LON = load_CEDS_Coarse_LatLon()
    GEOLAT, GEOLON = load_NA_GeoLatLon()
    lat_nearest_array,lat_ceil_array,lat_floor_array,lon_nearest_array,lon_ceil_array,lon_floor_array,dx,dy = load_Anthro_Emi_interpolate_indices(indir=Anthropogenic_Emission_outdir)
    for iyear in range(len(YYYY)):
        for nametag in nametags:
            print('YEAR: {}, {}'.format(YYYY[iyear],nametag))
            interpolate_anthro_emi_map(GeoLAT=GEOLAT,GeoLON=GEOLON,lat_ceil_array=lat_ceil_array,lat_floor_array=lat_floor_array,lon_ceil_array=lon_ceil_array,lon_floor_array=lon_floor_array,
                                       dx=dx,dy=dy,YEAR=YYYY[iyear],nametag=nametag,Area=Area)
    return

def copy_paste_emi(copy_YYYY, paste_YYYY, nametags):
    MM = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
    for iyear in range(len(copy_YYYY)):
        for imonth in range(len(MM)):
            for nametag in nametags:
                temp_mapdata = load_Anthro_Emi_interpolated_mapdata(nametag=nametag,YEAR=copy_YYYY[iyear],MONTH=MM[imonth],Area='NA')
                save_Anthro_Emi_interpolated_mapdata(mapdata=temp_mapdata,nametag=nametag,YEAR=paste_YYYY[iyear],MONTH=MM[imonth],Area='NA')

    return