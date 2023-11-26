import matplotlib.pyplot as plt
import matplotlib.colors as colors
import cartopy.crs as ccrs
import cartopy.feature as cfeat
import numpy as np
from sklearn.metrics import mean_squared_error,r2_score
import math
import os
import seaborn as sns
from ObsData_pkg.iostream import load_monthly_obs_data


def plot_AllSpecies_observations_loc(SPEC:list):

    fig, ax = plt.subplots(figsize=(10, 10), subplot_kw={"projection": ccrs.PlateCarree()})
    ax.set_extent([-130, -60, 25, 50], crs=ccrs.PlateCarree())
    ax.add_feature(cfeat.NaturalEarthFeature('physical', 'ocean', '50m', edgecolor='none', facecolor='white'))
    ax.add_feature(cfeat.NaturalEarthFeature('physical', 'land', '50m', edgecolor='none', facecolor=cfeat.COLORS['land']))
    ax.add_feature(cfeat.BORDERS, linewidth=0.1)
    ax.add_feature(cfeat.LAKES, linewidth = 0.05)
    count = 0
    for species in SPEC:
        if species != 'PM25':
            SPECIES_OBS, lat, lon =  load_monthly_obs_data(species=species)
            color = ['blue','orange','green','red','purple','pink','olive','cyan']
            number = len(lat)
            plt.scatter(lon,lat,s=10,
            linewidths=0.1, marker='o', edgecolors='black',c=color[count],
            alpha=0.3,zorder=2,label='{} - {} sites'.format(species, number))
            count+=1
        else:
            None
    plt.legend(loc='best')
    fig_outfile = '/my-projects/Projects/PM25_Speices_DL_2023/code/Data_Processing/derive_observation_information/figures/AllSpecies_Obs_location.png'
    plt.savefig(fig_outfile,format='png',dpi=1000,transparent=True,bbox_inches='tight')
    plt.close()
    return

def plot_EachSpecies_observations_loc(species:str,color):

    fig, ax = plt.subplots(figsize=(10, 10), subplot_kw={"projection": ccrs.PlateCarree()})
    ax.set_extent([-130, -60, 25, 50], crs=ccrs.PlateCarree())
    ax.add_feature(cfeat.NaturalEarthFeature('physical', 'ocean', '50m', edgecolor='none', facecolor='white'))
    ax.add_feature(cfeat.NaturalEarthFeature('physical', 'land', '50m', edgecolor='none', facecolor=cfeat.COLORS['land']))
    ax.add_feature(cfeat.BORDERS, linewidth=0.1)
    ax.add_feature(cfeat.LAKES, linewidth = 0.05)
    SPECIES_OBS, lat, lon =  load_monthly_obs_data(species=species)
    number = len(lat)
    plt.scatter(lon,lat,s=10,
            linewidths=0.1, marker='o', edgecolors='black',c=color,
            alpha=0.8,zorder=2,label='{} - {} sites'.format(species, number))
    plt.legend(loc='best')
            
    fig_outfile = '/my-projects/Projects/PM25_Speices_DL_2023/code/Data_Processing/derive_observation_information/figures/{}_Obs_location.png'.format(species)
    plt.savefig(fig_outfile,format='png',dpi=1000,transparent=True,bbox_inches='tight')
    plt.close()
    return

