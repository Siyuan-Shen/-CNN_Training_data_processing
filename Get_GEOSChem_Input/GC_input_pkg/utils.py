from GC_input_pkg.tracers_func import * 

def Tracers_lookup_table():
    lookup_table = {
        'PM25' : PM25_floor_ceil_concentrations,
        'NIT'  : NIT_floor_ceil_concentraions,
        'SO4'  : SO4_floor_ceil_concentraions,
        'NH4'  : NH4_floor_ceil_concentraions,
        'BC'   : BC_floor_ceil_concentraions,
        'OC'   : OC_floor_ceil_concentraions,
        'OM'   : OM_floor_ceil_concentraions,
        'SOA'  : SOA_floor_ceil_concentraions,
        'DST'  : DST_floor_ceil_concentraions,
        'SSLT' : SSLT_floor_ceil_concentraions
    }
    return lookup_table
GC_interpolate_indices_outdir = '/my-projects/Projects/PM25_Speices_DL_2023/data/input_variables_map/GEOS-Chem_input/'
GC_interpolate_speices_outdir = '/my-projects/Projects/PM25_Speices_DL_2023/data/input_variables_map/GEOS-Chem_input/'
