from Convert_TrainingData_pkg.Assemble_Func import get_save_nearest_indices, derive_TrainingDatasets

if __name__ == '__main__':
    SPEC_NAME = ['PM25', 'SO4', 'NH4', 'NO3', 'OM', 'BC', 'DUST', 'SS']
    YEAR = [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 
            2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]
    width = 11
    height = 11
    special_name = ''
    channel_names = ['EtaAOD_Bias', 'EtaCoastal', 'EtaMixing', 'EtaSGAOD_Bias', 'EtaSGTOPO_Bias', 'AOD', 'ETA', 'GeoPM25',
                     'GL_CNN_PM25',
                     'GC_PM25', 'GC_NH4', 'GC_SO4', 'GC_NIT', 'GC_SOA', 'GC_OC', 'GC_OM','GC_BC', 'GC_DST', 'GC_SSLT',
                     'NH3_anthro_emi', 'SO2_anthro_emi', 'NO_anthro_emi', 'N2O_anthro_emi', 'OC_anthro_emi', 'BC_anthro_emi', 'NMVOC_anthro_emi',
                     'DST_offline_emi', 'SSLT_offline_emi',
                     'PBLH', 'PRECTOT', 'RH', 'T2M', 'U10M', 'V10M',
                     'Crop_Nat_Vege_Mos', 'Permanent_Wetlands', 'Croplands', 'Urban_Builtup_Lands',
                     'S1', 'S2', 'S3', 'Lat', 'Lon', 'elevation']
    for species in SPEC_NAME:
        get_save_nearest_indices(species=species)
        derive_TrainingDatasets(species=species,channel_names=channel_names,width=width, height=height, special_name = special_name,YEAR=YEAR)