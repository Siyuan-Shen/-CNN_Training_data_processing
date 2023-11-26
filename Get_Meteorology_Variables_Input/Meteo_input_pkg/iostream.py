import netCDF4 as nc
import numpy as np
import os
from Meteo_input_pkg.utils import meteorology_indir, meteorology_mapdata_outdir


def load_meteorology_file(filetag:str,YYYY:str,MM:str,DD:str,Area:str):
    if Area == 'GL':
        infile = meteorology_indir + '{}/{}/MERRA2.{}{}{}.{}.05x0625.nc4'.format(YYYY,MM,YYYY,MM,DD,filetag)
    else:
        infile = meteorology_indir + '{}/{}/MERRA2.{}{}{}.{}.05x0625.{}.nc4'.format(YYYY,MM,YYYY,MM,DD,filetag,Area)
    data = nc.Dataset(infile)
    return data

def load_NA_GC_LatLon():
    indir = meteorology_mapdata_outdir
    GC_LAT_infile = indir + 'GC_LAT.npy'
    GC_LON_infile = indir + 'GC_LON.npy'
    GC_LAT = np.load(GC_LAT_infile)
    GC_LON = np.load(GC_LON_infile)
    GC_LAT = np.squeeze(GC_LAT)
    GC_LON = np.squeeze(GC_LON)
    return GC_LAT, GC_LON

def load_NA_GeoLatLon():
    indir = '/my-projects/Projects/PM25_Speices_DL_2023/data/input_variables_map/'
    lat_infile = indir + 'tSATLAT_NA.npy'
    lon_infile = indir + 'tSATLON_NA.npy'
    NA_GeoLAT = np.load(lat_infile)
    NA_GeoLON = np.load(lon_infile)
    return NA_GeoLAT, NA_GeoLON

def load_NA_GeoLatLon_Map():
    indir = '/my-projects/Projects/PM25_Speices_DL_2023/data/input_variables_map/'
    lat_infile = indir + 'tSATLAT_NA_MAP.npy'
    lon_infile = indir + 'tSATLON_NA_MAP.npy'
    NA_GeoLAT_Map = np.load(lat_infile)
    NA_GeoLON_Map = np.load(lon_infile)
    return NA_GeoLAT_Map, NA_GeoLON_Map

def load_meteo_interpolate_indices(indir):
    lat_nearest_index_file = indir + 'lat_nearest_index.npy'
    lon_nearest_index_file = indir + 'lon_nearest_index.npy'
    lat_floor_index_file   = indir + 'lat_floor_index.npy'
    lon_floor_index_file   = indir + 'lon_floor_index.npy'
    lat_ceil_index_file    = indir + 'lat_ceil_index.npy'
    lon_ceil_index_file    = indir + 'lon_ceil_index.npy'
    dx_file = indir + 'distance_x.npy'
    dy_file = indir + 'distance_y.npy'

    lat_nearest_array = np.load(lat_nearest_index_file)
    lon_nearest_array = np.load(lon_nearest_index_file)
    lat_floor_array   = np.load(lat_floor_index_file)
    lon_floor_array   = np.load(lon_floor_index_file)
    lat_ceil_array    = np.load(lat_ceil_index_file)
    lon_ceil_array    = np.load(lon_ceil_index_file)
    dx = np.load(dx_file)
    dy = np.load(dy_file)
    return lat_nearest_array,lat_ceil_array,lat_floor_array,lon_nearest_array,lon_ceil_array,lon_floor_array,dx,dy


def save_meteo_interpolate_indices(outdir,lat_nearest_array,lat_ceil_array,lat_floor_array,lon_nearest_array,lon_ceil_array,lon_floor_array,dx,dy):
    lat_nearest_index_file = outdir + 'lat_nearest_index.npy'
    lon_nearest_index_file = outdir + 'lon_nearest_index.npy'
    lat_floor_index_file   = outdir + 'lat_floor_index.npy'
    lon_floor_index_file   = outdir + 'lon_floor_index.npy'
    lat_ceil_index_file    = outdir + 'lat_ceil_index.npy'
    lon_ceil_index_file    = outdir + 'lon_ceil_index.npy'
    dx_file = outdir + 'distance_x.npy'
    dy_file = outdir + 'distance_y.npy'

    np.save(lat_nearest_index_file, lat_nearest_array)
    np.save(lon_nearest_index_file, lon_nearest_array)
    np.save(lat_floor_index_file, lat_floor_array)
    np.save(lon_floor_index_file, lon_floor_array)
    np.save(lat_ceil_index_file, lat_ceil_array)
    np.save(lon_ceil_index_file, lon_ceil_array)
    np.save(dx_file,dx)
    np.save(dy_file,dy)
    return


def save_meteo_mapdata(outdir, map_data, tagname, YYYY, MM, Area):
    outdir = outdir + YYYY+'/'
    if not os.path.isdir(outdir):
        os.makedirs(outdir)
    outfile = outdir + '{}_001x001_{}_map_{}{}.npy'.format(tagname,Area,YYYY,MM)
    np.save(outfile,map_data)
    return