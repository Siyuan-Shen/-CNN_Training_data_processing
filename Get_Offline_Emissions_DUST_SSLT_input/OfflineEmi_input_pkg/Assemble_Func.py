from OfflineEmi_input_pkg.data_func import *
from OfflineEmi_input_pkg.utils import *


def calculate_save_offline_emi_interpolate_indices():
    get_offline_emi_indices()
    return

def interpolate_offline_emi_mapdata(DST_YYYY,SSLT_YYYY, MM, Area):
    Days = [31,28,31,30,31,30,31,31,30,31,30,31]
    DD = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12',
      '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24',
      '25', '26', '27', '28', '29', '30', '31']
    
    GC_LAT, GC_LON = load_Coarse_LatLon(indir=Offline_EMI_outdir)
    GEOLAT, GEOLON = load_NA_GeoLatLon()
    lat_nearest_array,lat_ceil_array,lat_floor_array,lon_nearest_array,lon_ceil_array,lon_floor_array,dx,dy = load_OFFLINE_EMI_interpolate_indices(indir=Offline_EMI_outdir)
    for iyear in range(len(DST_YYYY)):
        for imonth in range(len(MM)):
            print('YEAR: {}, {}'.format(DST_YYYY[iyear],'DST'))
            temp_DST_days_average = np.zeros((len(GC_LAT),len(GC_LON), Days[imonth]),dtype=np.float64)
            for iday in range(Days[imonth]):
                
                temp_DST_days_average[:,:,iday] = load_OFFLINE_DST_EMI_data(indir=DUST_EMI_indir,YEAR=DST_YYYY[iyear],MONTH=MM[imonth],DAY=DD[iday])
            temp_monthly_DST_average = np.mean(temp_DST_days_average, axis = 2)
            interpolate_offline_emi_map(init_monthly_mapdata=temp_monthly_DST_average,GeoLAT=GEOLAT,GeoLON=GEOLON,lat_ceil_array=lat_ceil_array,lat_floor_array=lat_floor_array,lon_ceil_array=lon_ceil_array,lon_floor_array=lon_floor_array,
                                       dx=dx,dy=dy,YEAR=DST_YYYY[iyear],MONTH=MM[imonth],nametag='DST',Area=Area)
    for iyear in range(len(SSLT_YYYY)):
        for imonth in range(len(MM)):
            print('YEAR: {}, {}'.format(SSLT_YYYY[iyear],'SSLT'))
            temp_SSLT_days_average = np.zeros((len(GC_LAT),len(GC_LON), Days[imonth]),dtype=np.float64)
            for iday in range(Days[imonth]):
                temp_SSLT_days_average[:,:,iday] = load_OFFLINE_SSLT_EMI_data(indir=SSLT_EMI_indir,YEAR=SSLT_YYYY[iyear],MONTH=MM[imonth],DAY=DD[iday])
            temp_monthly_SSLT_average = np.mean(temp_SSLT_days_average, axis = 2)
            interpolate_offline_emi_map(init_monthly_mapdata=temp_monthly_SSLT_average,GeoLAT=GEOLAT,GeoLON=GEOLON,lat_ceil_array=lat_ceil_array,lat_floor_array=lat_floor_array,lon_ceil_array=lon_ceil_array,lon_floor_array=lon_floor_array,
                                       dx=dx,dy=dy,YEAR=SSLT_YYYY[iyear],MONTH=MM[imonth],nametag='SSLT',Area=Area)
    return

def copy_paste_emi(copy_YYYY, paste_YYYY):
    MM = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
    for iyear in range(len(copy_YYYY)):
        for imonth in range(len(MM)):
            
            temp_mapdata = load_OFFLINE_EMI_interpolated_mapdata(nametag='DST',YEAR=copy_YYYY[iyear],MONTH=MM[imonth],Area='NA')
            save_OFFLINE_EMI_interpolated_mapdata(mapdata=temp_mapdata,nametag='DST',YEAR=paste_YYYY[iyear],MONTH=MM[imonth],Area='NA')
    return