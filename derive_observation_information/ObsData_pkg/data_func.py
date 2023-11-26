import numpy as np
from .utils import get_Year_Month_Days

def Get_NA_Obs(data_dict:dict,species:str,SPEC:list):
    """This function is used to load the observation data for seleccted species

    Args:
        data_dict (dict): _description_
        species (str): _description_
        SPEC (list): _description_

    Returns:
        _type_: usitelat - lat location; usitelon - lon location; species_obs - observations [number_of_sites, number_of_dates]
    """
    index = SPEC.index(species)
    usitelat = data_dict['usitelat'][index]
    usitelon = data_dict['usitelon'][index]
    species_obs = data_dict['usitePM25'][index]
    return usitelat,usitelon,species_obs

def Convert_Biweekly2Monthly_Obs(biweekly_obs:np.array,Aimed_Years:np.array,index_DWA:np.array,coeff_DWA:np.array):
    """This is function is used to convert biweekly data to monthly average data.

    Args:
        biweekly_obs (np.array): Biweekly observation data
        Aimed_Years (np.array): Aimed Years
        index_DWA (np.array): Index for convert
        coeff_DWA (np.array): Coefficients for convert

    Returns:
        _type_: _description_
    """
    monthly_obs = np.zeros((biweekly_obs.shape[0],len(Aimed_Years)*12), dtype = np.float64)
    for isite in range(biweekly_obs.shape[0]):
        for ibiweek in range(biweekly_obs.shape[1]):
            for i in range(2):
                monthly_obs[isite,index_DWA[ibiweek,i]] += biweekly_obs[isite,ibiweek] * coeff_DWA[ibiweek,i]
    return monthly_obs

def Get_Coeff_Index_DaysWeightedAverage(Aimed_Years, start_Year, start_Month, start_days, end_Year, end_Month, end_days):
    """This function is used to derive the indexes and coefficient for Days-Weighted Average.

    Args:
        Aimed_Years (_type_): list - e.g. [1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021]
        start_Year (_type_): Year for start date
        start_Month (_type_): Month for start date
        start_days (_type_): Days for start date
        end_Year (_type_): Year for end date
        end_Month (_type_): Month for end date
        end_days (_type_): Days for end date

    Returns:
        _type_: Return index and coefficients.
    """
    Total_days = [31,28,31,30,31,30,31,31,30,31,30,31]
    index_DWA = np.zeros((len(start_Year),2),dtype = int) # This is for recording the index (biweekly data |-> monthly data) for days weighted average.
    coeff_DWA = np.zeros((len(start_Year),2),dtype = np.float)  # This is for recording the coefficients (biweekly data |-> monthly data) for days weighted average.

    for i in range(len(start_Year)):
        if start_Month[i] == end_Month[i]:
            index_DWA[i,0] =  int((start_Year[i]-Aimed_Years[0])*12 + (start_Month[i]-1))
            index_DWA[i,1] = 0
            coeff_DWA[i,0] = 14.0/Total_days[int(start_Month[i]-1)]
            coeff_DWA[i,1] = 0 # Only one coefficient is needed in this scenerio.
        else:
            index_DWA[i,0] = int((start_Year[i]-Aimed_Years[0])*12 + (start_Month[i]-1))
            index_DWA[i,1] = int((end_Year[i]-Aimed_Years[0])*12 + (end_Month[i]-1))
            coeff_DWA[i,0] = (Total_days[int(start_Month[i]-1)]-start_days[i]+1)/Total_days[int(start_Month[i]-1)]
            coeff_DWA[i,1] = end_days[i]/Total_days[int(end_Month[i]-1)]

    return index_DWA, coeff_DWA



def get_dates(AllMns:np.array):
    """This function is used to get the MM/DD/YYYY information for each data points and to 
        derive the days-average weighted coefficients in other function.

    Args:
        AllMns (np.array): The array for biweekly data date points
    Returns:
        Return the YYYY, MM, DD for start date and end date for each data point. 
    """
    start_date = AllMns[:,0]
    end_date   = AllMns[:,1]
    start_Year, start_Month, start_days = get_Year_Month_Days(start_date)
    end_Year, end_Month, end_days       = get_Year_Month_Days(end_date)
    return start_Year, start_Month, start_days, end_Year, end_Month, end_days