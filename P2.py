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

psi = dS['stream'].values

lat=dS['lat'].values
lon=dS['lon'].values

# para graficar
LONMIN= 0
LONMAX= 359
LATMIN= -88
LATMAX= 88
L = [LONMIN, LONMAX, LATMIN, LATMAX]
cmap = 'RdBu_r'

psi_c = Estado_basico(psi, lat, lon)



anomalia_psi_dia2_eb1p1 = psi[51,:,:] - psi_c
anomalia_psi_dia4_eb1p1 = psi[53,:,:] - psi_c
anomalia_psi_dia8_eb1p1 = psi[57,:,:] - psi_c

anomalia_psi_EB1P1 = (anomalia_psi_dia2_eb1p1, anomalia_psi_dia4_eb1p1, anomalia_psi_dia8_eb1p1)

cmin = -5000000
cmax = 5000000
ncont = 25
clevs = np.linspace(cmin, cmax, ncont)

dia = ("1" , "2", "3")
num = (0, 1, 2)

for i in num:
    VAR = anomalia_psi_EB1P1[i]
    nombre_titulo = 'Estado basico 1 perturbacion 1 Anomalia de $\Psi$ dia ' + dia[i]
    nombre_archivo = "EB1P1_psi_dia" + dia[i] + "_global"
    fig = mapa(cmin,cmax,ncont,lat,lon,L,VAR,cmap,nombre_titulo,nombre_archivo)
    


# en el cuadrante de la perturbacion

lat2 = lat[0:71]
lon2 = lon[120:255]
LONMIN= 230
LONMAX= 360
LATMIN= -88
LATMAX= 10
L = [LONMIN, LONMAX, LATMIN, LATMAX]
cmin = -5000000
cmax = 5000000
ncont = 25
clevs = np.linspace(cmin, cmax, ncont)

anomalia_psi_EB1P1_C = (anomalia_psi_dia2_eb1p1[0:71,120:255], anomalia_psi_dia4_eb1p1[0:71,120:255] , anomalia_psi_dia8_eb1p1[0:71,120:255])  

for i in num:
    VAR =  anomalia_psi_EB1P1_C[i]
    nombre_titulo = 'Estado basico 1 perturbacion 1 Anomalia de $\Psi$ dia ' + dia[i]
    nombre_archivo = "EB1P1_psi_dia" + dia[i] + "_cuadrante"
    fig = mapa2(cmin,cmax,ncont,lat2,lon2,L,VAR,cmap,nombre_titulo,nombre_archivo)



hovmoller1(psi_c, psi, lon, lat, "1", "1", "EB1P1")



#%%
################
#### EB1P2 #####
################

dS = xr.open_dataset(dir+'EB1P2_concatenado.nc', decode_times=False) #Abro el NetCdf
print(dS)

psi = dS['stream'].values

lat=dS['lat'].values
lon=dS['lon'].values

# para graficar
LONMIN= 0
LONMAX= 359
LATMIN= -88
LATMAX= 88
L = [LONMIN, LONMAX, LATMIN, LATMAX]
cmap = 'RdBu_r'

psi_c = Estado_basico(psi, lat, lon)

anomalia_psi_dia2_eb1p2 = psi[51,:,:] - psi_c
anomalia_psi_dia4_eb1p2 = psi[53,:,:] - psi_c
anomalia_psi_dia8_eb1p2 = psi[57,:,:] - psi_c

anomalia_psi_EB1P2 = (anomalia_psi_dia2_eb1p2, anomalia_psi_dia4_eb1p2, anomalia_psi_dia8_eb1p2)

cmin = -5000000
cmax = 5000000
ncont = 25
clevs = np.linspace(cmin, cmax, ncont)

dia = ("1" , "2", "3")
num = (0, 1, 2)

for i in num:
    VAR = anomalia_psi_EB1P2[i]
    nombre_titulo = 'Estado basico 1 perturbacion 2 Anomalia de $\Psi$ dia ' + dia[i]
    nombre_archivo = "EB1P2_psi_dia" + dia[i] + "_global"
    fig = mapa(cmin,cmax,ncont,lat,lon,L,VAR,cmap,nombre_titulo,nombre_archivo)
   
# en el cuadrante de la perturbacion    

