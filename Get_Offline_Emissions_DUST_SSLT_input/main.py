from OfflineEmi_input_pkg.Assemble_Func import *

if __name__ == '__main__':
    #calculate_save_offline_emi_interpolate_indices()
    DST_YYYY = [ '1998', '1999', '2000', '2001', '2002','2003', '2004',
        '2005', '2006', '2007', '2008', '2009', '2010', '2011',
        '2012', '2013', '2014', '2015', '2016', '2017', '2018',
        '2019', '2020', '2021']
    SSLT_YYYY = [ '1998', '1999', '2000', '2001', '2002','2003', '2004',
        '2005', '2006', '2007', '2008', '2009', '2010', '2011',
        '2012', '2013', '2014', '2015', '2016', '2017', '2018',
        '2019', '2020', '2021', '2022']
    MM = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
    #interpolate_offline_emi_mapdata(DST_YYYY=DST_YYYY,SSLT_YYYY=SSLT_YYYY,MM=MM,Area='NA')
    copy_YYYY = ['2019']
    paste_YYYY = ['2022']
    copy_paste_emi(copy_YYYY=copy_YYYY,paste_YYYY=paste_YYYY)