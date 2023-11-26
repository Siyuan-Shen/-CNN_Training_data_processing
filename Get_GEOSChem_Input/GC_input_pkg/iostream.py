import scipy.io as scio
import numpy as np
import netCDF4 as nc
import os

def load_GC_MERRASPEC(region:str):
    indir = '/my-projects/from_aaron/PM25_v5/'
    infile = indir + 'MERRASPEC-GCV11.{}-20230829-RH35-199801-202212-wSA.mat'.format(region)
    data = scio.loadmat(infile)
    MERRASPEC = data['MERRASPEC'][:]
    GCLAT = data['GCLAT']
    GCLON = data['GCLON']
    return MERRASPEC, GCLAT, GCLON

def load_NA_GeoLatLon():
    indir = '/my-projects/Projects/PM25_Speices_DL_2023/data/input_variables_map/'
    lat_infile = indir + 'tSATLAT_NA.npy'
    lon_infile = indir + 'tSATLON_NA.npy'
    NA_GeoLAT = np.load(lat_infile)
    NA_GeoLON = np.load(lon_infile)
    return NA_GeoLAT, NA_GeoLON

def load_GC_interpolate_indices(indir):
    lat_nearest_index_infile = indir+'Lat_Nearest_Index.npy'
    lat_floor_index_infile = indir+'Lat_Floor_Index.npy'
    lat_ceil_index_infile = indir+'Lat_Ceil_Index.npy'
    lon_nearest_index_infile = indir+'Lon_Nearest_Index.npy'         
    lon_floor_index_infile = indir+'Lon_Floor_Index.npy'
    lon_ceil_index_infile = indir+'Lon_Ceil_Index.npy'

    lat_nearest_index = np.load(lat_nearest_index_infile)
    lat_ceil_index = np.load(lat_ceil_index_infile)
    lat_floor_index = np.load(lat_floor_index_infile)
    lon_nearest_index = np.load(lon_nearest_index_infile)
    lon_ceil_index = np.load(lon_ceil_index_infile)
    lon_floor_index = np.load(lon_floor_index_infile)
    return lat_nearest_index, lat_ceil_index, lat_floor_index, lon_nearest_index, lon_ceil_index, lon_floor_index

def save_GC_interpolate_indices(outdir, lat_nearest_index,lon_nearest_index,lat_floor_index,lat_ceil_index,lon_floor_index,lon_ceil_index):
    if not os.path.isdir(outdir):
        os.makedirs(outdir)
    lat_nearest_index_outfile = outdir+'Lat_Nearest_Index.npy'
    lat_floor_index_outfile = outdir+'Lat_Floor_Index.npy'
    lat_ceil_index_outfile = outdir+'Lat_Ceil_Index.npy'
    lon_nearest_index_outfile = outdir+'Lon_Nearest_Index.npy'         
    lon_floor_index_outfile = outdir+'Lon_Floor_Index.npy'
    lon_ceil_index_outfile = outdir+'Lon_Ceil_Index.npy'
    np.save(lat_nearest_index_outfile, lat_nearest_index)
    np.save(lat_ceil_index_outfile,lat_ceil_index)
    np.save(lat_floor_index_outfile,lat_floor_index)
    np.save(lon_nearest_index_outfile, lon_nearest_index)
    np.save(lon_ceil_index_outfile,lon_ceil_index)
    np.save(lon_floor_index_outfile,lon_floor_index)           
    return

def save_GC_interpolated_map(outdir, map_data, species, YYYY, MM, Area):
    outdir = outdir + YYYY+'/'
    if not os.path.isdir(outdir):
        os.makedirs(outdir)
    outfile = outdir + '{}_001x001_{}_map_{}{}.npy'.format(species,Area,YYYY,MM)
    np.save(outfile,map_data)
    return