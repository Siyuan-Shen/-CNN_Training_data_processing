import numpy as np
from GC_input_pkg.iostream import save_GC_interpolate_indices, load_GC_MERRASPEC, save_GC_interpolated_map
from GC_input_pkg.utils import GC_interpolate_indices_outdir,Tracers_lookup_table, GC_interpolate_speices_outdir
from TrainingData_pkg.interpolation import calculate_difference,Bilinearinterpolate_GC_concentraion


def get_GC_interpolate_indices(GEO_LAT,GEO_LON):
    GL_LAT_Delta = 2.0
    GL_LON_Delta = 2.5
    GL_LAT_min    = -90.0
    GL_LAT_max    = 90.0
    GL_LON_min    = -180.0
    GL_LON_max    = 180.0

    AS_LAT_Delta = 0.5
    AS_LON_Delta = 0.625
    AS_LAT_min    = -11.0
    AS_LAT_max    = 55.0
    AS_LON_min    = 60.0
    AS_LON_max    = 150.0

    NA_LAT_Delta = 0.5
    NA_LON_Delta = 0.625
    NA_LAT_min    = 10.0
    NA_LAT_max    = 70.0
    NA_LON_min    = -140.0
    NA_LON_max    = -40.0

    EU_LAT_Delta = 0.5
    EU_LON_Delta = 0.625
    EU_LAT_min    = 30.0
    EU_LAT_max    = 70.0
    EU_LON_min    = -30.0  
    EU_LON_max    = 50.0

    lat_nearest_index = np.zeros((len(GEO_LAT),len(GEO_LON)),dtype=np.int16)
    lat_floor_index   = np.zeros((len(GEO_LAT),len(GEO_LON)),dtype=np.int16)
    lat_ceil_index    = np.zeros((len(GEO_LAT),len(GEO_LON)),dtype=np.int16)
    lon_nearest_index = np.zeros((len(GEO_LAT),len(GEO_LON)),dtype=np.int16)
    lon_floor_index   = np.zeros((len(GEO_LAT),len(GEO_LON)),dtype=np.int16)
    lon_ceil_index    = np.zeros((len(GEO_LAT),len(GEO_LON)),dtype=np.int16)
    for ix in range(len(GEO_LAT)):
            for jy in range(len(GEO_LON)):
                print('GEOLAT: ',GEO_LAT[ix], '   GEOLON: ',GEO_LON[jy])
                if (GEO_LAT[ix] > AS_LAT_min) and (GEO_LAT[ix] < AS_LAT_max) and (GEO_LON[jy] > AS_LON_min) and (
                        GEO_LON[jy] < AS_LON_max):
                    lat_index,lon_index,lat_index_floor,lat_index_ceil,lon_index_floor,lon_index_ceil = get_Interpolate_GC_index(
                    GEO_LAT[ix],GEO_LON[jy], AS = True, NA = False, EU= False)
                elif (GEO_LAT[ix] > NA_LAT_min) and (GEO_LAT[ix] < NA_LAT_max) and (GEO_LON[jy] > NA_LON_min) and (
                        GEO_LON[jy] < NA_LON_max):
                    lat_index,lon_index,lat_index_floor,lat_index_ceil,lon_index_floor,lon_index_ceil = get_Interpolate_GC_index(
                    GEO_LAT[ix],GEO_LON[jy], AS = False, NA = True, EU= False)
                elif (GEO_LAT[ix] > EU_LAT_min) and (GEO_LAT[ix] < EU_LAT_max) and (GEO_LON[jy] > EU_LON_min) and (
                        GEO_LON[jy] < EU_LON_max):
                    lat_index,lon_index,lat_index_floor,lat_index_ceil,lon_index_floor,lon_index_ceil = get_Interpolate_GC_index(
                        GEO_LAT[ix],GEO_LON[jy], AS = False, NA = False, EU= True)
                else:
                    lat_index,lon_index,lat_index_floor,lat_index_ceil,lon_index_floor,lon_index_ceil = get_Interpolate_GC_index(
                    GEO_LAT[ix],GEO_LON[jy], AS = False, NA = False, EU= False)
                    if lon_index == 144 or lon_index == 143:
                        lon_index =143
                        lon_index_ceil = 143
                        lon_index_floor = 142

                    if lat_index == 91 or lat_index == 90:
                        lat_index = 90
                        lat_index_ceil = 90
                        lat_index_floor = 89
                lat_nearest_index[ix,jy] = lat_index
                lat_ceil_index[ix,jy]    = lat_index_ceil
                lat_floor_index[ix,jy]   = lat_index_floor
                lon_nearest_index[ix,jy] = lon_index
                lon_ceil_index[ix,jy]    = lon_index_ceil
                lon_floor_index[ix,jy]   = lon_index_floor    
    save_GC_interpolate_indices(outdir=GC_interpolate_indices_outdir,lat_nearest_index=lat_nearest_index,lat_ceil_index=lat_ceil_index,lat_floor_index=lat_floor_index,
                                lon_nearest_index=lon_nearest_index,lon_ceil_index=lon_ceil_index,lon_floor_index=lon_floor_index)
       
    return

