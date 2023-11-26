from GLCNNPM25_pkg.data_func import crop_mapdata
from GLCNNPM25_pkg.iostream import load_GLCNNPM5, load_NA_GeoLatLon, load_cropped_GLCNNPM25,save_cropped_GLCNNPM25
from GLCNNPM25_pkg.utils import padding_GLCNNPM25

def Crop_Save_GLCNNPM25(YEAR, MONTH):
    GeoLAT, GeoLON = load_NA_GeoLatLon()
    for iyear in range(len(YEAR)):
        for imonth in range(len(MONTH)):
            temp_GLCNNPM25 = load_GLCNNPM5(YYYY=YEAR[iyear],MM=MONTH[imonth])
            padded_GLCNNPM25 = padding_GLCNNPM25(init_map=temp_GLCNNPM25)
            cropped_GLCNNPM25 = crop_mapdata(init_map=padded_GLCNNPM25,bottom_lat=GeoLAT[0],top_lat=GeoLAT[-1],left_lon=GeoLON[0],right_lon=GeoLON[-1])
            save_cropped_GLCNNPM25(cropped_Map=cropped_GLCNNPM25,YYYY=YEAR[iyear],MM=MONTH[imonth],Area='NA')
    return

def copy_paste_croppedMapdata(copy_YYYY, paste_YYYY):
    MM = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
    for iyear in range(len(copy_YYYY)):
        for imonth in range(len(MM)):
            temp_cropped_GLCNNPM25 = load_cropped_GLCNNPM25(YYYY=copy_YYYY[iyear],MM=MM[imonth],Area='NA')
            save_cropped_GLCNNPM25(cropped_Map=temp_cropped_GLCNNPM25,YYYY=paste_YYYY[iyear], MM=MM[imonth], Area='NA')
    return
