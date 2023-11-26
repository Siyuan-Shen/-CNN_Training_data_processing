import numpy as np

def get_CNN_training_site_data(initial_array, Height, Width,lat_index, lon_index,nsite):
    CNN_training = np.zeros((nsite, Height, Width), dtype=np.float64)
    for j in range(nsite):
            CNN_training[j,:,:] = initial_array[int(lat_index[j] - (Height - 1) / 2):int(
                lat_index[j] + (Height + 1) / 2), int(lon_index[j] - (Width - 1) / 2):int(
                lon_index[j] + (Width + 1) / 2)]

    return CNN_training

def get_nearest_point_index(sitelon, sitelat, lon_grid, lat_grid):
    '''
    func: get the index of stations on the grids map
    inputs:
        sitelon, sitelat: stations location, eg:[42.353,110.137] 0th dim:lat 1st dim:lat
        lon_grid: grids longitude
        lat_grid: grids latitude
    return:
        index: [index_lat,index_lon]
    '''
    # step1: get the spatial resolution; Default: the latitude and longitude have the same resolution
    det = 0.01
    # step2:
    lon_min = np.min(lon_grid)
    lat_min = np.min(lat_grid)
    index_lon = np.round((sitelon - lon_min) / det)
    index_lat = np.round((sitelat - lat_min) / det)
    index_lon = index_lon.astype(int)
    index_lat = index_lat.astype(int)
    
    return index_lon,index_lat