def get_Interpolate_GC_index(GEO_LAT,GEO_LON, AS, NA, EU):

    GL_LAT_Delta = 2.0
    GL_LON_Delta = 2.5
    GL_LAT_min    = -90.0
    GL_LON_min    = -180.0

    AS_LAT_Delta = 0.5
    AS_LON_Delta = 0.625
    AS_LAT_min    = -11.0
    AS_LON_min    = 60.0

    NA_LAT_Delta = 0.5
    NA_LON_Delta = 0.625
    NA_LAT_min    = 10.0
    NA_LON_min    = -140.0

    EU_LAT_Delta = 0.5
    EU_LON_Delta = 0.625
    EU_LAT_min    = 30.0
    EU_LON_min    = -30.0

    if AS:
        lat_index_floor = np.floor((GEO_LAT - AS_LAT_min)/AS_LAT_Delta)
        lat_index_ceil  = np.ceil((GEO_LAT - AS_LAT_min)/AS_LAT_Delta)
        lon_index_floor = np.floor((GEO_LON - AS_LON_min)/AS_LON_Delta)
        lon_index_ceil = np.ceil((GEO_LON - AS_LON_min)/AS_LON_Delta)
        lat_index = np.round((GEO_LAT - AS_LAT_min)/AS_LAT_Delta)
        lon_index = np.round((GEO_LON - AS_LON_min)/AS_LON_Delta)
        lat_index = lat_index.astype(int)
        lon_index = lon_index.astype(int)
        lat_index_floor = lat_index_floor.astype(int)
        lat_index_ceil = lat_index_ceil.astype(int)
        lon_index_floor = lon_index_floor.astype(int)
        lon_index_ceil = lon_index_ceil.astype(int)
    elif NA:
        lat_index_floor = np.floor((GEO_LAT - NA_LAT_min)/NA_LAT_Delta)
        lat_index_ceil  = np.ceil((GEO_LAT - NA_LAT_min)/NA_LAT_Delta)
        lon_index_floor = np.floor((GEO_LON - NA_LON_min)/NA_LON_Delta)
        lon_index_ceil = np.ceil((GEO_LON - NA_LON_min)/NA_LON_Delta)
        lat_index = np.round((GEO_LAT - NA_LAT_min) / NA_LAT_Delta)
        lon_index = np.round((GEO_LON - NA_LON_min) / NA_LON_Delta)
        lat_index = lat_index.astype(int)
        lon_index = lon_index.astype(int)
        lat_index_floor = lat_index_floor.astype(int)
        lat_index_ceil = lat_index_ceil.astype(int)
        lon_index_floor = lon_index_floor.astype(int)
        lon_index_ceil = lon_index_ceil.astype(int)
    elif EU:
        lat_index_floor = np.floor((GEO_LAT - EU_LAT_min)/EU_LAT_Delta)
        lat_index_ceil  = np.ceil((GEO_LAT - EU_LAT_min)/EU_LAT_Delta)
        lon_index_floor = np.floor((GEO_LON - EU_LON_min)/EU_LON_Delta)
        lon_index_ceil = np.ceil((GEO_LON - EU_LON_min)/EU_LON_Delta)
        lat_index = np.round((GEO_LAT - EU_LAT_min) / EU_LAT_Delta)
        lon_index = np.round((GEO_LON - EU_LON_min) / EU_LON_Delta)
        lat_index = lat_index.astype(int)
        lon_index = lon_index.astype(int)
        lat_index_floor = lat_index_floor.astype(int)
        lat_index_ceil = lat_index_ceil.astype(int)
        lon_index_floor = lon_index_floor.astype(int)
        lon_index_ceil = lon_index_ceil.astype(int)
    else:
        lat_index_floor = np.floor((GEO_LAT - GL_LAT_min)/GL_LAT_Delta)
        lat_index_ceil  = np.ceil((GEO_LAT - GL_LAT_min)/GL_LAT_Delta)
        lon_index_floor = np.floor((GEO_LON - GL_LON_min)/GL_LON_Delta)
        lon_index_ceil = np.ceil((GEO_LON - GL_LON_min)/GL_LON_Delta)
        lat_index = np.round((GEO_LAT - GL_LAT_min) / GL_LAT_Delta)
        lon_index = np.round((GEO_LON - GL_LON_min) / GL_LON_Delta)
        lat_index = lat_index.astype(int)
        lon_index = lon_index.astype(int)
        lat_index_floor = lat_index_floor.astype(int)
        lat_index_ceil = lat_index_ceil.astype(int)
        lon_index_floor = lon_index_floor.astype(int)
        lon_index_ceil = lon_index_ceil.astype(int)

    return lat_index,lon_index,lat_index_floor,lat_index_ceil,lon_index_floor,lon_index_ceil

