from LandCover_pkg.Assemble_Func import *
from LandCover_pkg.utils import IGBP_tagnames

if __name__ == '__main__':
    #calculate_save_LandCover_interpolate_indices()
    YYYY = [ '1998', '1999', '2000', '2001', '2002','2003', '2004',
        '2005', '2006', '2007', '2008', '2009', '2010', '2011',
        '2012', '2013', '2014', '2015', '2016', '2017', '2018',
        '2019', '2020', '2021', '2022']
    index = [11, 12, 13, 14]
    nametags = [IGBP_tagnames[i] for i in index]
    interpolate_LandCover_mapdata(YYYY=YYYY,nametags=nametags
                                  ,Area='NA', index=index)