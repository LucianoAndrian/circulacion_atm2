#!/usr/bin/env python3
# -- coding: utf-8 --
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

os.chdir('/Users/mini/Documents/Circulación/Atmósfera/P3/')

import xarray as xr
from netCDF4 import Dataset 
import cartopy.feature
from cartopy.mpl.ticker import LongitudeFormatter, LatitudeFormatter
import cartopy.crs as ccrs
from DerY import derivy 
#from DerX import derivx
from numpy import empty
# nuestras funciones
from Estado_basico import Estado_basico
from mapa2 import mapa2
from mapa3 import mapa3
from mapa import mapa
#dir = '/home/auri/Facultad/Materias/Circulacion/TP6/' # Luchi
script_dir = os.path.dirname(dir)
dir = '/Users/mini/Documents/Circulación/Atmósfera/P3/' # Mili

#%%

dS = xr.open_dataset(dir+'EB1P1_concatenado.nc', decode_times=False) #Abro el NetCdf
print(dS)

lat=dS['lat'].values
lon=dS['lon'].values
u = dS["ucomp"].values
v = dS["vcomp"].values
h = dS["h"].values

H = 40000 #h0 del name list
g = 9.8 #gravedad
rho = 1 #densidad del aire

eta = (h - H)/9.8  #superficie libre 


# Calculamos el estado basico de las velocidades y la superficie libre

u_b = Estado_basico(u, lat, lon)
v_b = Estado_basico(v, lat, lon)
h_b = Estado_basico(h, lat, lon)
eta_b = Estado_basico(eta, lat, lon)

#Calculamos las perturbaciones
u_e = u - u_b           
v_e = v - v_b           
eta_e = eta - eta_b     

#%%
# Energia cinetica
Ec = (rho*H)/2*(u*2 + v*2)
Ec_b = (rho*H)/2*(u_b*2 + v_b*2)
Ec_e = (rho*H)/2*(u_e*2 + v_e*2)


# Energia potencial
Ep = (rho*g)/2*(eta*2+H*2) # Energia potencial instantanea
Ep_b = (rho*g)/2*(eta_b*2+H*2) # Energia potencial del flujo medio
Ep_e = (rho*g)/2*(eta_e**2) # Energia potencial de las perturbaciones

#Defino parámetros para poder graficar
LONMIN= 0
LONMAX= 359
LATMIN= -88
LATMAX= 88
L = [LONMIN, LONMAX, LATMIN, LATMAX]
cmap = 'Spectral_r'

VAR1 = Ec_b
VAR2 = Ep_b

cmin1 = 0   #Límites de la E cinética
cmax1 = 5
ncont = 25

cmin2 = 3.92378
cmax2 = 3.97

nombre_titulo = "Comparación EC y EP"
nombre_archivo= "Ec_Ep_EB1P1"

fig= mapa3(cmin1,cmax1,cmin2,cmax2,ncont,lat,lon,L,VAR1,VAR2,cmap,nombre_titulo,nombre_archivo)

#%%
  