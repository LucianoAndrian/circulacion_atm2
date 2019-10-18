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
from hovmoller_pert1 import hovmoller1
from hovmoller_pert2 import hovmoller2

dir = '/home/auri/Facultad/Materias/Circulacion/TP5/Simulaciones/' # Luchi

#%%
###############
#### EB1P1 ####
###############


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

### ANOMALIA ###

# dia 2 de pert (51)
anomalia_psi_dia2 = psi[51,:,:] - psi_c

VAR = anomalia_psi_dia2 #es la vorticidad relativa
cmin = -5080000
cmax = 4350000
ncont = 15
clevs = np.linspace(cmin, cmax, ncont)
nombre_titulo = 'Estado basico 1 perturbacion 1 Anomalia de $\Psi$ dia 2'
nombre_archivo = 'EB1P1_psi_dia2_global'

fig = mapa(cmin,cmax,ncont,lat,lon,L,VAR,cmap,nombre_titulo,nombre_archivo)

###############################################################################

# anomalia psi dia 4
anomalia_psi_dia4 = psi[53,:,:] - psi_c

VAR = anomalia_psi_dia4 #es la vorticidad relativa
cmin = -5080000
cmax = 4350000
ncont = 15
clevs = np.linspace(cmin, cmax, ncont)
cmap = 'rainbow'
nombre_titulo = 'Estado basico 1 perturbacion 1 Anomalia de $\Psi$ dia 4'
nombre_archivo = 'EB1P1_psi_dia4_global'

fig = mapa(cmin,cmax,ncont,lat,lon,L,VAR,cmap,nombre_titulo,nombre_archivo)

###############################################################################

#anomalia psi dia 8
anomalia_psi_dia8 = psi[57,:,:] - psi_c

VAR = anomalia_psi_dia8 #es la vorticidad relativa
cmin = -5080000
cmax = 4350000
ncont = 15
clevs = np.linspace(cmin, cmax, ncont)
cmap = 'rainbow'
nombre_titulo = 'Estado basico 1 perturbacion 1 Anomalia de $\Psi$ dia 8'
nombre_archivo = 'EB1P1_psi_dia8_global'

fig = mapa(cmin,cmax,ncont,lat,lon,L,VAR,cmap,nombre_titulo,nombre_archivo)

###############################################################################

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


VAR = anomalia_psi_dia2[0:71,43:128] 
cmin = -5080000
cmax = 4350000
ncont = 15
clevs = np.linspace(cmin, cmax, ncont)
nombre_titulo = 'Estado basico 1 perturbacion 1 Anomalia de $\Psi$ dia 2'
nombre_archivo = 'EB1P1_psi_dia2_cuadradito'

# usando funcion mapa2, q grafica en la zona pedida
fig = mapa2(cmin,cmax,ncont,lat2,lon2,L,VAR,cmap,nombre_titulo,nombre_archivo)

###############################################################################

VAR = anomalia_psi_dia4[0:71,43:128] 
cmin = -5080000
cmax = 4350000
ncont = 15
clevs = np.linspace(cmin, cmax, ncont)
nombre_titulo = 'Estado basico 1 perturbacion 1 Anomalia de $\Psi$ dia 4'
nombre_archivo = 'EB1P1_psi_dia4_cuadradito'

fig = mapa2(cmin,cmax,ncont,lat2,lon2,L,VAR,cmap,nombre_titulo,nombre_archivo)

###############################################################################

VAR = anomalia_psi_dia8[0:71,43:128] 
cmin = -5080000
cmax = 4350000
ncont = 15
clevs = np.linspace(cmin, cmax, ncont)
nombre_titulo = 'Estado basico 1 perturbacion 1 Anomalia de $\Psi$ dia 8'
nombre_archivo = 'EB1P1_psi_dia8_cuadradito'

fig = mapa2(cmin,cmax,ncont,lat2,lon2,L,VAR,cmap,nombre_titulo,nombre_archivo)

###############################################################################
# diferencia de anomalia  con respecto al estado basico 1???? no entiendo que es lo q pide
###############################################################################
#%%
### HOVMOLLER ###
# zonal
# solo los dias de la perturbacion 50-59

