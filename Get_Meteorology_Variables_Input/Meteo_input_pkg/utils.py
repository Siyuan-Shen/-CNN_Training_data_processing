

meteorology_indir = '/ExtData/GEOS_0.5x0.625_NA/MERRA2/'
meteorology_mapdata_outdir = '/my-projects/Projects/PM25_Speices_DL_2023/data/input_variables_map/Meteorology_input/'

delta_x = 0.5
delta_y = 0.625


def get_variables_A1_files(A1_file, nametag, lev):
    variable = A1_file.variables[nametag][:]
    return variable

def get_variables_I3_A3cld_A3dyn_A3mstE_A3mstC(file, nametag, lev):
    variable = file.variables[nametag][:,lev,:,:]
    return variable

def File_lookup_table():
    lookup_table = {
        'A1' : get_variables_A1_files,
        'I3'  : get_variables_I3_A3cld_A3dyn_A3mstE_A3mstC,
        'A3cld'  : get_variables_I3_A3cld_A3dyn_A3mstE_A3mstC,
        'A3dyn'  : get_variables_I3_A3cld_A3dyn_A3mstE_A3mstC,
        'A3mstE'   : get_variables_I3_A3cld_A3dyn_A3mstE_A3mstC,
        'A3mstC'   : get_variables_I3_A3cld_A3dyn_A3mstE_A3mstC,
        
    }
    return lookup_table