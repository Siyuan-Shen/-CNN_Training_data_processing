import numpy as np

def crop_mapdata(init_map,bottom_lat,top_lat,left_lon,right_lon):
    lat_start_index = int((bottom_lat + 89.995)* 100)
    lon_start_index = int((left_lon + 179.995) * 100)
    lat_end_index = int((top_lat + 89.995) * 100 )
    lon_end_index = int((right_lon + 179.995)*100)
    cropped_mapdata = init_map[lat_start_index:lat_end_index+1,lon_start_index:lon_end_index+1]
    return cropped_mapdata

def derive_spherical_coordinates(LAT_MAP, LON_MAP):
    print('LAT Shape:', LAT_MAP.shape)
    print('LON Shape:', LON_MAP.shape)
    S1 = np.zeros((LAT_MAP.shape[0], LAT_MAP.shape[1]), dtype=np.float64)
    S2 = np.zeros((LAT_MAP.shape[0], LAT_MAP.shape[1]), dtype=np.float64)
    S3 = np.zeros((LAT_MAP.shape[0], LAT_MAP.shape[1]), dtype=np.float64)

    for ix in range(LAT_MAP.shape[0]):
        for iy in range(LON_MAP.shape[1]):
            print(ix, ' ' ,iy)
            S1[ix,iy] = np.cos(2*np.pi*LON_MAP[ix,iy]/360.0) * np.cos(2*np.pi*LAT_MAP[ix,iy]/180.0)
            S2[ix,iy] = np.cos(2*np.pi*LON_MAP[ix,iy]/360.0) * np.sin(2*np.pi*LAT_MAP[ix,iy]/180.0)
            S3[ix,iy] = np.sin(2*np.pi*LON_MAP[ix,iy]/360.0)
    return S1, S2, S3