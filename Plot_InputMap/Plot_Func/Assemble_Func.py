import numpy as np
from Plot_Func.plot_tool import plot_mapinput_figures
from Plot_Func.iostream import get_figure_outfile, load_NA_GeoLatLon
from Plot_Func.utils import inputfiles_table

def plot_training_input_map(YEAR, MONTH, channel_names):
    NA_GeoLAT, NA_GeoLON = load_NA_GeoLatLon()
    extent = [NA_GeoLAT[0], NA_GeoLAT[-1], NA_GeoLON[0], NA_GeoLON[-1]]
    for iyear in range(len(YEAR)):
        for imonth in range(len(MONTH)):
            infile_table = inputfiles_table(YYYY=YEAR[iyear], MM=MONTH[imonth])
            for channel_name in channel_names:
                print('{} - {}, {}'.format(YEAR[iyear], MONTH[imonth], channel_name))
                temp_map_data = np.load(infile_table[channel_name])
                figure_outfile = get_figure_outfile(YYYY=YEAR[iyear], MM=MONTH[imonth], channel_name=channel_name)
                plot_mapinput_figures(temp_map_data,NA_GeoLAT, NA_GeoLON, extent, channel_name, figure_outfile)
                    
    return