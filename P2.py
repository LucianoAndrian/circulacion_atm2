#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 16:49:18 2019
as
@author:   auri
"""
import numpy as np
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math
import time 
import os
# os.chdir('/Users/mini/Documents/Circulación/Atmósfera')
import xarray as xr
from netCDF4 import Dataset 
import cartopy.feature
from cartopy.mpl.ticker import LongitudeFormatter, LatitudeFormatter
import cartopy.crs as ccrs
from DerY import derivy 
from numpy import empty
# nuestras funciones
from mapa import mapa
from Estado_basico import Estado_basico
from mapa2 import mapa2
from hovmoller import hovmoller

#%%
# Estado basico 1 pert1 EB1P1
dir = '/home/auri/Facultad/Materias/Circulacion/TP5/Simulaciones/' # Luchi
dS = xr.open_dataset(dir+'EB1P1_concatenado.nc', decode_times=False) #Abro el NetCdf
print(dS)

forzante = dS['fr'].values
u=dS['ucomp'].values
v=dS['vcomp'].values
forzante = dS['fr'].values
vort=dS['vor'].values
psi = dS['stream'].values

lat=dS['lat'].values
lon=dS['lon'].values

# para graficar
LONMIN= 0
LONMAX= 359
LATMIN= -88
LATMAX= 88
L = [LONMIN, LONMAX, LATMIN, LATMAX]
cmap = 'rainbow'

# usando funcion "estado_basico" 
# ya calcula el estado basico (la correccion) 
psi_c = Estado_basico(psi, lat, lon)
#%%

# anomalia

# dia 2 de pert (51)
anomalia_psi_dia2 = psi_c - psi[51,:,:]


VAR = anomalia_psi_dia2 #es la vorticidad relativa
cmin = -4350000
cmax =  5080000
ncont = 15
clevs = np.linspace(cmin, cmax, ncont)
nombre_titulo = 'Estado basico 1 perturbacion 1 Anomalia de $\Psi$ dia 2'
nombre_archivo = 'EB1P1_psi_dia2_global'

fig = mapa(cmin,cmax,ncont,lat,lon,L,VAR,cmap,nombre_titulo,nombre_archivo)


# anomalia psi dia 4

anomalia_psi_dia4 = psi_c - psi[53,:,:]

VAR = anomalia_psi_dia4 #es la vorticidad relativa
cmin = -4350000
cmax =  5080000
ncont = 15
clevs = np.linspace(cmin, cmax, ncont)
cmap = 'rainbow'
nombre_titulo = 'Estado basico 1 perturbacion 1 Anomalia de $\Psi$ dia 4'
nombre_archivo = 'EB1P1_psi_dia4_global'

fig = mapa(cmin,cmax,ncont,lat,lon,L,VAR,cmap,nombre_titulo,nombre_archivo)


#anomalia psi dia 8

anomalia_psi_dia8 = psi_c - psi[57,:,:]

VAR = anomalia_psi_dia8 #es la vorticidad relativa
cmin = -4350000
cmax =  5080000
ncont = 15
clevs = np.linspace(cmin, cmax, ncont)
cmap = 'rainbow'
nombre_titulo = 'Estado basico 1 perturbacion 1 Anomalia de $\Psi$ dia 8'
nombre_archivo = 'EB1P1_psi_dia8_global'

fig = mapa(cmin,cmax,ncont,lat,lon,L,VAR,cmap,nombre_titulo,nombre_archivo)



# en el cuadro 90S-10N y 60E-180O 
# 90S es primera fila de las matrices, 10N es fila 71
#60E es fila 43, 180O es 128 columna

lat2 = lat[0:71]
lon2 = lon[43:128]
LONMIN= 60
LONMAX= 180
LATMIN= -88
LATMAX= 10
L = [LONMIN, LONMAX, LATMIN, LATMAX]
anomalia_psi_dia2 = psi_c - psi[51,:,:]

VAR = anomalia_psi_dia2[0:71,43:128] 
cmin = -4350000
cmax =  5080000
ncont = 15
clevs = np.linspace(cmin, cmax, ncont)
nombre_titulo = 'Estado basico 1 perturbacion 1 Anomalia de $\Psi$ dia 2'
nombre_archivo = 'EB1P1_psi_dia2_cuadradito'

# usando funcion mapa2, q grafica en la zona pedida

fig = mapa2(cmin,cmax,ncont,lat2,lon2,L,VAR,cmap,nombre_titulo,nombre_archivo)

VAR = anomalia_psi_dia4[0:71,43:128] 
cmin = -4350000
cmax =  5080000
ncont = 15
clevs = np.linspace(cmin, cmax, ncont)
nombre_titulo = 'Estado basico 1 perturbacion 1 Anomalia de $\Psi$ dia 4'
nombre_archivo = 'EB1P1_psi_dia4_cuadradito'

fig = mapa2(cmin,cmax,ncont,lat2,lon2,L,VAR,cmap,nombre_titulo,nombre_archivo)

VAR = anomalia_psi_dia8[0:71,43:128] 
cmin = -4350000
cmax =  5080000
ncont = 15
clevs = np.linspace(cmin, cmax, ncont)
nombre_titulo = 'Estado basico 1 perturbacion 1 Anomalia de $\Psi$ dia 8'
nombre_archivo = 'EB1P1_psi_dia8_cuadradito'

fig = mapa2(cmin,cmax,ncont,lat2,lon2,L,VAR,cmap,nombre_titulo,nombre_archivo)
#%%


# Hovmoller
# zonal
# solo los dias de la perturbacion 50-59

# usando la funcion hovmoller. # ya selecciona los dias,, grafica y guarda los graficos

hovmoller(psi_c, psi, lon, lat, "1", "1", "EB1P1")
