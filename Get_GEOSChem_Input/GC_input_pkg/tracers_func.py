import numpy as np



def PM25_floor_ceil_concentrations(MERRASPEC,ix,jy,lon_floor_index,lon_ceil_index,lat_floor_index,lat_ceil_index,START_NUMBER_OF_MONTHS,NUMBER_OF_MONTHS):
    PM25_ratio = np.array([1,1,1,
                           1,1,1,1,
                           1,1,
                           1,0,
                           1,1,1,1,0.3,0,0,
                           1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],dtype=np.float64)
    Cxfyf = np.sum(MERRASPEC[lat_floor_index[ix,jy],lon_floor_index[ix,jy],START_NUMBER_OF_MONTHS:NUMBER_OF_MONTHS,:]*PM25_ratio)
    Cxfyc = np.sum(MERRASPEC[lat_floor_index[ix,jy],lon_ceil_index[ix,jy],START_NUMBER_OF_MONTHS:NUMBER_OF_MONTHS,:]*PM25_ratio)
    Cxcyf = np.sum(MERRASPEC[lat_ceil_index[ix,jy],lon_floor_index[ix,jy],START_NUMBER_OF_MONTHS:NUMBER_OF_MONTHS,:]*PM25_ratio)
    Cxcyc = np.sum(MERRASPEC[lat_ceil_index[ix,jy],lon_ceil_index[ix,jy],START_NUMBER_OF_MONTHS:NUMBER_OF_MONTHS,:]*PM25_ratio)   
    return Cxfyf,Cxfyc,Cxcyf,Cxcyc

def SO4_floor_ceil_concentraions(MERRASPEC,ix,jy,lon_floor_index,lon_ceil_index,lat_floor_index,lat_ceil_index,START_NUMBER_OF_MONTHS,NUMBER_OF_MONTHS):
    Cxfyf = MERRASPEC[lat_floor_index[ix,jy],lon_floor_index[ix,jy],START_NUMBER_OF_MONTHS:NUMBER_OF_MONTHS,0]
    Cxfyc = MERRASPEC[lat_floor_index[ix,jy],lon_ceil_index[ix,jy],START_NUMBER_OF_MONTHS:NUMBER_OF_MONTHS,0]
    Cxcyf = MERRASPEC[lat_ceil_index[ix,jy],lon_floor_index[ix,jy],START_NUMBER_OF_MONTHS:NUMBER_OF_MONTHS,0]
    Cxcyc = MERRASPEC[lat_ceil_index[ix,jy],lon_ceil_index[ix,jy],START_NUMBER_OF_MONTHS:NUMBER_OF_MONTHS,0]
    return Cxfyf,Cxfyc,Cxcyf,Cxcyc

def NIT_floor_ceil_concentraions(MERRASPEC,ix,jy,lon_floor_index,lon_ceil_index,lat_floor_index,lat_ceil_index,START_NUMBER_OF_MONTHS,NUMBER_OF_MONTHS):
    Cxfyf = MERRASPEC[lat_floor_index[ix,jy],lon_floor_index[ix,jy],START_NUMBER_OF_MONTHS:NUMBER_OF_MONTHS,2]
    Cxfyc = MERRASPEC[lat_floor_index[ix,jy],lon_ceil_index[ix,jy],START_NUMBER_OF_MONTHS:NUMBER_OF_MONTHS,2]
    Cxcyf = MERRASPEC[lat_ceil_index[ix,jy],lon_floor_index[ix,jy],START_NUMBER_OF_MONTHS:NUMBER_OF_MONTHS,2]
    Cxcyc = MERRASPEC[lat_ceil_index[ix,jy],lon_ceil_index[ix,jy],START_NUMBER_OF_MONTHS:NUMBER_OF_MONTHS,2]
    return Cxfyf,Cxfyc,Cxcyf,Cxcyc


def NH4_floor_ceil_concentraions(MERRASPEC,ix,jy,lon_floor_index,lon_ceil_index,lat_floor_index,lat_ceil_index,START_NUMBER_OF_MONTHS,NUMBER_OF_MONTHS):
    Cxfyf = MERRASPEC[lat_floor_index[ix,jy],lon_floor_index[ix,jy],START_NUMBER_OF_MONTHS:NUMBER_OF_MONTHS,1]
    Cxfyc = MERRASPEC[lat_floor_index[ix,jy],lon_ceil_index[ix,jy],START_NUMBER_OF_MONTHS:NUMBER_OF_MONTHS,1]
    Cxcyf = MERRASPEC[lat_ceil_index[ix,jy],lon_floor_index[ix,jy],START_NUMBER_OF_MONTHS:NUMBER_OF_MONTHS,1]
    Cxcyc = MERRASPEC[lat_ceil_index[ix,jy],lon_ceil_index[ix,jy],START_NUMBER_OF_MONTHS:NUMBER_OF_MONTHS,1]
    return Cxfyf,Cxfyc,Cxcyf,Cxcyc