lat2 = lat[0:71]
lon2 = lon[120:255]
LONMIN= 230
LONMAX= 360
LATMIN= -88
LATMAX= 10
L = [LONMIN, LONMAX, LATMIN, LATMAX]
cmin = -5000000
cmax = 5000000
ncont = 25
clevs = np.linspace(cmin, cmax, ncont)

anomalia_psi_EB1P2_C = (anomalia_psi_dia2_eb1p2[0:71,120:255], anomalia_psi_dia4_eb1p2[0:71,120:255] , anomalia_psi_dia8_eb1p2[0:71,120:255])  

for i in num:
    VAR =  anomalia_psi_EB1P2_C[i]
    nombre_titulo = 'Estado basico 1 perturbacion 2 Anomalia de $\Psi$ dia ' + dia[i]
    nombre_archivo = "EB1P2_psi_dia" + dia[i] + "_cuadrante"
    fig = mapa2(cmin,cmax,ncont,lat2,lon2,L,VAR,cmap,nombre_titulo,nombre_archivo)


hovmoller2(psi_c, psi, lon, lat, "1", "2", "EB1P2")




#%%
################
#### EB2P1 #####
################

dS = xr.open_dataset(dir+'EB2P1_concatenado.nc', decode_times=False) #Abro el NetCdf
print(dS)

psi = dS['stream'].values

lat=dS['lat'].values
lon=dS['lon'].values

# para graficar
LONMIN= 0
LONMAX= 359
LATMIN= -88
LATMAX= 88
L = [LONMIN, LONMAX, LATMIN, LATMAX]
cmap = 'RdBu_r'

psi_c = Estado_basico(psi, lat, lon)  # estado basico


anomalia_psi_dia2_eb2p1 = psi[51,:,:] - psi_c
anomalia_psi_dia4_eb2p1 = psi[53,:,:] - psi_c
anomalia_psi_dia8_eb2p1 = psi[57,:,:] - psi_c


anomalia_psi_EB2P1 = (anomalia_psi_dia2_eb2p1, anomalia_psi_dia4_eb2p1, anomalia_psi_dia8_eb2p1)


cmin = -5000000
cmax = 5000000
ncont = 25
clevs = np.linspace(cmin, cmax, ncont)

dia = ("1" , "2", "3")
num = (0, 1, 2)

for i in num:
    VAR = anomalia_psi_EB2P1[i]
    nombre_titulo = 'Estado basico 2 perturbacion 1 Anomalia de $\Psi$ dia ' + dia[i]
    nombre_archivo = "EB2P1_psi_dia" + dia[i] + "_global"
    fig = mapa(cmin,cmax,ncont,lat,lon,L,VAR,cmap,nombre_titulo,nombre_archivo)
    


# en el cuadrante de la perturbacion

lat2 = lat[0:71]
lon2 = lon[120:255]
LONMIN= 230
LONMAX= 360
LATMIN= -88
LATMAX= 10
L = [LONMIN, LONMAX, LATMIN, LATMAX]
cmin = -5000000
cmax = 5000000
ncont = 25
clevs = np.linspace(cmin, cmax, ncont)

anomalia_psi_EB2P1_C = (anomalia_psi_dia2_eb2p1[0:71,120:255], anomalia_psi_dia4_eb2p1[0:71,120:255] , anomalia_psi_dia8_eb2p1[0:71,120:255])  

for i in num:
    VAR =  anomalia_psi_EB2P1_C[i]
    nombre_titulo = 'Estado basico 2 perturbacion 1 Anomalia de $\Psi$ dia ' + dia[i]
    nombre_archivo = "EB2P1_psi_dia" + dia[i] + "_cuadrante"
    fig = mapa2(cmin,cmax,ncont,lat2,lon2,L,VAR,cmap,nombre_titulo,nombre_archivo)


hovmoller1(psi_c, psi, lon, lat, "2", "1", "EB2P1")


#%%
###############
#### EB2P2 ####
###############

dS = xr.open_dataset(dir+'EB2P2_concatenado.nc', decode_times=False) #Abro el NetCdf
print(dS)

psi = dS['stream'].values

lat=dS['lat'].values
lon=dS['lon'].values

# para graficar
LONMIN= 0
LONMAX= 359
LATMIN= -88
LATMAX= 88
L = [LONMIN, LONMAX, LATMIN, LATMAX]
cmap = 'RdBu_r'

