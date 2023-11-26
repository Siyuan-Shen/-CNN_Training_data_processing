import numpy as np
from Convert_TrainingData_pkg.data_func import get_nearest_point_index,get_CNN_training_site_data
from Convert_TrainingData_pkg.iostream import load_mapdata,load_monthly_obs_LatLon,load_NA_GeoLatLon,load_lat_lon_indices,save_lat_lon_indices,nc_saveTrainingVariables,nc_createDimensions
from Convert_TrainingData_pkg.utils import inputfiles_table,TrainingData_outdir
import os


def get_save_nearest_indices(species):
    GeoLAT, GeoLON = load_NA_GeoLatLon()
    sites_number, sitelat, sitelon = load_monthly_obs_LatLon(species=species)
    lon_index, lat_index = get_nearest_point_index(sitelat=sitelat,sitelon=sitelon,lat_grid=GeoLAT,lon_grid=GeoLON)
    save_lat_lon_indices(species=species,lat_index=lat_index,lon_index=lon_index)
    return

def derive_TrainingDatasets(species, channel_names, width, height, special_name, YEAR):

    #### Set variables and load arrays for running function
    MONTH = ['01','02','03','04','05','06','07','08','09','10','11','12']
    start_YYYYMM = '{}{}'.format(YEAR[0],MONTH[0])
    end_YYYYMM   = '{}{}'.format(YEAR[-1],MONTH[-1])
    sites_number, sitelat, sitelon = load_monthly_obs_LatLon(species=species)
    datenumber = len(YEAR)*12
    total_number = sites_number * datenumber
    lat_index, lon_index  = load_lat_lon_indices(species=species)

    ### Set outfile
    outdir = TrainingData_outdir + '{}/'.format(species)
    if not os.path.isdir(outdir):
        os.mkdir(outdir)
    outfile = outdir + '{}-cnn_TrainingData_{}channels_{}x{}_{}01-{}12{}.nc'.format(species,len(channel_names),width,height,YEAR[0],YEAR[-1],special_name)

    ### Create the nc file and add primary information
    nc_createDimensions(outfile=outfile,species=species,nametags=channel_names,start_YYYYMM=start_YYYYMM,end_YYYYMM=end_YYYYMM,
                        start_YYYY=YEAR[0],end_YYYY=YEAR[-1],sitesnumber=sites_number,
                        datenumber=datenumber,total_number=total_number,width=width,height=height)
    
    
    for itag in range(len(channel_names)):
        temp_trainingdata = np.zeros((total_number,width,height),dtype=np.float64)
        for iyear in range(len(YEAR)):
            for imonth in range(len(MONTH)):
                inputfiles_dic = inputfiles_table(YYYY=YEAR[iyear],MM=MONTH[imonth])
                infile = inputfiles_dic[channel_names[itag]]
                mapdata = load_mapdata(infile=infile)
                temp_trainingdata[sites_number*(iyear*12+imonth):sites_number*(iyear*12+imonth+1),:,:] = get_CNN_training_site_data(initial_array=mapdata,Height=height,Width=width,lat_index=lat_index,lon_index=lon_index,nsite=sites_number)
        nc_saveTrainingVariables(outfile=outfile,training_data_array=temp_trainingdata,nametag=channel_names[itag])
            


    return