# usando la funcion hovmoller. # ya selecciona los dias,, grafica y guarda los graficos
hovmoller1(psi_c, psi, lon, lat, "1", "1", "EB1P1")



###############################################################################
###############################################################################
###############################################################################
#%%
# EB1P2 [este esta mal, o nosotros tenemos el archivo mal.. la cuestion es que no tiene perturbacion.]



###############################################################################
###############################################################################
###############################################################################
#%%
################
#### EB2P1 #####
################

dS = xr.open_dataset(dir+'EB2P1_concatenado.nc', decode_times=False) #Abro el NetCdf
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


psi_c = Estado_basico(psi, lat, lon)  # estado basico


#%%
#(copiar y pegar de arriba, se podria hacer un for pero cmin y cmax hay que setearlos a mano en cada caso)

# anomalia

# dia 2 de pert (51)
anomalia_psi_dia2 = psi[51,:,:] - psi_c

VAR = anomalia_psi_dia2 #es la vorticidad relativa
cmin = -5080000
cmax = 4350000
ncont = 15
clevs = np.linspace(cmin, cmax, ncont)
nombre_titulo = 'Estado basico 2 perturbacion 1 Anomalia de $\Psi$ dia 2'
nombre_archivo = 'EB2P1_psi_dia2_global'

fig = mapa(cmin,cmax,ncont,lat,lon,L,VAR,cmap,nombre_titulo,nombre_archivo)

###############################################################################

# anomalia psi dia 4
anomalia_psi_dia4 = psi[53,:,:] - psi_c

VAR = anomalia_psi_dia4 #es la vorticidad relativa
cmin = -5080000
cmax = 4350000
ncont = 15
clevs = np.linspace(cmin, cmax, ncont)
cmap = 'rainbow'
nombre_titulo = 'Estado basico 2 perturbacion 1 Anomalia de $\Psi$ dia 4'
nombre_archivo = 'EB2P1_psi_dia4_global'

fig = mapa(cmin,cmax,ncont,lat,lon,L,VAR,cmap,nombre_titulo,nombre_archivo)

###############################################################################

#anomalia psi dia 8
anomalia_psi_dia8 = psi[57,:,:] - psi_c

VAR = anomalia_psi_dia8 #es la vorticidad relativa
cmin = -5080000
cmax = 4350000
ncont = 15
clevs = np.linspace(cmin, cmax, ncont)
cmap = 'rainbow'
nombre_titulo = 'Estado basico 2 perturbacion 1 Anomalia de $\Psi$ dia 8'
nombre_archivo = 'EB2P1_psi_dia8_global'

fig = mapa(cmin,cmax,ncont,lat,lon,L,VAR,cmap,nombre_titulo,nombre_archivo)

###############################################################################

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


VAR = anomalia_psi_dia2[0:71,43:128] 
cmin = -5080000
cmax = 4350000
ncont = 15
clevs = np.linspace(cmin, cmax, ncont)
nombre_titulo = 'Estado basico 2 perturbacion 1 Anomalia de $\Psi$ dia 2'
nombre_archivo = 'EB2P1_psi_dia2_cuadradito'
# usando funcion mapa2, q grafica en la zona pedida
fig = mapa2(cmin,cmax,ncont,lat2,lon2,L,VAR,cmap,nombre_titulo,nombre_archivo)

###############################################################################

VAR = anomalia_psi_dia4[0:71,43:128] 
cmin = -5080000
cmax = 4350000
ncont = 15
clevs = np.linspace(cmin, cmax, ncont)
nombre_titulo = 'Estado basico 2 perturbacion 1 Anomalia de $\Psi$ dia 4'
nombre_archivo = 'EB2P1_psi_dia4_cuadradito'

fig = mapa2(cmin,cmax,ncont,lat2,lon2,L,VAR,cmap,nombre_titulo,nombre_archivo)

###############################################################################

VAR = anomalia_psi_dia8[0:71,43:128] 
cmin = -5080000
cmax = 4350000
ncont = 15
clevs = np.linspace(cmin, cmax, ncont)
nombre_titulo = 'Estado basico 2 perturbacion 1 Anomalia de $\Psi$ dia 8'
nombre_archivo = 'EB2P1_psi_dia8_cuadradito'

