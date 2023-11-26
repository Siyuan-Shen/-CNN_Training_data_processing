import numpy as np
import netCDF4 as nc
import mat73 as mat
import os
import scipy.io as scio
from OfflineEmi_input_pkg.utils import Offline_EMI_outdir, get_total_dust_emissions, get_total_SSLT_emissions

def load_Coarse_LatLon(indir):
    indir = Offline_EMI_outdir
    lat_infile = indir + 'Offline_Emi_lat.npy'
    lon_infile = indir + 'Offline_Emi_lon.npy'
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



def load_OFFLINE_DST_EMI_data(indir,YEAR,MONTH,DAY):
    infile = indir + '{}/{}/dust_emissions_05.{}{}{}.nc'.format(YEAR,MONTH,YEAR,MONTH,DAY)
    data = nc.Dataset(infile)
    total_emi = get_total_dust_emissions(data=data)
    return total_emi


def load_OFFLINE_SSLT_EMI_data(indir,YEAR,MONTH,DAY):
    infile = indir + '{}/{}/seasalt_05.{}{}{}.nc'.format(YEAR,MONTH,YEAR,MONTH,DAY)
    data = nc.Dataset(infile)
    total_emi = get_total_SSLT_emissions(data=data)
    return total_emi


def load_OFFLINE_EMI_interpolate_indices(indir):
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



def load_OFFLINE_EMI_interpolated_mapdata(nametag,YEAR,MONTH,Area):
    indir = Offline_EMI_outdir + '{}/'.format(YEAR)
    infile = indir + '{}-em-EMI_Total_001x001_{}_{}{}.npy'.format(nametag,Area,YEAR,MONTH)
    mapdata = np.load(infile)
    return mapdata



def save_OFFLINE_Emi_interpolate_indices(outdir,lat_nearest_array,lat_ceil_array,lat_floor_array,lon_nearest_array,lon_ceil_array,lon_floor_array,dx,dy):
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


def save_OFFLINE_EMI_interpolated_mapdata(mapdata,nametag,YEAR,MONTH,Area):
    outdir = Offline_EMI_outdir + '{}/'.format(YEAR)
    if not os.path.isdir(outdir):
        os.mkdir(outdir)
    outfile = outdir + '{}-em-EMI_Total_001x001_{}_{}{}.npy'.format(nametag,Area,YEAR,MONTH)
    print(outfile)
    np.save(outfile,mapdata)
    
    return

