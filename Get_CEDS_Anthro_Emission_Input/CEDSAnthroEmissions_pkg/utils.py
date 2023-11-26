



CEDS_indir = '/ExtData/HEMCO/CEDS/v2023-04/'

Anthropogenic_Emission_outdir = '/my-projects/Projects/PM25_Speices_DL_2023/data/input_variables_map/Anthropogenic_Emissions_input/'

delta_x = 0.1
delta_y = 0.1

def get_total_emissions(data,nametag):
    agr_sector = data.variables['{}_agr'.format(nametag)][:]
    ene_sector = data.variables['{}_ene'.format(nametag)][:]
    ind_sector = data.variables['{}_ind'.format(nametag)][:]
    tra_sector = data.variables['{}_tra'.format(nametag)][:]
    rco_sector = data.variables['{}_rco'.format(nametag)][:]
    slv_sector = data.variables['{}_slv'.format(nametag)][:]
    wst_sector = data.variables['{}_wst'.format(nametag)][:]
    shp_sector = data.variables['{}_shp'.format(nametag)][:]
    total_emi = agr_sector + ene_sector + ind_sector + tra_sector + rco_sector + slv_sector + wst_sector + shp_sector 
    return total_emi