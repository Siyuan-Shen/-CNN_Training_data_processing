TrainingData_outdir = '/my-projects/Projects/PM25_Speices_DL_2023/data/TraningDatasets/'
geophysical_species_data_outdir = '/my-projects/Projects/PM25_Speices_DL_2023/data/monthly_geophysical/'
geophysical_biases_data_outdir = '/my-projects/Projects/PM25_Speices_DL_2023/data/monthly_biases/'


GeoPM25_AOD_ETA_input_indir         = '/my-projects/Projects/PM25_Speices_DL_2023/data/input_variables_map/GeoPM25_AOD_ETA_input/'
GEOS_Chem_input_indir               = '/my-projects/Projects/PM25_Speices_DL_2023/data/input_variables_map/GEOS-Chem_input/'
Global_CNN_PM25_input_indir         = '/my-projects/Projects/PM25_Speices_DL_2023/data/input_variables_map/GL_CNN_PM25/'


def inputfiles_table(YYYY, MM):
    inputfiles_dic = {
        
        'AOD'                : GeoPM25_AOD_ETA_input_indir + '{}/AOD_001x001_NA_map_{}{}.npy'.format(YYYY,YYYY,MM),
        'ETA'                : GeoPM25_AOD_ETA_input_indir + '{}/ETA_001x001_NA_map_{}{}.npy'.format(YYYY,YYYY,MM),
        'GL_CNN_PM25'        : Global_CNN_PM25_input_indir + '/vManuscript-2023May/{}/GL-prediction-cnn-PM25_28Channel_ResNet1111_SigmoidMSELoss_alpha0d005_beta8d0_gamma3d0_lambda1-0d2_ForceSlopeFalse_{}{}_NA.npy'.format(YYYY,YYYY,MM),
        'GeoPM25'            : GeoPM25_AOD_ETA_input_indir + '{}/geophysical_PM25_001x001_NA_map_{}{}.npy'.format(YYYY,YYYY,MM),
        ##################### [Variables from GEOS-Chem] ###################
        'GC_PM25'            : GEOS_Chem_input_indir + '{}/PM25_001x001_NA_map_{}{}.npy'.format(YYYY,YYYY,MM),
        'GC_NH4'             : GEOS_Chem_input_indir + '{}/NH4_001x001_NA_map_{}{}.npy'.format(YYYY,YYYY,MM),
        'GC_SO4'             : GEOS_Chem_input_indir + '{}/SO4_001x001_NA_map_{}{}.npy'.format(YYYY,YYYY,MM),
        'GC_NO3'             : GEOS_Chem_input_indir + '{}/NIT_001x001_NA_map_{}{}.npy'.format(YYYY,YYYY,MM),
        'GC_SOA'             : GEOS_Chem_input_indir + '{}/SOA_001x001_NA_map_{}{}.npy'.format(YYYY,YYYY,MM),
        'GC_OC'              : GEOS_Chem_input_indir + '{}/OC_001x001_NA_map_{}{}.npy'.format(YYYY,YYYY,MM),
        'GC_OM'              : GEOS_Chem_input_indir + '{}/OM_001x001_NA_map_{}{}.npy'.format(YYYY,YYYY,MM),
        'GC_BC'              : GEOS_Chem_input_indir + '{}/BC_001x001_NA_map_{}{}.npy'.format(YYYY,YYYY,MM),
        'GC_DUST'            : GEOS_Chem_input_indir + '{}/DST_001x001_NA_map_{}{}.npy'.format(YYYY,YYYY,MM),
        'GC_SS'              : GEOS_Chem_input_indir + '{}/SSLT_001x001_NA_map_{}{}.npy'.format(YYYY,YYYY,MM),
         
    }
    return inputfiles_dic