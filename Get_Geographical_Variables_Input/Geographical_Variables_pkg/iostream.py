import numpy as np
import netCDF4 as nc
import os 
from Geographical_Variables_pkg.utils import elevation_indir, elevation_outdir, spherical_coordinates_outdir

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

def load_elevation_Map():
    infile = elevation_indir + 'elevation_0.01.nc4'
    nc_data = nc.Dataset(infile)
    elevation = nc_data.variables['elev'][:]
    return elevation

def save_cropped_elevation_Map(cropped_mapdata,Area):
    outfile = elevation_outdir + 'elevartion_001x001_{}.npy'.format(Area)
    cropped_mapdata = np.array(cropped_mapdata)
    np.save(outfile,cropped_mapdata)
    return

def save_spherical_coordinates_Map(S1,S2,S3):
    if not os.path.isdir(spherical_coordinates_outdir):
        os.makedirs(spherical_coordinates_outdir)
    S1_outfile = spherical_coordinates_outdir + 'Spherical_Coordinates_1.npy'
    S2_outfile = spherical_coordinates_outdir + 'Spherical_Coordinates_2.npy'
    S3_outfile = spherical_coordinates_outdir + 'Spherical_Coordinates_3.npy'
    np.save(S1_outfile, S1)
    np.save(S2_outfile, S2)
    np.save(S3_outfile, S3)

    return
