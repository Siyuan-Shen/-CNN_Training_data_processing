from Plot_Func.utils import Figures_outdir
import os
import numpy as np

def get_figure_outfile(YYYY:str, MM:str, channel_name:str):
    outdir = Figures_outdir + '{}/{}/'.format(YYYY, MM)
    if not os.path.isdir(outdir):
        os.makedirs(outdir)
    outfile = outdir + '{}_001x001_map.png'.format(channel_name)     
    return outfile

def load_NA_GeoLatLon():
    indir = '/my-projects/Projects/PM25_Speices_DL_2023/data/input_variables_map/'
    lat_infile = indir + 'tSATLAT_NA.npy'
    lon_infile = indir + 'tSATLON_NA.npy'
    NA_GeoLAT = np.load(lat_infile)
    NA_GeoLON = np.load(lon_infile)
    return NA_GeoLAT, NA_GeoLON