from GeoSpecies_pkg.utils import TrainingData_outdir
import numpy as np
import netCDF4 as nc
import os
from GeoSpecies_pkg.utils import geophysical_biases_data_outdir,geophysical_species_data_outdir

def load_lat_lon_indices(species):
    indir = TrainingData_outdir + '{}/'.format(species)
    lat_index_infile = indir + '{}-lat_index.npy'.format(species)
    lon_index_infile = indir + '{}-lon_index.npy'.format(species)
    lat_index = np.load(lat_index_infile)
    lon_index = np.load(lon_index_infile)
    return lat_index, lon_index


def load_monthly_obs_data(species:str):
    indir = '/my-projects/Projects/PM25_Speices_DL_2023/data/monthly_observation/'
    infile = indir + '{}_monthly_observations.nc'.format(species)
    data = nc.Dataset(infile)
    SPECIES_OBS = data.variables[species][:]
    lat = data.variables["latitude"][:]
    lon = data.variables["longitude"][:]
    return SPECIES_OBS, lat, lon 

def load_geophysical_species_data(species:str):
    infile = geophysical_species_data_outdir + '{}_monthly_geophysical_concentration.nc'.format(species)
    species_monthly_data = nc.Dataset(infile)
    geophysical_species = species_monthly_data.variables[species][:]
    latitudes = species_monthly_data.variables["latitude"][:]
    longitudes = species_monthly_data.variables["longitude"][:]
    return geophysical_species, latitudes, longitudes

def load_geophysical_biases_data(species:str):
    infile = geophysical_biases_data_outdir + '{}_monthly_biases_concentration.nc'.format(species)
    species_monthly_data = nc.Dataset(infile)
    geophysical_species = species_monthly_data.variables[species][:]
    latitudes = species_monthly_data.variables["latitude"][:]
    longitudes = species_monthly_data.variables["longitude"][:]
    return geophysical_species, latitudes, longitudes

def save_geophysical_species_data(geophysical_species:np.array,sitelat:np.array,sitelon:np.array,species:str):
    if not os.path.isdir(geophysical_species_data_outdir):
        os.makedirs(geophysical_species_data_outdir)
    outfile = geophysical_species_data_outdir + '{}_monthly_geophysical_concentration.nc'.format(species)
    species_monthly_data = nc.Dataset(outfile,'w',format='NETCDF4')
    species_monthly_data.TITLE = 'Monthly  co-located geophysical {} over North America'.format(species)
    species_monthly_data.TIMERESOLUTION = 'Monthly'
    species_monthly_data.TIMECOVERAGE = '199801-202112'
    
    sites = species_monthly_data.createDimension('sites',geophysical_species.shape[0])
    dates = species_monthly_data.createDimension('dates',geophysical_species.shape[1])
    lat = species_monthly_data.createDimension("lat",len(sitelat))
    lon = species_monthly_data.createDimension("lon",len(sitelon))
    SPECIES_OBS = species_monthly_data.createVariable(species,'f4',('sites','dates',))
    latitudes = species_monthly_data.createVariable("latitude","f4",("lat",))
    longitudes = species_monthly_data.createVariable("longitude","f4",("lon",))

    latitudes[:] = sitelat
    longitudes[:] = sitelon
    SPECIES_OBS[:] = geophysical_species
    species_monthly_data.close()
    return

    

def save_geophysical_species_biases_data(geophysical_biases:np.array,sitelat:np.array,sitelon:np.array,species:str):
    if not os.path.isdir(geophysical_biases_data_outdir):
        os.makedirs(geophysical_biases_data_outdir)
    outfile = geophysical_biases_data_outdir + '{}_monthly_biases_concentration.nc'.format(species)
    species_monthly_data = nc.Dataset(outfile,'w',format='NETCDF4')
    species_monthly_data.TITLE = 'Monthly  co-located biases {} over North America'.format(species)
    species_monthly_data.TIMERESOLUTION = 'Monthly'
    species_monthly_data.TIMECOVERAGE = '199801-202112'

    sites = species_monthly_data.createDimension('sites',geophysical_biases.shape[0])
    dates = species_monthly_data.createDimension('dates',geophysical_biases.shape[1])
    lat = species_monthly_data.createDimension("lat",len(sitelat))
    lon = species_monthly_data.createDimension("lon",len(sitelon))
    SPECIES_OBS = species_monthly_data.createVariable(species,'f4',('sites','dates',))
    latitudes = species_monthly_data.createVariable("latitude","f4",("lat",))
    longitudes = species_monthly_data.createVariable("longitude","f4",("lon",))

    latitudes[:] = sitelat
    longitudes[:] = sitelon
    SPECIES_OBS[:] = geophysical_biases
    species_monthly_data.close()
    return

