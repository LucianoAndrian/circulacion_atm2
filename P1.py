import numpy as np
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math
import time 
import os
os.chdir('/Users/mini/Documents/Circulación/Atmósfera')
import xarray as xr
from netCDF4 import Dataset 
import cartopy.feature
from cartopy.mpl.ticker import LongitudeFormatter, LatitudeFormatter
import cartopy.crs as ccrs
from mapa import mapa
from DerY import derivy 
#%%
dir = '/Users/mini/Documents/Circulación/Atmósfera/Experimento1/shallow.nc'

dS = xr.open_dataset(dir, decode_times=False) #Abro el NetCdf
print(dS)       # visualizo la info del .nc

#Las variables están dimensionalizadas
forzante = dS['fr'].values
u=dS['ucomp'].values
v=dS['vcomp'].values
forzante = dS['fr'].values
vort=dS['vor'].values


lat=dS['lat'].values
lon=dS['lon'].values

beta=2*10**-11

#%% Grafico la velocidad zonal en el último paso temporal (el 50)

VAR=u[49,:,:]
cmin = 0
cmax = 10
ncont = 11
clevs = np.linspace(cmin, cmax, ncont)
LONMIN=0
LONMAX=359
LATMIN=-88
LATMAX=88
L = [LONMIN, LONMAX, LATMIN, LATMAX]
cmap = 'rainbow'
nombre_titulo = 'u'
nombre_archivo = 'u_tiempo_50_EB1'


fig = mapa(cmin,cmax,ncont,lat,lon,L,VAR,cmap,nombre_titulo,nombre_archivo)

#%%
#Grafico forzante en el "estado estacionario"

VAR=forzante[49,:,:]
cmin = 40000
cmax = 50000
ncont = 11
clevs = np.linspace(cmin, cmax, ncont)
LONMIN=0
LONMAX=359
LATMIN=-88
LATMAX=88
L = [LONMIN, LONMAX, LATMIN, LATMAX]
cmap = 'rainbow'
nombre_titulo = 'Forzante'
nombre_archivo = 'forzante_tiempo_50_EB1'


fig = mapa(cmin,cmax,ncont,lat,lon,L,VAR,cmap,nombre_titulo,nombre_archivo)

#%% Graficamos la vorticidad absoluta
R=6370000
omega=7.27*10**-5
beta=2*omega*np.cos(lat)/R
vort_abs=vort+beta

VAR=vort[49,:,:] #es la vorticidad relativa
cmin = -5*10**-6
cmax = 5*10**-6
ncont = 11
clevs = np.linspace(cmin, cmax, ncont)
LONMIN=0
LONMAX=359
LATMIN=-88
LATMAX=88
L = [LONMIN, LONMAX, LATMIN, LATMAX]
cmap = 'rainbow'
nombre_titulo = 'Vorticidad'
nombre_archivo = 'vorticidad_tiempo_50_EB1'


fig = mapa(cmin,cmax,ncont,lat,lon,L,VAR,cmap,nombre_titulo,nombre_archivo)
