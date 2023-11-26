from GLCNNPM25_pkg.Assemble_Func import Crop_Save_GLCNNPM25, copy_paste_croppedMapdata

if __name__ == '__main__':
    YEAR = [ '2000', '2001', '2002','2003', '2004',
        '2005', '2006', '2007', '2008', '2009', '2010', '2011',
        '2012', '2013', '2014', '2015', '2016', '2017', '2018',
        '2019']
    
    MONTH = ['01','02','03','04','05','06','07','08','09','10','11','12']

    Crop_Save_GLCNNPM25(YEAR=YEAR,MONTH=MONTH)

    Copy_YEAR = ['2000','2000','2019','2019','2019']
    Paste_YEAR = ['1998','1999','2020','2021','2022']

    copy_paste_croppedMapdata(copy_YYYY=Copy_YEAR,paste_YYYY=Paste_YEAR) 