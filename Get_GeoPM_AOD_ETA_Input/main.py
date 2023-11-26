from GeoPM_AOD_ETA_input_pkg.data_func import get_save_GeoPM_AOD_ETA_InputVariables

if __name__ == '__main__':
    YEAR = ['1998','1999','2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010',
            '2011','2012','2013','2014','2015','2016','2017','2018','2019','2020','2021','2022']
    MONTH = ['01','02','03','04','05','06','07','08','09','10','11','12']
    for YYYY in YEAR:
        for MM in MONTH:
            print(YYYY,' ',MM)
            get_save_GeoPM_AOD_ETA_InputVariables(YYYY=YYYY,MM=MM)