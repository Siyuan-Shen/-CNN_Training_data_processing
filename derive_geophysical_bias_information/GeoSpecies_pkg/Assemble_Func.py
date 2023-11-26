
import numpy as np
from GeoSpecies_pkg.iostream import load_lat_lon_indices,load_monthly_obs_data,save_geophysical_species_biases_data,save_geophysical_species_data, load_geophysical_species_data
from GeoSpecies_pkg.data_func import derive_geophysical_biases, derive_geophysical_species, get_nearSites_pixels
from GeoSpecies_pkg.utils import inputfiles_table

def Monthly_geophysicalSpecies_derive_save(Aimed_Years:list, species:str):

    MONTH = ['01','02','03','04','05','06','07','08','09','10','11','12']
    lat_index, lon_index = load_lat_lon_indices(species=species)
    SPECIES_OBS, lat, lon = load_monthly_obs_data(species=species)

    # initialize geophysical species array
    geophysical_species = np.zeros(SPECIES_OBS.shape,dtype=np.float128)

    for iyear in range(len(Aimed_Years)):
        for imonth in range(len(MONTH)):
            print('YYYY: {}, MM: {}'.format(Aimed_Years[iyear], MONTH[imonth]))
            infiles_table = inputfiles_table(YYYY=Aimed_Years[iyear],MM=MONTH[imonth])
            GeoPM25_Map      = np.load(infiles_table['GeoPM25'])
            GC_SPECIES_MAP   = np.load(infiles_table['GC_{}'.format(species)])
            GC_PM25_MAP      = np.load(infiles_table['GC_PM25'])
            Hybrid_PM25_MAP  = np.load(infiles_table['GL_CNN_PM25'])

            GeoPM25     = get_nearSites_pixels(mapdata=GeoPM25_Map, lat_index=lat_index, lon_index=lon_index)
            GC_SPECIES  = get_nearSites_pixels(mapdata=GC_SPECIES_MAP, lat_index=lat_index, lon_index=lon_index)
            GC_PM25     = get_nearSites_pixels(mapdata=GC_PM25_MAP, lat_index=lat_index, lon_index=lon_index)
            Hybrid_PM25 = get_nearSites_pixels(mapdata=Hybrid_PM25_MAP, lat_index=lat_index, lon_index=lon_index)
            if species == 'PM25':
                geophysical_species[:,iyear*12+imonth] = derive_geophysical_species(GC_SPECEIS=GC_SPECIES, GC_PM25=GC_PM25, HybridPM25=GeoPM25)
            else:
                geophysical_species[:,iyear*12+imonth] = derive_geophysical_species(GC_SPECEIS=GC_SPECIES, GC_PM25=GC_PM25, HybridPM25=Hybrid_PM25)
    save_geophysical_species_data(geophysical_species=geophysical_species, sitelat=lat, sitelon=lon, species=species)

    return

def Monthly_geophysicalBiases_derive_save(species:str):
    SPECIES_OBS, lat, lon = load_monthly_obs_data(species=species)
    geophysical_species, lat, lon = load_geophysical_species_data(species=species)
    # initialize geophysical species array
    geophysical_biases = derive_geophysical_biases(geophysical_species=geophysical_species,observatio_species=SPECIES_OBS)
    save_geophysical_species_biases_data(geophysical_biases=geophysical_biases,sitelat=lat,sitelon=lon,species=species)
    return