import numpy as np
import GeoPM_AOD_ETA_input_pkg.iostream as Geo_io
import GeoPM_AOD_ETA_input_pkg.utils as Geo_ut
import os


def get_save_GeoPM_AOD_ETA_InputVariables(YYYY,MM):
    data = Geo_io.load_gPM25_fromAvDonkelaar(YYYY=YYYY,MM=MM)
    SATLAT = data['tSATLAT'][:]
    SATLON = data['tSATLON'][:]
    NA_GeoLAT, NA_GeoLON = Geo_io.load_NA_GeoLatLon()
    GeoPM25 = data['tSATPM25adj'][:,:,3]/10.0
    AOD     = data['tSATAODadj'][:,:,3]/1000.0
    ETA     = GeoPM25/(AOD+0.000001)
    ttETAAODBIAS = data['ttETAAODBIAS'][:]
    ttETACOASTAL = data['ttETACOASTAL'][:]
    ttETAMIXING  = data['ttETAMIXING'][:]
    ttETASGAODBIAS = data['ttETASGAODBIAS'][:]
    ttETASGTOPOBIAS = data['ttETASGTOPOBIAS'][:]

    GeoPM25 = crop_map_data(init_mapdata=GeoPM25,init_lat=SATLAT,init_lon=SATLON,cropped_lat=NA_GeoLAT,cropped_lon=NA_GeoLON)
    AOD     = crop_map_data(init_mapdata=AOD,init_lat=SATLAT,init_lon=SATLON,cropped_lat=NA_GeoLAT,cropped_lon=NA_GeoLON)
    ETA     = crop_map_data(init_mapdata=ETA,init_lat=SATLAT,init_lon=SATLON,cropped_lat=NA_GeoLAT,cropped_lon=NA_GeoLON)
    ttETAAODBIAS     = crop_map_data(init_mapdata=ttETAAODBIAS,init_lat=SATLAT,init_lon=SATLON,cropped_lat=NA_GeoLAT,cropped_lon=NA_GeoLON)
    ttETACOASTAL     = crop_map_data(init_mapdata=ttETACOASTAL,init_lat=SATLAT,init_lon=SATLON,cropped_lat=NA_GeoLAT,cropped_lon=NA_GeoLON)
    ttETAMIXING     = crop_map_data(init_mapdata=ttETAMIXING,init_lat=SATLAT,init_lon=SATLON,cropped_lat=NA_GeoLAT,cropped_lon=NA_GeoLON)
    ttETASGAODBIAS     = crop_map_data(init_mapdata=ttETASGAODBIAS,init_lat=SATLAT,init_lon=SATLON,cropped_lat=NA_GeoLAT,cropped_lon=NA_GeoLON)
    ttETASGTOPOBIAS     = crop_map_data(init_mapdata=ttETASGTOPOBIAS,init_lat=SATLAT,init_lon=SATLON,cropped_lat=NA_GeoLAT,cropped_lon=NA_GeoLON)
    
    Geo_io.save_mapdata(outdir=Geo_ut.GeoPM_AOD_ETA_outdir,mapdata=GeoPM25,tagname='geophysical_PM25',YYYY=YYYY,MM=MM,area='NA')
    Geo_io.save_mapdata(outdir=Geo_ut.GeoPM_AOD_ETA_outdir,mapdata=AOD,tagname='AOD',YYYY=YYYY,MM=MM,area='NA')
    Geo_io.save_mapdata(outdir=Geo_ut.GeoPM_AOD_ETA_outdir,mapdata=ETA,tagname='ETA',YYYY=YYYY,MM=MM,area='NA')
    Geo_io.save_mapdata(outdir=Geo_ut.GeoPM_AOD_ETA_outdir,mapdata=ttETAAODBIAS,tagname='ttETAAODBIAS',YYYY=YYYY,MM=MM,area='NA')
    Geo_io.save_mapdata(outdir=Geo_ut.GeoPM_AOD_ETA_outdir,mapdata=ttETACOASTAL,tagname='ttETACOASTAL',YYYY=YYYY,MM=MM,area='NA')
    Geo_io.save_mapdata(outdir=Geo_ut.GeoPM_AOD_ETA_outdir,mapdata=ttETAMIXING,tagname='ttETAMIXING',YYYY=YYYY,MM=MM,area='NA')
    Geo_io.save_mapdata(outdir=Geo_ut.GeoPM_AOD_ETA_outdir,mapdata=ttETASGAODBIAS,tagname='ttETASGAODBIAS',YYYY=YYYY,MM=MM,area='NA')
    Geo_io.save_mapdata(outdir=Geo_ut.GeoPM_AOD_ETA_outdir,mapdata=ttETASGTOPOBIAS,tagname='ttETASGTOPOBIAS',YYYY=YYYY,MM=MM,area='NA')

    return

def crop_map_data(init_mapdata,init_lat,init_lon,cropped_lat, cropped_lon):
    start_lat_index = np.where(init_lat==cropped_lat[0])[0][0]
    end_lat_index   = np.where(init_lat==cropped_lat[-1])[0][0]
    start_lon_index = np.where(init_lon==cropped_lon[0])[0][0]
    end_lon_index   = np.where(init_lon==cropped_lon[-1])[0][0]
    cropped_mapdata = init_mapdata[start_lat_index:end_lat_index+1,start_lon_index:end_lon_index+1]
    return cropped_mapdata