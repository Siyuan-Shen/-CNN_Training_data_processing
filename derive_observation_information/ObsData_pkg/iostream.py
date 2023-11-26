import numpy as np
import netCDF4 as nc
import mat73 as mat
import os


def import_biweekly_data():
    """_summary_

    Returns:
        
        SPEC - List for Species ['PM25', 'SO4', 'NH4', 'NO3', 'OM', 'BC', 'DUST', 'SS'];
        AllMns - array for data points' date;
        NA - A dictionary for observattions.
    """

    infile = '/my-projects/from_aaron/PM25_v5/CompileSPECGM-NA-20230131-BiWeekly_ALLFILLPM25_NoDuplicates.mat'
    data_dict = mat.loadmat(infile)
    SPEC = data_dict['SPEC'][:]
    AllMns = data_dict['AllMns'][:]
    NA = data_dict['NA']
    return SPEC, AllMns, NA



def save_monthly_obs_data(species:str,monthly_obs:np.array,sitelat:np.array,sitelon:np.array):
    outdir = '/my-projects/Projects/PM25_Speices_DL_2023/data/monthly_observation/'
    if not os.path.isdir(outdir):
        os.makedirs(outdir)
    outfile = outdir + '{}_monthly_observations.nc'.format(species)
    species_monthly_data = nc.Dataset(outfile,'w',format='NETCDF4')
    species_monthly_data.TITLE = 'Monthly {} observations over North America'.format(species)
    species_monthly_data.TIMERESOLUTION = 'Monthly'
    species_monthly_data.TIMECOVERAGE = '199801-202112'

    sites = species_monthly_data.createDimension('sites',monthly_obs.shape[0])
    dates = species_monthly_data.createDimension('dates',monthly_obs.shape[1])
    lat = species_monthly_data.createDimension("lat",len(sitelat))
    lon = species_monthly_data.createDimension("lon",len(sitelon))
    SPECIES_OBS = species_monthly_data.createVariable(species,'f4',('sites','dates',))
    latitudes = species_monthly_data.createVariable("latitude","f4",("lat",))
    longitudes = species_monthly_data.createVariable("longitude","f4",("lon",))

    latitudes[:] = sitelat
    longitudes[:] = sitelon
    SPECIES_OBS[:] = monthly_obs
    return

def load_monthly_obs_data(species:str):
    indir = '/my-projects/Projects/PM25_Speices_DL_2023/data/monthly_observation/'
    infile = indir + '{}_monthly_observations.nc'.format(species)
    data = nc.Dataset(infile)
    SPECIES_OBS = data[species][:]
    lat = data["latitude"][:]
    lon = data["longitude"][:]
    return SPECIES_OBS, lat, lon

def save_DWA_arrays(DWA_index, DWA_coeff):
    outdir = '/my-projects/Projects/PM25_Speices_DL_2023/data/monthly_observation/'
    if not os.path.isdir(outdir):
        os.makedirs(outdir)
    DWA_index_outfile = outdir + 'DWA_index.npy'
    DWA_coeff_outfile = outdir + 'DWA_coeff.npy'
    np.save(DWA_coeff_outfile,DWA_coeff)
    np.save(DWA_index_outfile,DWA_index)
    return

def load_DWA_arrays():
    indir = '/my-projects/Projects/PM25_Speices_DL_2023/data/monthly_observation/'
    DWA_index_infile = indir + 'DWA_index.npy'
    DWA_coeff_infile = indir + 'DWA_coeff.npy'
    DWA_index = np.load(DWA_index_infile)
    DWA_coeff = np.load(DWA_coeff_infile)
    return DWA_index, DWA_coeff

