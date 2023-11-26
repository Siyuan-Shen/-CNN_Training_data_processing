from Geographical_Variables_pkg.Assemble_Func import crop_save_elevation_mapdata, derive_save_spherical_coordinates

if __name__ == '__main__':
    bottom_lat = 10.005
    top_lat = 69.995
    left_lon = -139.995
    right_lon = -40.005
    #crop_save_elevation_mapdata(bottom_lat=bottom_lat,top_lat=top_lat,left_lon=left_lon,right_lon=right_lon,Area='NA')
    derive_save_spherical_coordinates()
    