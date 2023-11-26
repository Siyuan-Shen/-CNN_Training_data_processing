import numpy as np
import netCDF4 as nc
import os
from LandCover_pkg.utils import *


def load_Coarse_LatLon():
    indir = LandCover_outdir
    lat_infile = indir + 'LandCover_lat.npy'
    lon_infile = indir + 'LandCover_lon.npy'
    Coarse_lat = np.load(lat_infile)
    Coarse_lon = np.load(lon_infile)
    return Coarse_lat, Coarse_lon

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

def load_LandCover_init_mapdata(YYYY):
    indir = LandCover_init_indir
    infile = indir + 'MCD12C1.A{}001.061.hdf'.format(YYYY)
    data = nc.Dataset(infile)
    return data

def load_LandCover_mapdata(nametag,YEAR,Area):
    indir = LandCover_outdir + '{}/'.format(nametag) 
    infile = indir + '{}-MCD12C1_LandCover_001x001_{}_{}{}.npy'.format(nametag,Area,YEAR)
    mapdata = np.load(infile)
    return mapdata

def load_LandCover_interpolate_indices(indir):
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

def save_LandCover_interpolate_indices(outdir,lat_nearest_array,lat_ceil_array,lat_floor_array,lon_nearest_array,lon_ceil_array,lon_floor_array,dx,dy):
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

def save_LandCover_mapdata(mapdata,nametag,YEAR,Area):
    outdir = LandCover_outdir + '{}/'.format(nametag)
    if not os.path.isdir(outdir):
        os.makedirs(outdir)
    outfile = outdir + '{}-MCD12C1_LandCover_001x001_{}_{}.npy'.format(nametag,Area,YEAR)
    print(outfile)
    np.save(outfile,mapdata)
    return