def interpolate_GC_SPEC_gloabl(GEO_LAT, GEO_LON, maptype, Tracers,lat_ceil_index,lat_floor_index,lon_ceil_index,lon_floor_index,START_NUMBER_OF_MONTHS,YEAR,MONTH):
    NUMBER_OF_MONTHS = START_NUMBER_OF_MONTHS + len(YEAR)*len(MONTH)

    GL_MERRASPEC, GLLAT, GLLON = load_GC_MERRASPEC('GL')
    NA_MERRASPEC, NALAT, NALON = load_GC_MERRASPEC('NA')
    EU_MERRASPEC, EULAT, EULON = load_GC_MERRASPEC('EU')
    AS_MERRASPEC, ASLAT, ASLON = load_GC_MERRASPEC('AS')

    AS_delta_x = 0.5
    AS_delta_y = 0.625
    NA_delta_x = 0.5
    NA_delta_y = 0.625
    EU_delta_x = 0.5
    EU_delta_y = 0.625
    GL_delta_x = 2.0
    GL_delta_y = 2.5

    AS_map = np.where(maptype == 0)
    NA_map = np.where(maptype == 1)
    EU_map = np.where(maptype == 2)
    GL_map = np.where(maptype == 3)

    lookup_table = Tracers_lookup_table()
    Tracers_Map = np.zeros((len(GEO_LAT),len(GEO_LON),len(YEAR)*len(MONTH)), dtype=np.float32)
    for ix in range(len(GEO_LAT)):
        for jy in range(len(GEO_LON)):
            print('GEOLAT: ',GEO_LAT[ix], '   GEOLON: ',GEO_LON[jy])
            if maptype[ix,jy] == 0:
                Cxfyf,Cxfyc,Cxcyf,Cxcyc = lookup_table[Tracers](AS_MERRASPEC,ix,jy,lon_floor_index,lon_ceil_index,lat_floor_index,lat_ceil_index,START_NUMBER_OF_MONTHS,NUMBER_OF_MONTHS)
                dx, dy = calculate_difference(GEO_LAT,GEO_LON,ASLAT,ASLON,ix,jy,lat_floor_index,lon_floor_index)
                Tracers_Map[ix,jy,:] = Bilinearinterpolate_GC_concentraion(Cxfyf=Cxfyf,Cxfyc=Cxfyc,Cxcyf=Cxcyf,Cxcyc=Cxcyc,
                delta_x=AS_delta_x,delta_y=AS_delta_y,dx=dx,dy=dy)
            elif maptype[ix,jy] == 1:
                Cxfyf,Cxfyc,Cxcyf,Cxcyc = lookup_table[Tracers](NA_MERRASPEC,ix,jy,lon_floor_index,lon_ceil_index,lat_floor_index,lat_ceil_index,START_NUMBER_OF_MONTHS,NUMBER_OF_MONTHS)
                dx, dy = calculate_difference(GEO_LAT,GEO_LON,NALAT,NALON,ix,jy,lat_floor_index,lon_floor_index)
                Tracers_Map[ix,jy,:] = Bilinearinterpolate_GC_concentraion(Cxfyf=Cxfyf,Cxfyc=Cxfyc,Cxcyf=Cxcyf,Cxcyc=Cxcyc,
                delta_x=NA_delta_x,delta_y=NA_delta_y,dx=dx,dy=dy)
            elif maptype[ix,jy] == 2:
                Cxfyf,Cxfyc,Cxcyf,Cxcyc = lookup_table[Tracers](EU_MERRASPEC,ix,jy,lon_floor_index,lon_ceil_index,lat_floor_index,lat_ceil_index,START_NUMBER_OF_MONTHS,NUMBER_OF_MONTHS)
                dx, dy = calculate_difference(GEO_LAT,GEO_LON,EULAT,EULON,ix,jy,lat_floor_index,lon_floor_index)
                Tracers_Map[ix,jy,:] = Bilinearinterpolate_GC_concentraion(Cxfyf=Cxfyf,Cxfyc=Cxfyc,Cxcyf=Cxcyf,Cxcyc=Cxcyc,
            delta_x=EU_delta_x,delta_y=EU_delta_y,dx=dx,dy=dy)
            else:
                Cxfyf,Cxfyc,Cxcyf,Cxcyc = lookup_table[Tracers](GL_MERRASPEC,ix,jy,lon_floor_index,lon_ceil_index,lat_floor_index,lat_ceil_index,START_NUMBER_OF_MONTHS,NUMBER_OF_MONTHS)
                dx, dy = calculate_difference(GEO_LAT,GEO_LON,GLLAT,GLLON,ix,jy,lat_floor_index,lon_floor_index)
                Tracers_Map[ix,jy,:] = Bilinearinterpolate_GC_concentraion(Cxfyf=Cxfyf,Cxfyc=Cxfyc,Cxcyf=Cxcyf,Cxcyc=Cxcyc,
            delta_x=GL_delta_x,delta_y=GL_delta_y,dx=dx,dy=dy)
    
    for iyear in range(len(YEAR)):
        for imonth in range(len(MONTH)):
            save_GC_interpolated_map(outdir=GC_interpolate_speices_outdir,species=Tracers,YYYY=
                                     YEAR[iyear],MM=MONTH[imonth],Area='GL')
    return



