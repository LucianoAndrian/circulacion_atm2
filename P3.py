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

#os.chdir('/Users/mini/Documents/Circulación/Atmósfera/P3/')  #Esto es para que se quede en el directorio que querés

import xarray as xr
from netCDF4 import Dataset 
import cartopy.feature
from cartopy.mpl.ticker import LongitudeFormatter, LatitudeFormatter
import cartopy.crs as ccrs

from DerY import derivy # LA ULTIMA QUE SUBIO LEAN
from DerX import derivx     
from numpy import empty


# nuestras funciones
from Estado_basico import Estado_basico
from mapa import mapa
from mapa2 import mapa2
from mapa3 import mapa3 ## CON CAMBIOS
from mapa4 import mapa4 ##NUEVA
from mapa5 import mapa5 ##NUEVA


dir = '/home/auri/Facultad/Materias/Circulacion/TP6/' # Luchi
script_dir = os.path.dirname(dir)
#dir = '/Users/mini/Documents/Circulación/Atmósfera/P3/' # Mili

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
eta_b = Estado_basico(eta, lat, lon)

#Calculamos las perturbaciones
u_e = u - u_b           
v_e = v - v_b           
eta_e = eta - eta_b     

#%%
# Energia cinetica
Ec = (rho*H)/2*(u**2 + v**2)
Ec_b = (rho*H)/2*(u_b**2 + v_b**2)
Ec_e = (rho*H)/2*(u_e**2 + v_e**2)


# Energia potencial
Ep = (rho*g)/2*(eta**2+H**2) # Energia potencial instantanea
Ep_b = (rho*g)/2*(eta_b**2+H**2) # Energia potencial del flujo medio
Ep_e = (rho*g)/2*(eta_e**2) # Energia potencial de las perturbaciones


# Graficos Ec y Ep del flujo medio
#Defino parámetros para poder graficar
LONMIN= 0
LONMAX= 359
LATMIN= -88
LATMAX= 88
L = [LONMIN, LONMAX, LATMIN, LATMAX]
cmap = 'Spectral_r'

VAR1 = Ec_b
VAR2 = Ep_b/10000
VAR3 = eta_e[51,:,:] #anomalia de la sfc libre dia 2 de la perturbaciòn

cmin1 = 0   #Límites de la E cinética
cmax1 = 25
ncont = 25

cmin2 = 7.8398  #Límites de E potencial 
cmax2 = 7.8412  # esto es un mierda jajaja --> la escala cambio a 1e9 porque se habian borrado los ** en el calculo de la energia

nombre_titulo = "Comparación EC y EP"
nombre_archivo= "Ec_Ep_EB1P1"

fig= mapa3(cmin1,cmax1,cmin2,cmax2,ncont,lat,lon,L,VAR1,VAR2,VAR3,cmap,nombre_titulo,nombre_archivo)


# Graficos Ec y Ep de las perturbaciones dia 2 de la perturbaciòn

VAR1 = Ec_e[51,:,:]
VAR2 = Ep_e[51,:,:]
VAR3 = eta_e[51,:,:]

cmap = 'YlOrRd' # cambiando los colores porque queda horrible sino
 
cmin1 = 0
cmax1 = 3.5
ncont = 25

cmin2 = 0
cmax2 = 0.04

nombre_titulo = ""
nombre_archivo = "Ec_Ep_EB1P1_E"
fig= mapa3(cmin1,cmax1,cmin2,cmax2,ncont,lat,lon,L,VAR1,VAR2,VAR3,cmap,nombre_titulo,nombre_archivo)
#%%

# para el ej2
# derivx requiere una escala en x que depende de la latitud 
R = 6370000
dx = (R*2*np.pi)/256
dy = (R*np.pi)/128

Ec_e_x = derivx(Ec_e, dx, lat)
Ec_e_y = derivy(Ec_e, dy)

Adv = -(u_b*Ec_e_x + v_b*Ec_e_y + u_e*Ec_e_x + v_e*Ec_e_y)  #adveccion total


# conversion barotropica

u_b_x = derivx(u_b, dx, lat)
u_b_y = derivy(u_b, dy)
v_b_x = derivx(v_b, dx, lat)
v_b_y = derivy(v_b, dy)

C_barotropica = -rho*H*(u_e**2*u_b_x + u_e*v_e*u_b_y + u_e*v_e*v_b_x + v_e**2*v_b_y)


# conversion baroclinica

Vu_ex = derivx(u_e, dx, lat)
Vv_ey = derivy(v_e, dy)
div = Vu_ex + Vv_ey

