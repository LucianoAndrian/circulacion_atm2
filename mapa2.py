"""
Ayuda para hacer un mapa con la libreria cartopy en python
Circulacion 2019
Dani B Risaro - Lean B Diaz
"""

#Abrimos librerias necesarias
import numpy as np
from matplotlib import pyplot as plt
import cartopy.feature
from cartopy.mpl.ticker import LongitudeFormatter, LatitudeFormatter
import cartopy.crs as ccrs

#L = [LONMIN, LONMAX, LATMIN, LATMAX]
#cmap = 'rainbow'
#nombre_titulo = 'forzante'
#nombre_archivo = 'forzante_tiempo_50_EB1'

def mapa2(cmin,cmax,ncont,lat,lon,L,VAR,cmap,nombre_titulo,nombre_archivo):
    
    #Pasamos las latitudes/longitudes del dataset a una reticula para graficar
    lons, lats = np.meshgrid(lon, lat)
    
    clevs = np.linspace(cmin, cmax, ncont)
    
    #Creamos figura
    fig=plt.figure(figsize=(3,2),dpi=200)
    
    #Definimos proyección
    ax = plt.axes(projection=ccrs.PlateCarree(central_longitude=250))
    crs_latlon = ccrs.PlateCarree()
    ax.set_extent(L, crs=crs_latlon)
    
    #Graficamos
    im=ax.contourf(lons, lats, VAR, clevs, cmap=plt.get_cmap(cmap), extend='both', transform=crs_latlon)
    ax.contour(lons, lats, VAR, levels = 0, colors = "w", xtend='both', transform=crs_latlon)
    #Agregamos barra de colores
    cb = plt.colorbar(im, fraction=0.052, pad=0.04, shrink=0.8, aspect=8)
    cb.ax.tick_params(labelsize=6)
    #Características del mapa
    ax.add_feature(cartopy.feature.LAND, facecolor='#d9d9d9')
    ax.add_feature(cartopy.feature.COASTLINE)
    ax.add_feature(cartopy.feature.BORDERS, linestyle='-', alpha=.5)
    ax.gridlines(crs=crs_latlon, linewidth=0.3, linestyle='-')
    ax.set_xticks(np.arange(170, 360, 45), crs=crs_latlon)
    ax.set_yticks(np.arange(-90, 10, 30), crs=crs_latlon)
    lon_formatter = LongitudeFormatter(zero_direction_label=True)
    lat_formatter = LatitudeFormatter()
    ax.xaxis.set_major_formatter(lon_formatter)
    ax.yaxis.set_major_formatter(lat_formatter)
    ax.tick_params(labelsize=6)
    #Características del mapa
    
    #Titulo
    plt.title(nombre_titulo, fontsize=6, y=0.98, loc="center")
    
    #Guardar figura
    plt.savefig(nombre_archivo + '.jpg')