def OC_floor_ceil_concentraions(MERRASPEC,ix,jy,lon_floor_index,lon_ceil_index,lat_floor_index,lat_ceil_index,START_NUMBER_OF_MONTHS,NUMBER_OF_MONTHS):
    Cxfyf = np.sum(MERRASPEC[lat_floor_index[ix,jy],lon_floor_index[ix,jy],START_NUMBER_OF_MONTHS:NUMBER_OF_MONTHS,3:5],axis=1)*2.1 + np.sum(MERRASPEC[lat_floor_index[ix,jy],lon_floor_index[ix,jy],START_NUMBER_OF_MONTHS:NUMBER_OF_MONTHS,5:7],axis=1)*1.4
    Cxfyc = np.sum(MERRASPEC[lat_floor_index[ix,jy],lon_ceil_index[ix,jy],START_NUMBER_OF_MONTHS:NUMBER_OF_MONTHS,3:5],axis=1)*2.1 + np.sum(MERRASPEC[lat_floor_index[ix,jy],lon_ceil_index[ix,jy],START_NUMBER_OF_MONTHS:NUMBER_OF_MONTHS,5:7],axis=1)*1.4
    Cxcyf = np.sum(MERRASPEC[lat_ceil_index[ix,jy],lon_floor_index[ix,jy],START_NUMBER_OF_MONTHS:NUMBER_OF_MONTHS,3:5],axis=1)*2.1 + np.sum(MERRASPEC[lat_ceil_index[ix,jy],lon_floor_index[ix,jy],START_NUMBER_OF_MONTHS:NUMBER_OF_MONTHS,5:7],axis=1)*1.4
    Cxcyc = np.sum(MERRASPEC[lat_ceil_index[ix,jy],lon_ceil_index[ix,jy],START_NUMBER_OF_MONTHS:NUMBER_OF_MONTHS,3:5],axis=1)*2.1  + np.sum(MERRASPEC[lat_ceil_index[ix,jy],lon_ceil_index[ix,jy],START_NUMBER_OF_MONTHS:NUMBER_OF_MONTHS,5:7],axis=1)*1.4
    return Cxfyf,Cxfyc,Cxcyf,Cxcyc

def BC_floor_ceil_concentraions(MERRASPEC,ix,jy,lon_floor_index,lon_ceil_index,lat_floor_index,lat_ceil_index,START_NUMBER_OF_MONTHS,NUMBER_OF_MONTHS):
    Cxfyf = np.sum(MERRASPEC[lat_floor_index[ix,jy],lon_floor_index[ix,jy],START_NUMBER_OF_MONTHS:NUMBER_OF_MONTHS,7:9],axis=1)
    Cxfyc = np.sum(MERRASPEC[lat_floor_index[ix,jy],lon_ceil_index[ix,jy],START_NUMBER_OF_MONTHS:NUMBER_OF_MONTHS,7:9],axis=1)
    Cxcyf = np.sum(MERRASPEC[lat_ceil_index[ix,jy],lon_floor_index[ix,jy],START_NUMBER_OF_MONTHS:NUMBER_OF_MONTHS,7:9],axis=1)
    Cxcyc = np.sum(MERRASPEC[lat_ceil_index[ix,jy],lon_ceil_index[ix,jy],START_NUMBER_OF_MONTHS:NUMBER_OF_MONTHS,7:9],axis=1)
    return Cxfyf,Cxfyc,Cxcyf,Cxcyc

def SOA_floor_ceil_concentraions(MERRASPEC,ix,jy,lon_floor_index,lon_ceil_index,lat_floor_index,lat_ceil_index,START_NUMBER_OF_MONTHS,NUMBER_OF_MONTHS):
    Cxfyf = np.sum(MERRASPEC[lat_floor_index[ix,jy],lon_floor_index[ix,jy],START_NUMBER_OF_MONTHS:NUMBER_OF_MONTHS,18:34],axis=1)
    Cxfyc = np.sum(MERRASPEC[lat_floor_index[ix,jy],lon_ceil_index[ix,jy],START_NUMBER_OF_MONTHS:NUMBER_OF_MONTHS,18:34],axis=1)
    Cxcyf = np.sum(MERRASPEC[lat_ceil_index[ix,jy],lon_floor_index[ix,jy],START_NUMBER_OF_MONTHS:NUMBER_OF_MONTHS,18:34],axis=1)
    Cxcyc = np.sum(MERRASPEC[lat_ceil_index[ix,jy],lon_ceil_index[ix,jy],START_NUMBER_OF_MONTHS:NUMBER_OF_MONTHS,18:34],axis=1)
    return Cxfyf,Cxfyc,Cxcyf,Cxcyc

