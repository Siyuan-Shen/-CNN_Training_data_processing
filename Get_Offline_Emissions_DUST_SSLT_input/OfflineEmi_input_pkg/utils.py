import numpy as np


DUST_EMI_indir = '/ExtData/HEMCO/OFFLINE_DUST/v2021-08/0.5x0.625/'
SSLT_EMI_indir = '/ExtData/HEMCO/OFFLINE_SEASALT/v2019-01/0.5x0.625/'

Offline_EMI_outdir = '/my-projects/Projects/PM25_Speices_DL_2023/data/input_variables_map/Offline_Emissions_input/'

delta_x = 0.1
delta_y = 0.1

def get_total_dust_emissions(data):
    EMIS_DST1 = data.variables['EMIS_DST1'][:]
    EMIS_DST2 = data.variables['EMIS_DST2'][:]
    EMIS_DST1 = np.sum(EMIS_DST1, axis=0)
    EMIS_DST2 = np.sum(EMIS_DST2, axis=0)
    total_emi = EMIS_DST1 + EMIS_DST2
    return total_emi

def get_total_SSLT_emissions(data):
    SALA_TOTAL = data.variables['SALA_TOTAL'][:]
    SALA_TOTAL = np.sum(SALA_TOTAL, axis=0)


    return SALA_TOTAL