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
from DerX import derivx
from numpy import empty
# nuestras funciones
from mapa import mapa
from Estado_basico import Estado_basico
from mapa2 import mapa2
from hovmoller_pert1 import hovmoller1
from hovmoller_pert2 import hovmoller2

dir = '/home/auri/Facultad/Materias/Circulacion/TP6/' # Luchi
script_dir = os.path.dirname(dir)
#%%

dS = xr.open_dataset(dir+'EB1P1_concatenado.nc', decode_times=False) #Abro el NetCdf
print(dS)

psi = dS['stream'].values

lat=dS['lat'].values
lon=dS['lon'].values


u = dS["ucomp"].values
v = dS["vcomp"].values
h = dS["h"].values
H = 40000 #h0 del name list
g = 9.8
eta = (h - H)/9.8
rho = 1

# aplicar estado basico

u_b = Estado_basico(u, lat, lon)
v_b = Estado_basico(v, lat, lon)
h_b = Estado_basico(h, lat, lon)
eta_b = Estado_basico(eta, lat, lon)

u_e = u - u_b
v_e = v - v_b
eta_e = eta - eta_b

# energi cinetica
Ec = (rho*H)/2*(u**2 + v**2)
Ec_b = (rho*H)/2*(u_b**2 + v_b**2)
Ec_e = (rho*H)/2*(u_e**2 + v_e**2)


# energi potencial
Ep = (rho*g)/2*(eta**2+H**2) # ENERGIA POTENCIAL INSTANTANEA
Ep_b = (rho*g)/2*(eta_b**2+H**2) # ENERGIA POTENCIAL DEL FLUJO MEDIO
Ep_e = (rho*g)/2*(eta_e**2) # ENERGIA POTENCIAL DE LAS PERTURBACIONES

# para el ej2
# derivx requiere una escala en x que depende de la latitud 
R = 6370000
dx = (R*2*np.pi)/256
dy = (R*np.pi)/128


Ec_e_x = derivx(Ec_e, dx, lat)
Ec_e_y = derivy(Ec_e, dy)

Adv = -(u_b*Ec_e_x + v_b*Ec_e_y + u_e*Ec_e_x + v_e*Ec_e_y)  #adveccion total

u_b_x = derivx(u_b, dx, lat)
u_b_y = derivy(u_b, dy)
v_b_x = derivx(v_b, dx, lat)
v_b_y = derivy(v_b, dy)

C_Ec_b_Ec_e = -rho*H*(u_e**2*u_b_x + u_e*v_e*u_b_y + u_e*v_e*v_b_x + v_e**2*v_b_y)


# dispersion

Dispx = -g*H*(# derivadas #)


# viento geostrofico para el flujo..
R = 6370000
omega = 7.27*10**-5
lat_g = lat*np.pi/180 # regla de tres para pasar de grados a radianes.
beta = omega*np.cos(lat_g)/R
long_arco = R*lat_g


# haciendo lo mismo que antes pero de forma matricial simplifica los proximos pasos

lon_m, lat_m = np.meshgrid(lon, lat) 
lat_g_m = lat_m*np.pi/180 # regla de tres para pasar de grados a radianes.


Vgx = -1/(2*7.27e-05*np.cos(lat_g_m)/R)*derivy(h, dy)
Vgy = 1/(2*7.27e-05*np.cos(lat_g_m)/R)*derivx(h, dx, lat)
Vgx_b = Estado_basico(Vgx, lat, lon)
Vgy_b = Estado_basico(Vgy, lat, lon)

Vgx_e = u - Vgx_b
Vgy_e = v - Vgy_b
