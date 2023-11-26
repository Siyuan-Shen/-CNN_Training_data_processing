import numpy as np
import mat73 as mat
import os

def load_gPM25_fromAvDonkelaar(YYYY,MM):
    indir = '/my-projects/from_aaron/gPM25-20230818/'
    infile = indir + 'gPM25-20230818-CombinedMonthlyPM25-{}{}.mat'.format(YYYY,MM)
    data = mat.loadmat(infile)
    return data

def load_NA_GeoLatLon():
    indir = '/my-projects/Projects/PM25_Speices_DL_2023/data/input_variables_map/'
    lat_infile = indir + 'tSATLAT_NA.npy'
    lon_infile = indir + 'tSATLON_NA.npy'
    NA_GeoLAT = np.load(lat_infile)
    NA_GeoLON = np.load(lon_infile)
    return NA_GeoLAT, NA_GeoLON

def save_mapdata(outdir,mapdata,tagname:str,YYYY:str,MM:str,area:str):
    outdir = outdir + YYYY +'/'
    if not os.path.isdir(outdir):
        os.makedirs(outdir)
    outfile = outdir + '{}_001x001_{}_map_{}{}.npy'.format(tagname,area,YYYY,MM)
    np.save(outfile,mapdata)
    return 