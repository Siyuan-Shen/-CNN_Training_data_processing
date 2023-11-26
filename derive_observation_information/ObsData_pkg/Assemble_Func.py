import numpy as np
from ObsData_pkg.iostream import import_biweekly_data,save_monthly_obs_data, save_DWA_arrays
from ObsData_pkg.data_func import Get_Coeff_Index_DaysWeightedAverage, Convert_Biweekly2Monthly_Obs,Get_NA_Obs,get_dates

def Monthly_Observation_DeriveAndSave(Aimed_Years):
    
    SPEC, AllMns, NA = import_biweekly_data()
    start_Year, start_Month, start_days, end_Year, end_Month, end_days = get_dates(AllMns=AllMns)
    index_DWA, coeff_DWA = Get_Coeff_Index_DaysWeightedAverage(Aimed_Years=Aimed_Years,start_Year=start_Year,start_Month=start_Month,start_days=start_days,
                                                               end_Year=end_Year,end_Month=end_Month,end_days=end_days)
    save_DWA_arrays(DWA_index=index_DWA,DWA_coeff=coeff_DWA)
    for species in SPEC:
        print(species)
        sitelat,sitelon,biweekly_obs = Get_NA_Obs(data_dict=NA,species=species,SPEC=SPEC)
        monthly_obs = Convert_Biweekly2Monthly_Obs(biweekly_obs=biweekly_obs,Aimed_Years=Aimed_Years,index_DWA=index_DWA,coeff_DWA=coeff_DWA)
        print(monthly_obs.shape)
        save_monthly_obs_data(species=species,monthly_obs=monthly_obs,sitelat=sitelat,sitelon=sitelon)
    return