fig = mapa2(cmin,cmax,ncont,lat2,lon2,L,VAR,cmap,nombre_titulo,nombre_archivo)

###############################################################################
### HOVMOLLER ###
hovmoller1(psi_c, psi, lon, lat, "2", "1", "EB2P1")

#%%
###############
#### EB2P2 ####
###############

dS = xr.open_dataset(dir+'EB2P2_concatenado.nc', decode_times=False) #Abro el NetCdf
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

psi_c = Estado_basico(psi, lat, lon)  # estado basico

#%%


### ANOMALIA ###

# dia 2 de pert (51)
anomalia_psi_dia2 = psi[51,:,:] - psi_c

VAR = anomalia_psi_dia2 #es la vorticidad relativa
cmin = -5080000
cmax = 4350000
ncont = 15
clevs = np.linspace(cmin, cmax, ncont)
nombre_titulo = 'Estado basico 2 perturbacion 2 Anomalia de $\Psi$ dia 2'
nombre_archivo = 'EB2P2_psi_dia2_global'

fig = mapa(cmin,cmax,ncont,lat,lon,L,VAR,cmap,nombre_titulo,nombre_archivo)

###############################################################################

# anomalia psi dia 4
anomalia_psi_dia4 = psi[53,:,:] - psi_c

VAR = anomalia_psi_dia4 #es la vorticidad relativa
cmin = -5080000
cmax = 4350000
ncont = 15
clevs = np.linspace(cmin, cmax, ncont)
cmap = 'rainbow'
nombre_titulo = 'Estado basico 2 perturbacion 2 Anomalia de $\Psi$ dia 4'
nombre_archivo = 'EB2P2_psi_dia4_global'

fig = mapa(cmin,cmax,ncont,lat,lon,L,VAR,cmap,nombre_titulo,nombre_archivo)

###############################################################################

#anomalia psi dia 8
anomalia_psi_dia8 = psi[57,:,:] - psi_c

VAR = anomalia_psi_dia8 #es la vorticidad relativa
cmin = -5080000
cmax = 4350000
ncont = 15
clevs = np.linspace(cmin, cmax, ncont)
cmap = 'rainbow'
nombre_titulo = 'Estado basico 2 perturbacion 2 Anomalia de $\Psi$ dia 8'
nombre_archivo = 'EB2P2_psi_dia8_global'

fig = mapa(cmin,cmax,ncont,lat,lon,L,VAR,cmap,nombre_titulo,nombre_archivo)

###############################################################################

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
cmin = -5080000
cmax = 4350000
ncont = 15
clevs = np.linspace(cmin, cmax, ncont)
nombre_titulo = 'Estado basico 2 perturbacion 2 Anomalia de $\Psi$ dia 2'
nombre_archivo = 'EB2P2_psi_dia2_cuadradito'

# usando funcion mapa2, q grafica en la zona pedida

fig = mapa2(cmin,cmax,ncont,lat2,lon2,L,VAR,cmap,nombre_titulo,nombre_archivo)

###############################################################################

VAR = anomalia_psi_dia4[0:71,43:128] 
cmin = -5080000
cmax = 4350000
ncont = 15
clevs = np.linspace(cmin, cmax, ncont)
nombre_titulo = 'Estado basico 2 perturbacion 2 Anomalia de $\Psi$ dia 4'
nombre_archivo = 'EB2P2_psi_dia4_cuadradito'

fig = mapa2(cmin,cmax,ncont,lat2,lon2,L,VAR,cmap,nombre_titulo,nombre_archivo)

###############################################################################

VAR = anomalia_psi_dia8[0:71,43:128] 
cmin = -5080000
cmax = 4350000
ncont = 15
clevs = np.linspace(cmin, cmax, ncont)
nombre_titulo = 'Estado basico 2 perturbacion 2 Anomalia de $\Psi$ dia 8'
nombre_archivo = 'EB2P2_psi_dia8_cuadradito'

fig = mapa2(cmin,cmax,ncont,lat2,lon2,L,VAR,cmap,nombre_titulo,nombre_archivo)

###############################################################################

hovmoller2(psi_c, psi, lon, lat, "2", "2", "EB2P2")
