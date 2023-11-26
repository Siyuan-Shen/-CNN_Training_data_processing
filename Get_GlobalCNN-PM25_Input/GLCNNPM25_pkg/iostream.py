import netCDF4 as nc
import numpy as np
import os
from GLCNNPM25_pkg.utils import GL_CNN_PM25_indir, cropped_mapdata_outdir, version, special_name,number_of_channel


def load_NA_GeoLatLon():
    indir = '/my-projects/Projects/PM25_Speices_DL_2023/data/input_variables_map/'
    lat_infile = indir + 'tSATLAT_NA.npy'
    lon_infile = indir + 'tSATLON_NA.npy'
    NA_GeoLAT = np.load(lat_infile)
    NA_GeoLON = np.load(lon_infile)
    return NA_GeoLAT, NA_GeoLON


def load_GLCNNPM5(YYYY,MM):
    indir = GL_CNN_PM25_indir + '{}/{}/'.format(version,YYYY)
    infile = indir + 'CNNMLBiasPM25_MonthlyPM25_{}Channel{}_{}{}.nc'.format(number_of_channel,special_name,YYYY,MM)
    mapdata = nc.Dataset(infile)
    CNN_PM25 = np.array(mapdata.variables['PM25'][:])
    return CNN_PM25

def load_cropped_GLCNNPM25(YYYY,MM,Area):
    indir = cropped_mapdata_outdir + '{}/{}/'.format(version,YYYY)
    infile = indir + 'GL-prediction-cnn-PM25_{}Channel{}_{}{}_{}.npy'.format(number_of_channel,special_name
                                                                              ,YYYY,MM,Area)
    cropped_Map = np.load(infile)

    return cropped_Map


def save_cropped_GLCNNPM25(cropped_Map,YYYY,MM,Area):
    outdir = cropped_mapdata_outdir + '{}/{}/'.format(version,YYYY)
    if not os.path.isdir(outdir):
        os.makedirs(outdir)
    outfile = outdir + 'GL-prediction-cnn-PM25_{}Channel{}_{}{}_{}.npy'.format(number_of_channel,special_name
                                                                              ,YYYY,MM,Area)
    print(outfile)
    np.save(outfile, cropped_Map)
    return