psi_c = Estado_basico(psi, lat, lon)  # estado basico

anomalia_psi_dia2_eb2p2 = psi[51,:,:] - psi_c
anomalia_psi_dia4_eb2p2 = psi[53,:,:] - psi_c
anomalia_psi_dia8_eb2p2 = psi[57,:,:] - psi_c


anomalia_psi_EB2P2  = (anomalia_psi_dia2_eb2p2, anomalia_psi_dia4_eb2p2, anomalia_psi_dia8_eb2p2)

cmin = -5000000
cmax = 5000000
ncont = 25
clevs = np.linspace(cmin, cmax, ncont)

dia = ("1" , "2", "3")
num = (0, 1, 2)

for i in num:
    VAR = anomalia_psi_EB2P2[i]
    nombre_titulo = 'Estado basico 2 perturbacion 2 Anomalia de $\Psi$ dia ' + dia[i]
    nombre_archivo = "EB2P2_psi_dia" + dia[i] + "_global"
    fig = mapa(cmin,cmax,ncont,lat,lon,L,VAR,cmap,nombre_titulo,nombre_archivo)
    

# en el cuadrante de la perturbacion

lat2 = lat[0:71]
lon2 = lon[120:255]
LONMIN= 230
LONMAX= 360
LATMIN= -88
LATMAX= 10
L = [LONMIN, LONMAX, LATMIN, LATMAX]
cmin = -5000000
cmax = 5000000
ncont = 25
clevs = np.linspace(cmin, cmax, ncont)

anomalia_psi_EB2P2_C = (anomalia_psi_dia2_eb2p2[0:71,120:255], anomalia_psi_dia4_eb2p2[0:71,120:255] , anomalia_psi_dia8_eb2p2[0:71,120:255])  

for i in num:
    VAR =  anomalia_psi_EB2P2_C[i]
    nombre_titulo = 'Estado basico 2 perturbacion 2 Anomalia de $\Psi$ dia ' + dia[i]
    nombre_archivo = "EB2P2_psi_dia" + dia[i] + "_cuadrante"
    fig = mapa2(cmin,cmax,ncont,lat2,lon2,L,VAR,cmap,nombre_titulo,nombre_archivo)


hovmoller2(psi_c, psi, lon, lat, "2", "2", "EB2P2")


#%%
### item b - Diferencias entre los estados

anomalias_p1 = (anomalia_psi_dia2_eb1p1, anomalia_psi_dia2_eb2p1, anomalia_psi_dia4_eb1p1, anomalia_psi_dia4_eb2p1,
        anomalia_psi_dia8_eb1p1, anomalia_psi_dia8_eb2p1)

titulo = (" 2", " 2", " 4", " 4", " 8", " 8")
archivo = ("_2", "_2", "_4", "_4", "_8", "_8")
num = (0, 1, 2)

for i in num:
    i = i + i
    VAR = anomalias_p1[i] - anomalias_p1[i+1]
    cmin = -1300000
    cmax = 1300000
    ncont = 25
    clevs = np.linspace(cmin, cmax, ncont)
    nombre_titulo = "Diferencia anomalia 1 Dia" + titulo[i]
    nombre_archivo = "dif_P1_dia" + archivo[i]
    fig = mapa(cmin,cmax,ncont,lat,lon,L,VAR,cmap,nombre_titulo,nombre_archivo)


anomalias_p2 = (anomalia_psi_dia2_eb1p2, anomalia_psi_dia2_eb2p2, anomalia_psi_dia4_eb1p2, anomalia_psi_dia4_eb2p2,
        anomalia_psi_dia8_eb1p2, anomalia_psi_dia8_eb2p2)



for i in num:
    i = i + i
    VAR = anomalias_p2[i] - anomalias_p2[i+1]
    cmin = -1300000
    cmax = 1300000
    ncont = 25
    clevs = np.linspace(cmin, cmax, ncont)
    nombre_titulo = "Diferencia anomalia 2 Dia" + titulo[i]
    nombre_archivo = "dif_P2_dia" + archivo[i]                       #\m/
    fig = mapa(cmin,cmax,ncont,lat,lon,L,VAR,cmap,nombre_titulo,nombre_archivo)

