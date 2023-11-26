import numpy as np

def crop_mapdata(init_map,bottom_lat,top_lat,left_lon,right_lon):
    lat_start_index = int((bottom_lat + 59.995)* 100)
    lon_start_index = int((left_lon + 179.995) * 100)
    lat_end_index = int((top_lat + 59.995) * 100 )
    lon_end_index = int((right_lon + 179.995)*100)
    cropped_mapdata = init_map[lat_start_index:lat_end_index+1,lon_start_index:lon_end_index+1]
    return cropped_mapdata