def interpolate_GC_SPEC_regional(GEO_LAT, GEO_LON,Area,Tracers,lat_ceil_index,lat_floor_index,lon_ceil_index,lon_floor_index,START_NUMBER_OF_MONTHS,YEAR,MONTH):
    NUMBER_OF_MONTHS = START_NUMBER_OF_MONTHS + len(YEAR)*len(MONTH)
    MERRASPEC, GCLAT, GCLON = load_GC_MERRASPEC(Area)
    delta_x = GCLAT[2]-GCLAT[1]
    delta_y = GCLON[2]-GCLON[1]
    lookup_table = Tracers_lookup_table()
    Tracers_Map = np.zeros((len(GEO_LAT),len(GEO_LON),len(YEAR)*len(MONTH)), dtype=np.float32)
    for ix in range(len(GEO_LAT)):
        for jy in range(len(GEO_LON)):
            print('GEOLAT: ',GEO_LAT[ix], '   GEOLON: ',GEO_LON[jy])
            Cxfyf,Cxfyc,Cxcyf,Cxcyc = lookup_table[Tracers](MERRASPEC,ix,jy,lon_floor_index,lon_ceil_index,lat_floor_index,lat_ceil_index,START_NUMBER_OF_MONTHS,NUMBER_OF_MONTHS)
            dx, dy = calculate_difference(GEO_LAT,GEO_LON,GCLAT,GCLON,ix,jy,lat_floor_index,lon_floor_index)
            Tracers_Map[ix,jy,:] = Bilinearinterpolate_GC_concentraion(Cxfyf=Cxfyf,Cxfyc=Cxfyc,Cxcyf=Cxcyf,Cxcyc=Cxcyc,
                delta_x=delta_x,delta_y=delta_y,dx=dx,dy=dy)
    for iyear in range(len(YEAR)):
        for imonth in range(len(MONTH)):
            save_GC_interpolated_map(outdir=GC_interpolate_speices_outdir,map_data=Tracers_Map[:,:,iyear*12+imonth],species=Tracers,YYYY=YEAR[iyear],MM=MONTH[imonth],
                                     Area=Area)
    return