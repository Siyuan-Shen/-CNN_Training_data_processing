from Plot_Func.Assemble_Func import plot_training_input_map

if __name__ == '__main__':
    YEAR = [2005,2010,2015]
    MONTH = ['01','02','03','04','05','06','07','08','09','10','11','12']
    channel_names =  ['EtaAOD_Bias', 'EtaCoastal', 'EtaMixing', 'EtaSGAOD_Bias', 'EtaSGTOPO_Bias', 'AOD', 'ETA', 'GeoPM25',
                     'GL_CNN_PM25',
                     'GC_PM25', 'GC_NH4', 'GC_SO4', 'GC_NIT', 'GC_SOA', 'GC_OC', 'GC_OM', 'GC_BC', 'GC_DST', 'GC_SSLT',
                     'NH3_anthro_emi', 'SO2_anthro_emi', 'NO_anthro_emi', 'N2O_anthro_emi', 'OC_anthro_emi', 'BC_anthro_emi', 'NMVOC_anthro_emi',
                     'DST_offline_emi', 'SSLT_offline_emi',
                     'PBLH', 'PRECTOT', 'RH', 'T2M', 'U10M', 'V10M',
                     'Crop_Nat_Vege_Mos', 'Permanent_Wetlands', 'Croplands', 'Urban_Builtup_Lands',
                     'S1', 'S2', 'S3', 'Lat', 'Lon', 'elevation']
    plot_training_input_map(YEAR=YEAR, MONTH=MONTH, channel_names=channel_names)