def OM_floor_ceil_concentraions(MERRASPEC,ix,jy,lon_floor_index,lon_ceil_index,lat_floor_index,lat_ceil_index,START_NUMBER_OF_MONTHS,NUMBER_OF_MONTHS):
    Cxfyf_OC,Cxfyc_OC,Cxcyf_OC,Cxcyc_OC = OC_floor_ceil_concentraions(MERRASPEC,ix,jy,lon_floor_index,lon_ceil_index,lat_floor_index,lat_ceil_index,START_NUMBER_OF_MONTHS,NUMBER_OF_MONTHS)
    Cxfyf_SOA,Cxfyc_SOA,Cxcyf_SOA,Cxcyc_SOA = SOA_floor_ceil_concentraions(MERRASPEC,ix,jy,lon_floor_index,lon_ceil_index,lat_floor_index,lat_ceil_index,START_NUMBER_OF_MONTHS,NUMBER_OF_MONTHS)
    Cxfyf = Cxfyf_SOA + Cxfyf_OC * 2.1
    Cxfyc = Cxfyc_SOA + Cxfyc_OC * 2.1
    Cxcyf = Cxcyf_SOA + Cxcyf_OC * 2.1
    Cxcyc = Cxcyc_SOA + Cxcyc_OC * 2.1
    return Cxfyf,Cxfyc,Cxcyf,Cxcyc

def DST_floor_ceil_concentraions(MERRASPEC,ix,jy,lon_floor_index,lon_ceil_index,lat_floor_index,lat_ceil_index,START_NUMBER_OF_MONTHS,NUMBER_OF_MONTHS):
    Cxfyf = np.sum(MERRASPEC[lat_floor_index[ix,jy],lon_floor_index[ix,jy],START_NUMBER_OF_MONTHS:NUMBER_OF_MONTHS,11:15],axis=1)+0.3*MERRASPEC[lat_floor_index[ix,jy],lon_floor_index[ix,jy],START_NUMBER_OF_MONTHS:NUMBER_OF_MONTHS,15]
    Cxfyc = np.sum(MERRASPEC[lat_floor_index[ix,jy],lon_ceil_index[ix,jy],START_NUMBER_OF_MONTHS:NUMBER_OF_MONTHS,11:15],axis=1)+0.3*MERRASPEC[lat_floor_index[ix,jy],lon_floor_index[ix,jy],START_NUMBER_OF_MONTHS:NUMBER_OF_MONTHS,15]
    Cxcyf = np.sum(MERRASPEC[lat_ceil_index[ix,jy],lon_floor_index[ix,jy],START_NUMBER_OF_MONTHS:NUMBER_OF_MONTHS,11:15],axis=1)+0.3*MERRASPEC[lat_floor_index[ix,jy],lon_floor_index[ix,jy],START_NUMBER_OF_MONTHS:NUMBER_OF_MONTHS,15]
    Cxcyc = np.sum(MERRASPEC[lat_ceil_index[ix,jy],lon_ceil_index[ix,jy],START_NUMBER_OF_MONTHS:NUMBER_OF_MONTHS,11:15],axis=1)+0.3*MERRASPEC[lat_floor_index[ix,jy],lon_floor_index[ix,jy],START_NUMBER_OF_MONTHS:NUMBER_OF_MONTHS,15]
    return Cxfyf,Cxfyc,Cxcyf,Cxcyc


def SSLT_floor_ceil_concentraions(MERRASPEC,ix,jy,lon_floor_index,lon_ceil_index,lat_floor_index,lat_ceil_index,START_NUMBER_OF_MONTHS,NUMBER_OF_MONTHS):
    Cxfyf = MERRASPEC[lat_floor_index[ix,jy],lon_floor_index[ix,jy],START_NUMBER_OF_MONTHS:NUMBER_OF_MONTHS,9]
    Cxfyc = MERRASPEC[lat_floor_index[ix,jy],lon_ceil_index[ix,jy],START_NUMBER_OF_MONTHS:NUMBER_OF_MONTHS,9]
    Cxcyf = MERRASPEC[lat_ceil_index[ix,jy],lon_floor_index[ix,jy],START_NUMBER_OF_MONTHS:NUMBER_OF_MONTHS,9]
    Cxcyc = MERRASPEC[lat_ceil_index[ix,jy],lon_ceil_index[ix,jy],START_NUMBER_OF_MONTHS:NUMBER_OF_MONTHS,9]
    return Cxfyf,Cxfyc,Cxcyf,Cxcyc