C_baroclinica = g*H*eta_e*div


# dispersion de Ec (POR LAS DUDAS REVISAR!!!)

V_eta_u_ey = derivy(eta_e*u_e,dy)
V_eta_v_ex = derivx(eta_e*v_e, dx, lat)

Disp = -g*H*(V_eta_u_ey + V_eta_v_ex)

# flujo ajestrofico

omega = 7.27e-5
lon_m, lat_m = np.meshgrid(lon, lat) 
lat_g_m = lat_m*np.pi/180 # regla de tres para pasar de grados a radianes.


# viento geostrofico

Vgx = -1/(2*omega*np.sin(lat_g_m))*derivy(h, dy)
Ugy = 1/(2*omega*np.sin(lat_g_m))*derivx(h, dx, lat)

V_ag = u - Vgx 
U_ag = v - Ugy

# viento agesotrofico

V_ag_b = Estado_basico(V_ag, lat, lon)
U_ag_b = Estado_basico(U_ag, lat, lon)

V_ag_anom = V_ag - V_ag_b
U_ag_anom = U_ag - U_ag_b

#%%
## GRAFICOS ##

# Grafico adveccion Ec_e y Ec_e dias 1234
# ver el * de la practica con respecto a graficar la adv en m2s-2dia-1 ..que??? ### VER ESTO!!!!

lat2=lat[20:67]
lon2=lon[128:214]
LONMIN= 180
LONMAX= 300
LATMIN= -60
LATMAX= 5
L = [LONMIN, LONMAX, LATMIN, LATMAX]

cmin = -1
cmax = 1
cmap = 'Spectral_r'
dia = ("1", "2", "3", "4")

for i in np.arange(0,4,1):
    VAR1 = Adv[50+i, 20:67, 128:214]
    VAR2 = Ec_e[50+i, 20:67, 128:214]/10000

    nombre_titulo = "Advecciòn de Ke y Ke - Dia " + dia[i] 
    nombre_archivo = "Adv_Ke_EB1P1_dia" + dia[i]
    
    mapa4(cmin,cmax,ncont,lat2,lon2,L,VAR1,VAR2,cmap,nombre_titulo,nombre_archivo)


# c baroclinica

cmin = -2
cmax = 2
cmap = 'Spectral_r'
dia = ("1", "2", "3", "4")

for i in np.arange(0,4,1):
    VAR1 = C_baroclinica[50+i, 20:67, 128:214]
    VAR2 = Ec_e[50+i, 20:67, 128:214]/10000

    nombre_titulo = "Conversiòn baroclìnica y Ke - Dia " + dia[i] 
    nombre_archivo = "C_baroc_Ke_EB1P1_dia" + dia[i]
    
    mapa4(cmin,cmax,ncont,lat2,lon2,L,VAR1,VAR2,cmap,nombre_titulo,nombre_archivo)
    
    
# Dispersion y flujo agesotrofico

lat3=lat[20:61]   # NUEVAS LATITUDES PARA QUE GRAFIQUE LOS VECTORES CERCA DEL ECUADOR
lon3=lon[128:214]

cmin = -60
cmax = 60
cmap = 'Spectral_r'
dia = ("1", "2", "3", "4")

for i in np.arange(0,4,1):
    VAR1 = Disp[50+i, 20:61, 128:214]
    VAR2 = Ec_e[50+i, 20:61, 128:214]/10000
    
    V =V_ag_anom[50+i, 20:61,128:214]
    U = U_ag_anom[50+i, 20:61, 128:214]

    nombre_titulo = "Dispersiòn de K y Ke - Dia " + dia[i] 
    nombre_archivo = "Disp_Ke_EB1P1_dia" + dia[i]
    
    mapa5(cmin,cmax,ncont,lat3,lon3,L,VAR1,VAR2,U,V,cmap,nombre_titulo,nombre_archivo)
    
    
# c barotropica
    
cmin = -1
cmax = 1
cmap = 'Spectral_r'
dia = ("1", "2", "3", "4")

for i in np.arange(0,4,1):
    VAR1 = C_barotropica[50+i, 20:67, 128:214]
    VAR2 = Ec_e[50+i, 20:67, 128:214]/10000

    nombre_titulo = "Conversiòn barotropica y Ke - Dia " + dia[i] 
    nombre_archivo = "C_barot_Ke_EB1P1_dia" + dia[i]
    
    mapa4(cmin,cmax,ncont,lat2,lon2,L,VAR1,VAR2,cmap,nombre_titulo,nombre_archivo)
    
