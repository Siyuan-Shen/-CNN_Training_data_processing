from Geographical_Variables_pkg.data_func import crop_mapdata, derive_spherical_coordinates
from Geographical_Variables_pkg.iostream import load_elevation_Map,load_NA_GeoLatLon,load_NA_GeoLatLon_Map,save_cropped_elevation_Map, save_spherical_coordinates_Map

def crop_save_elevation_mapdata(bottom_lat,top_lat,left_lon,right_lon,Area):
    init_elevation_Map = load_elevation_Map()
    cropped_mapdata = crop_mapdata(init_map=init_elevation_Map,bottom_lat=bottom_lat,top_lat=top_lat,left_lon=left_lon
                                   ,right_lon=right_lon)
    save_cropped_elevation_Map(cropped_mapdata=cropped_mapdata,Area=Area)
    return

def derive_save_spherical_coordinates():
    NA_GeoLAT_Map, NA_GeoLON_Map = load_NA_GeoLatLon_Map()
    S1, S2, S3 = derive_spherical_coordinates(LAT_MAP=NA_GeoLAT_Map, LON_MAP=NA_GeoLON_Map)
    save_spherical_coordinates_Map(S1=S1,S2=S2,S3=S3)
    return