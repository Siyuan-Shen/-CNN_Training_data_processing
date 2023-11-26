import numpy as np


def derive_geophysical_species(GC_SPECEIS,GC_PM25, HybridPM25):
    geophysical_species = (GC_SPECEIS / (GC_PM25 + 0.01)) * HybridPM25
    return geophysical_species


def derive_geophysical_biases(geophysical_species, observatio_species):
    bias_species = observatio_species - geophysical_species                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
    return bias_species

def get_nearSites_pixels(mapdata:np.array,lat_index:np.array,lon_index:np.array):
    sites_colocated_data = mapdata[lat_index,lon_index] 
    return sites_colocated_data