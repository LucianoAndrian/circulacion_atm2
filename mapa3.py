"""
Figura con dos mapas de dos variables 
"""

#Librerías
import numpy as np
from matplotlib import pyplot as plt
import cartopy.feature
from cartopy.mpl.ticker import LongitudeFormatter, LatitudeFormatter
import cartopy.crs as ccrs

#L = [LONMIN, LONMAX, LATMIN, LATMAX]
#cmap = 'rainbow'
#nombre_titulo = ''
#nombre_archivo = ''

def mapa3(cmin1,cmax1,cmin2,cmax2,ncont,lat,lon,L,VAR1,VAR2,VAR3,cmap,nombre_titulo,nombre_archivo):
    
    #Pasamos las latitudes/longitudes del dataset a una reticula para graficar
    lons, lats = np.meshgrid(lon, lat)
    
    clevs1 = np.linspace(cmin1, cmax1, ncont)
    clevs2 = np.linspace(cmin2, cmax2, ncont)
    
    #Creamos figura
    fig=plt.figure(figsize=(3.8,3),dpi=200)
    
    #Definimos proyección
    ax = plt.axes([0.01,0.55,0.9,0.41],projection=ccrs.PlateCarree(central_longitude=180))
    crs_latlon = ccrs.PlateCarree()
    ax.set_extent(L, crs=crs_latlon)
    
    bx = plt.axes([0.01,0.08,0.9,0.41], projection=ccrs.PlateCarree(central_longitude=180))
    crs_latlon = ccrs.PlateCarree()
    bx.set_extent(L, crs=crs_latlon)
    
    
    #Graficamos
    im1=ax.contourf(lons, lats, VAR1/100000, clevs1, cmap=plt.get_cmap(cmap), extend='both', transform=crs_latlon)
    ax.contour(lons, lats, VAR1/100000, levels = 0, colors = "w", xtend='both', transform=crs_latlon)

  
    im2=bx.contourf(lons, lats, VAR2/100000, clevs2, cmap=plt.get_cmap(cmap), extend='both', transform=crs_latlon)
    bx.contour(lons, lats, VAR2/100000, levels = 0, colors = "w", xtend='both', transform=crs_latlon)

    
    # Defino los ejes donde van a estar las colorbar
    cbaxes1 = fig.add_axes([0.82, 0.55, 0.02, 0.4]) 
    
    cbaxes2 = fig.add_axes([0.82, 0.08, 0.02, 0.4]) 
    
    #Agregamos las barra de colores
    cb1 = plt.colorbar(im1, fraction=0.052, pad=0.04, shrink=0.7, aspect=9,  cax = cbaxes1)
    cb1.ax.tick_params(labelsize=5.8)
    cb1.set_label('$x10^{5}$', labelpad = -22, y=1.08, rotation=0,fontsize=5.8)
    
    cb2 = plt.colorbar(im2, fraction=0.052, pad=0.04, shrink=0.7, aspect=9,  cax = cbaxes2)   #TIENEN QUE ESTAR EN DIF LUGARES
    cb2.ax.tick_params(labelsize=5.8)
    cb2.set_label('$x10^{9}$', labelpad = -30, y=1.08, rotation=0,fontsize=5.8)
    
   
    # agrega las lineas de VAR3. (van despues de las barras de colores, para que tengan color aparte)
    
    anom = ax.contour(lons , lats, VAR3, transform=crs_latlon, linewidths=0.5, colors = "black")
    ax.clabel(anom, inline=1, fontsize = 4)
    
    anom = bx.contour(lons , lats, VAR3, transform=crs_latlon, linewidths=0.5, colors = "black")
    bx.clabel(anom, inline=1, fontsize = 4)
 

    #Características del mapa
    ax.add_feature(cartopy.feature.LAND, facecolor='#d9d9d9')
    ax.add_feature(cartopy.feature.COASTLINE)
    ax.add_feature(cartopy.feature.BORDERS, linestyle='-', alpha=.5)
    ax.gridlines(crs=crs_latlon, linewidth=0.3, linestyle='-')
    #ax.set_xticks(np.arange(-180, 180, 45), crs=crs_latlon)
    ax.set_yticks(np.arange(-90, 90, 30), crs=crs_latlon)
    
    lon_formatter = LongitudeFormatter(zero_direction_label=True)
    lat_formatter = LatitudeFormatter()
    ax.xaxis.set_major_formatter(lon_formatter)
    ax.yaxis.set_major_formatter(lat_formatter)
    ax.tick_params(labelsize=6)
    plt.tight_layout()
    

    
    
    bx.add_feature(cartopy.feature.LAND, facecolor='#d9d9d9')
    bx.add_feature(cartopy.feature.COASTLINE)
    bx.add_feature(cartopy.feature.BORDERS, linestyle='-', alpha=.5)
    bx.gridlines(crs=crs_latlon, linewidth=0.3, linestyle='-')
    bx.set_xticks(np.arange(-180, 180, 45), crs=crs_latlon)
    bx.set_yticks(np.arange(-90, 90, 30), crs=crs_latlon)
    
    lon_formatter = LongitudeFormatter(zero_direction_label=True)
    lat_formatter = LatitudeFormatter()
    bx.xaxis.set_major_formatter(lon_formatter)
    bx.yaxis.set_major_formatter(lat_formatter)
    bx.tick_params(labelsize=6)
    plt.tight_layout()
    
    #Titulo
    #plt.title(nombre_titulo, fontsize=6, y=2.2, x = -17) # con esto el titulo queda centrado 
                                                          # pero al guardar lo corta mal al titulo
    #Guardar figura
    plt.savefig(nombre_archivo + '.jpg')