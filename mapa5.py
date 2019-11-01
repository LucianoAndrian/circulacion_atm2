#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 01:19:51 2019

@author: auri
"""

#Abrimos librerias necesarias
import numpy as np
from matplotlib import pyplot as plt
import cartopy.feature
from cartopy.mpl.ticker import LongitudeFormatter, LatitudeFormatter
import cartopy.crs as ccrs
import os
#L = [LONMIN, LONMAX, LATMIN, LATMAX]
#cmap = 'rainbow'
#nombre_titulo = 'forzante'
#nombre_archivo = 'forzante_tiempo_50_EB1'

def mapa5(cmin,cmax,ncont,lat,lat4,lon,L,VAR1,VAR2,U,V,cmap,nombre_titulo,nombre_archivo):
    #dir = '/home/auri/Facultad/Materias/Circulacion/TP6/' # Luchi
    #script_dir = os.path.dirname(dir)
    #results_dir = os.path.join(script_dir, 'salidas/')  
    #Pasamos las latitudes/longitudes del dataset a una reticula para graficar
    lons, lats = np.meshgrid(lon, lat)
    lons2, lats2 = np.meshgrid(lon, lat4)
    
    clevs = np.linspace(cmin, cmax, ncont)
    
    #Creamos figura
    fig=plt.figure(figsize=(6,4),dpi=300) # dpi enorme para que tenga buena definicion. 
    
    #Definimos proyección
    ax = plt.axes(projection=ccrs.PlateCarree(central_longitude=250))
    crs_latlon = ccrs.PlateCarree()
    ax.set_extent(L, crs=crs_latlon)
   
    #Graficamos
    im=ax.contourf(lons, lats, VAR1, clevs, cmap=plt.get_cmap(cmap), extend='both', transform=crs_latlon)
    anom = ax.contour(lons, lats, VAR2, xtend='both', transform=crs_latlon, linewidths=0.5, colors = "black", alpha = 0.8)
    ax.clabel(anom, inline=1, fontsize = 5)
    ax.quiver(lons2[::3,::3], lats2[::3,::3], U[::3,::3], V[::3,::3],width = 0.002, pivot = "tail", scale = 1 / 0.05,
                   transform = crs_latlon, color = "black")
    #plt.quiverkey(Q, 0.9, 0.9, 1, r'$1 \frac{m}{s}$', labelpos='E', coordinates='figure')    
    
    #Agregamos barra de colores
    cb = plt.colorbar(im, fraction=0.052, pad=0.04, shrink=0.8, aspect=8)
    cb.ax.tick_params(labelsize=6)
    #Características del mapa
    ax.add_feature(cartopy.feature.LAND, facecolor='#d9d9d9')
    ax.add_feature(cartopy.feature.COASTLINE)
    ax.add_feature(cartopy.feature.BORDERS, linestyle='-', alpha=.5)
    ax.gridlines(crs=crs_latlon, linewidth=0.3, linestyle='-')
    ax.set_xticks(np.arange(180, 300, 45), crs=crs_latlon)
    ax.set_yticks(np.arange(-60, 10, 10 ), crs=crs_latlon)
    lon_formatter = LongitudeFormatter(zero_direction_label=True)
    lat_formatter = LatitudeFormatter()
    ax.xaxis.set_major_formatter(lon_formatter)
    ax.yaxis.set_major_formatter(lat_formatter)
    ax.tick_params(labelsize=6)
    plt.tight_layout()
    #Características del mapa
    
    #Titulo
    plt.title(nombre_titulo, fontsize=6, y=0.98, loc="center")
    
    #Guardar figura
    plt.savefig(nombre_archivo + '.jpg')
    plt.close()
