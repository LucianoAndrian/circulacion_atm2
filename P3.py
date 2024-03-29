#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 16:49:18 2019
as
@author:   auri
"""
import numpy as np
import matplotlib.pyplot as plt
import os

import xarray as xr
from netCDF4 import Dataset 
import cartopy.feature
from cartopy.mpl.ticker import LongitudeFormatter, LatitudeFormatter
import cartopy.crs as ccrs

from DerY import derivy 
from DerX import derivx     
from numpy import empty

# nuestras funciones
from Estado_basico import Estado_basico
from mapa import mapa
from mapa2 import mapa2
from mapa3 import mapa3 ## con cambios
from mapa4 import mapa4 
from mapa5 import mapa5 


dir = '/home/auri/Facultad/Materias/Circulacion/TP6/' # Luchi
script_dir = os.path.dirname(dir)

#os.chdir('/Users/mini/Documents/Circulación/Atmósfera/P3/')  #Esto es para que se quede en el directorio que querés
#dir = '/Users/mini/Documents/Circulación/Atmósfera/P3/' # Mili

#%%
    #############
    ### EB1P1 ###
    #############
    
dS = xr.open_dataset(dir+'EB1P1_concatenado.nc', decode_times=False) 
print(dS)

lat=dS['lat'].values
lon=dS['lon'].values
u = dS["ucomp"].values
v = dS["vcomp"].values
h = dS["h"].values

H = 40000 # h0 del name list
g = 9.8 # gravedad
rho = 1 # densidad del aire

eta = (h - H)/9.8  #superficie libre 

# Calculamos el estado basico de las velocidades y la superficie libre

u_b = Estado_basico(u, lat, lon)
v_b = Estado_basico(v, lat, lon)
eta_b = Estado_basico(eta, lat, lon)

# Calculamos las perturbaciones

u_e = u - u_b           
v_e = v - v_b           
eta_e = eta - eta_b   

#%%
# Energia cinetica

Ec = (rho*H/g)/2*(u**2 + v**2)
Ec_b = (rho*H/g)/2*(u_b**2 + v_b**2)
Ec_e = (rho*H/g)/2*(u_e**2 + v_e**2)


# Energia potencial

Ep = (rho*g)/2*(eta**2+(H/g)**2) # Energia potencial instantanea
Ep_b = (rho*g)/2*(eta_b**2+(H/g)**2) # Energia potencial del flujo medio
Ep_e = (rho*g)/2*(eta_e**2) # Energia potencial de las perturbaciones


# Graficos Ec y Ep del flujo medio
# Defino parámetros para poder graficar

LONMIN= 0
LONMAX= 359
LATMIN= -88
LATMAX= 88
L = [LONMIN, LONMAX, LATMIN, LATMAX]
cmap = 'YlOrRd'  # cambiando los colores para estos mapas

VAR1 = Ec_b/1e4   # dividir por 1e4 en todas las energia. asi quedan bien las escalas de la funcion mapa3
VAR2 = Ep_b/1e4
VAR3 = eta_e[51,:,:] #anomalia de la sfc libre dia 2 de la perturbaciòn

cmin1 = 0   #Límites de la E cinética
cmax1 = 24
ncont = 25

cmax2 = 8250 #Límites de E potencial 
cmin2 = 8180   

nombre_titulo1 = "Energía Cinética - Estado básico 1"
nombre_titulo2 = "Energía Potencial - Estado básico 1"
nombre_archivo= "Ec_Ep_EB1P1"

fig= mapa3(cmin1,cmax1,cmin2,cmax2,ncont,lat,lon,L,VAR1,VAR2,VAR3,cmap,nombre_titulo1,nombre_titulo2,nombre_archivo)


# Graficos Ec y Ep de las perturbaciones dia 2 de la perturbaciòn

VAR1 = Ec_e[51,:,:]/1e4
VAR2 = Ep_e[51,:,:]/1e4
VAR3 = eta_e[51,:,:]

 
cmin1 = 0
cmax1 = 3.5
ncont = 25

cmin2 = 0
cmax2 = 0.25

nombre_titulo1 = "Anomalía Energìa Cinética - Estado básico 1"
nombre_titulo2 = "Anomalía Energìa Potencial - Estado básico 1"
nombre_archivo = "Ec_Ep_EB1P1_E"
fig= mapa3(cmin1,cmax1,cmin2,cmax2,ncont,lat,lon,L,VAR1,VAR2,VAR3,cmap,nombre_titulo1,nombre_titulo2,nombre_archivo)
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

C_barotropica = -rho*H/g*(u_e**2*u_b_x + u_e*v_e*u_b_y + u_e*v_e*v_b_x + v_e**2*v_b_y)


# conversion baroclinica

Vu_ex = derivx(u_e, dx, lat)
Vv_ey = derivy(v_e, dy)
div = Vu_ex + Vv_ey

C_baroclinica = H*eta_e*div


# dispersion de Ec (POR LAS DUDAS REVISAR!!!)

V_eta_u_ey = derivy(eta_e*v_e,dy)
V_eta_v_ex = derivx(eta_e*u_e, dx, lat)

Disp = -H*(V_eta_u_ey + V_eta_v_ex)

# flujo ajestrofico

omega = 7.27e-5
lon_m, lat_m = np.meshgrid(lon, lat) 
lat_g_m = lat_m*np.pi/180 # regla de tres para pasar de grados a radianes.


# viento ageostrofico

Ug = -1/(2*omega*np.sin(lat_g_m))*derivy(h, dy)
Vg = 1/(2*omega*np.sin(lat_g_m))*derivx(h, dx, lat)

Ug_b = Estado_basico(Ug, lat, lon)
Vg_b = Estado_basico(Vg, lat, lon)

Ug_e = Ug - Ug_b
Vg_e = Vg - Vg_b

Uag = u_e - Ug_e
Vag = v_e - Vg_e



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

cmin = -5
cmax = 5
cmap = 'Spectral_r'
dia = ("1", "2", "3", "4")

p=86400/1e4 # para que sea por dia y que la escala quede razonable

for i in np.arange(0,4,1):
    VAR1 = Adv[50+i, 20:67, 128:214]*p
    VAR2 = Ec_e[50+i, 20:67, 128:214]/10000 

    nombre_titulo = "Advección de Ke y Ke - Dia " + dia[i] + " Estado básico 1"
    nombre_archivo = "Adv_Ke_EB1P1_dia" + dia[i]
    
    mapa4(cmin,cmax,ncont,lat2,lon2,L,VAR1,VAR2,cmap,nombre_titulo,nombre_archivo)


# c baroclinica

cmap = 'Spectral_r'
dia = ("1", "2", "3", "4")

for i in np.arange(0,4,1):
    VAR1 = C_baroclinica[50+i, 20:67, 128:214]*p
    VAR2 = Ec_e[50+i, 20:67, 128:214]/10000

    nombre_titulo = "Conversión baroclínica y Ke - Dia " + dia[i] + " Estado básico 1"
    nombre_archivo = "C_baroc_Ke_EB1P1_dia" + dia[i]
    
    mapa4(cmin,cmax,ncont,lat2,lon2,L,VAR1,VAR2,cmap,nombre_titulo,nombre_archivo)
    
    
# Dispersion y flujo agesotrofico

lat3=lat[20:70]   # LATITUDES PARA QUE GRAFIQUE LOS VECTORES CERCA DEL ECUADOR
lon3=lon[128:214]
lat4=lat[20:56]

cmap = 'Spectral_r'
dia = ("1", "2", "3", "4")

for i in np.arange(0,4,1):
    VAR1 = Disp[50+i, 20:70, 128:214]*p
    VAR2 = Ec_e[50+i, 20:70, 128:214]/10000

    
    V = Vag[50+i, 20:56,128:214]*eta_e[50+i, 20:56,128:214]
    U = Uag[50+i, 20:56, 128:214]*eta_e[50+i, 20:56,128:214]

    nombre_titulo = "Dispersión de K y Ke - Dia " + dia[i] + " Estado básico 1"
    nombre_archivo = "Disp_Ke_EB1P1_dia" + dia[i]
    
    mapa5(cmin,cmax,ncont,lat3,lat4,lon3,L,VAR1,VAR2,U,V,cmap,nombre_titulo,nombre_archivo)
    
    
# c barotropica
    
cmap = 'Spectral_r'
dia = ("1", "2", "3", "4")

for i in np.arange(0,4,1):
    VAR1 = C_barotropica[50+i, 20:67, 128:214]*p
    VAR2 = Ec_e[50+i, 20:67, 128:214]/10000

    nombre_titulo = "Conversión barotrópica y Ke - Dia " + dia[i] + " Estado básico 1"
    nombre_archivo = "C_barot_Ke_EB1P1_dia" + dia[i]
    
    mapa4(cmin,cmax,ncont,lat2,lon2,L,VAR1,VAR2,cmap,nombre_titulo,nombre_archivo)
    
