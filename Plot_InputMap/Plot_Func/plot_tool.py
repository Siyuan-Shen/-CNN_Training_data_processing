from click import style
import matplotlib.pyplot as plt
import matplotlib as mpl
import cartopy as crt
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeat
import xarray as xr
import numpy as np
import numpy.ma as ma
import netCDF4 as nc
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER
import matplotlib.ticker as mticker
import matplotlib.ticker as tick
import matplotlib.colors as colors
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error


def plot_mapinput_figures(PM25_Map:np.array,PM25_LAT:np.array,PM25_LON:np.array,extent:np.array,Channel_name:str,outfile:str):
    PM25_Map[np.where(PM25_Map < 0)] = 0
    ax = plt.axes(projection=ccrs.PlateCarree())
    m1 = (np.mean(PM25_Map)+np.min(PM25_Map))/2.0
    m2 = (np.mean(PM25_Map)+np.max(PM25_Map))/2.0
    extent = [extent[2],extent[3],extent[0],extent[1]]
    print('extent:', extent)
    ax.set_extent(extent,crs=ccrs.PlateCarree())
    ax.add_feature(cfeat.NaturalEarthFeature('physical', 'ocean', '50m', edgecolor='none', facecolor='grey'))
    #ax.add_feature(cfeat.COASTLINE,linewidth = 0.15) 
    ax.add_feature(cfeat.LAKES, linewidth = 0.05)
    ax.add_feature(cfeat.BORDERS, linewidth=0.1)
    pcm = plt.pcolormesh(PM25_LON, PM25_LAT,PM25_Map,transform=ccrs.PlateCarree(),
          cmap = 'rainbow',norm=colors.Normalize(vmin = m1, vmax = m2))
    #ax.add_feature(cfeat.OCEAN) 

    #RMSE = round(np.sqrt(mean_squared_error(sitePM25[area_index, (yyyy[iyear]-1998)*12+mm[imonth]],
    #                                      pre_pm25_site[area_index])),2)
    #R2 = round(linear_regression(sitePM25[area_index, (yyyy[iyear]-1998)*12+mm[imonth]],pre_pm25_site[area_index]),2)    
    #ax.text(extent[2], extent[1]-0.1*abs(extent[1]), '$R^2 = $' + str(R2), style='italic', fontsize=12)
    #ax.text(extent[2], extent[1], '$RMSE = $' + str(RMSE), style='italic', fontsize=12)
    cbar = plt.colorbar(pcm, fraction=0.05, pad=0.05, shrink = 0.5, orientation='horizontal', extend='both')
    cbar.set_label(Channel_name)
    cbar.ax.xaxis.set_major_formatter(tick.FormatStrFormatter('%.2f'))
    gl = ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True, linewidth=0.4, color='k', alpha=0.7, linestyle='--')
    gl.top_labels = False  ##关闭上侧坐标显示
    gl.right_labels = False  ##关闭右侧坐标显示
    gl.xformatter = LONGITUDE_FORMATTER  ##坐标刻度转换为经纬度样式
    gl.yformatter = LATITUDE_FORMATTER
    gl.xlocator = mticker.FixedLocator(np.arange(extent[0], extent[1], 10))
    gl.ylocator = mticker.FixedLocator(np.arange(extent[2], extent[3], 10))
    gl.xlabel_style = {'size': 3.5}
    gl.ylabel_style = {'size': 3.5}
    plt.savefig(outfile, format = 'png', dpi= 2000, transparent = True)
    plt.close()

    return
