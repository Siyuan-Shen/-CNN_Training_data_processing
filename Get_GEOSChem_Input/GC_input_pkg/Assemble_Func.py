import GC_input_pkg.iostream as GC_io
import GC_input_pkg.data_func as GC_df
import GC_input_pkg.utils as GC_ut

def calculate_interporlate_indices():
    """This funciton is assembled to derive the indices for bilinear interpolation.
    """
    NA_GeoLAT, NA_GeoLON = GC_io.load_NA_GeoLatLon()
    GC_df.get_GC_interpolate_indices(GEO_LAT=NA_GeoLAT,GEO_LON=NA_GeoLON)
    return 

def derive_interpolated_GC_Map(YEAR,MONTH,START_NUMBER_OF_MONTHS,Tracer):
    lat_nearest_index, lat_ceil_index, lat_floor_index, lon_nearest_index, lon_ceil_index, lon_floor_index = GC_io.load_GC_interpolate_indices(indir=GC_ut.GC_interpolate_indices_outdir)
    NA_GeoLAT, NA_GeoLON = GC_io.load_NA_GeoLatLon()
    GC_df.interpolate_GC_SPEC_regional(GEO_LAT=NA_GeoLAT,GEO_LON=NA_GeoLON,Area='NA',Tracers=Tracer,lat_ceil_index=lat_ceil_index,lat_floor_index=lat_floor_index,lon_ceil_index=lon_ceil_index,
                                       lon_floor_index=lon_floor_index,START_NUMBER_OF_MONTHS=START_NUMBER_OF_MONTHS,YEAR=YEAR,MONTH=MONTH)
    return