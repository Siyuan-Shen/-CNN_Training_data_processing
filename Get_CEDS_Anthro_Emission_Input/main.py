from CEDSAnthroEmissions_pkg.Assemble_Func import *

if __name__ == '__main__':
    YYYY = [ '1998', '1999', '2000', '2001', '2002','2003', '2004',
        '2005', '2006', '2007', '2008', '2009', '2010', '2011',
        '2012', '2013', '2014', '2015', '2016', '2017', '2018',
        '2019', ]
    nametags = ['BC', 'OC', 
                'SO2', 'NO', 'N2O', 'NH3',
                'NMVOC','ALD2','ALK4_butanes','ALK4_hexanes','ALK4_pentanes','BENZ',
                'C2H2','C2H4','C2H6','C3H8','CH2O','CH4','HCOOH']
    #calculate_save_anthro_emi_interpolate_indices()
    interpolate_anthro_emi_mapdata(YYYY=YYYY,nametags=nametags,Area='NA')

    copy_YYYY = ['2019','2019','2019']
    paste_YYYY = ['2020','2021','2022']
    copy_paste_emi(copy_YYYY=copy_YYYY,paste_YYYY=paste_YYYY,nametags=nametags)
