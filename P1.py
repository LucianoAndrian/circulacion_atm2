import numpy as np
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math
import time 
import os
# os.chdir('/Users/mini/Documents/Circulación/Atmósfera')
os.chdir('/home/auri/Facultad/Materias/Circulacion/TP4/')
import xarray as xr
from netCDF4 import Dataset 
import cartopy.feature
from cartopy.mpl.ticker import LongitudeFormatter, LatitudeFormatter
import cartopy.crs as ccrs
from mapa import mapa
from DerY import derivy 
#%%
# dir = '/Users/mini/Documents/Circulación/Atmósfera/Experimento1/shallow.nc' # Mili

dir = '/home/auri/Facultad/Materias/Circulacion/TP4/Experimento1/shallow.nc' # Luchi
dS = xr.open_dataset(dir, decode_times=False) #Abro el NetCdf
print(dS)       # visualizo la info del .nc

# Las variables están dimensionalizadas
forzante = dS['fr'].values
u=dS['ucomp'].values
v=dS['vcomp'].values
forzante = dS['fr'].values
vort=dS['vor'].values


lat=dS['lat'].values
lon=dS['lon'].values

#%% Grafico la velocidad zonal en el último paso temporal (el 50)

VAR = u[49,:,:]
cmin = 0
cmax = 15
ncont = 11
clevs = np.linspace(cmin, cmax, ncont)
LONMIN = 0
LONMAX = 359
LATMIN = -88
LATMAX = 88
L = [LONMIN, LONMAX, LATMIN, LATMAX]
cmap = 'YlOrRd'
nombre_titulo = 'Componente Zonal del viento Simulacion 1'
nombre_archivo = 'u_tiempo_50_EB1'


fig = mapa(cmin,cmax,ncont,lat,lon,L,VAR,cmap,nombre_titulo,nombre_archivo)

#%%
#Grafico forzante en el "estado estacionario"

VAR = forzante[49,:,:]
cmin = 40000
cmax = 60000 # un poco por arriba del maximo real para que el maximo del EB2 no quede tan bajo
ncont = 11
clevs = np.linspace(cmin, cmax, ncont)
LONMIN = 0
LONMAX = 359
LATMIN = -88
LATMAX = 88
L = [LONMIN, LONMAX, LATMIN, LATMAX]
cmap = 'YlOrRd'
nombre_titulo = 'Forzante simulacion 1'
nombre_archivo = 'forzante_tiempo_50_EA1'


fig = mapa(cmin,cmax,ncont,lat,lon,L,VAR,cmap,nombre_titulo,nombre_archivo)

#%% Graficar el gradiente meridional de vorticidad absoluta

# gradiente vorticidad planetaria
R = 6370000
omega = 7.27*10**-5

# gradiente de vorticidad relativa

# longitud de arco en radianes es R*angulo--> 6370000*pi
# para tener el dy--> longitud de arco/128 (puntos de grilla)

lat_g = lat*np.pi/180 # regla de tres para pasar de grados a radianes.
beta = omega*np.cos(lat_g)/R
long_arco = R*lat_g

dy = R*np.pi/128

vort_y = derivy(vort[49,:,:], dy)

# haciendo lo mismo que antes pero de forma matricial simplifica los proximos pasos

lon_m, lat_m = np.meshgrid(lon, lat) 
lat_g_m = lat_m*np.pi/180 # regla de tres para pasar de grados a radianes.
beta_m = omega*np.cos(lat_g_m)/R
long_arco_m = R*lat_g

vort_abs = vort_y + beta_m

# gradiente de vorticidad relativa #ESTO CREO Q NO VA AL INFORME
#VAR= vort_y 
#cmin = np.round(np.min(vort_y), 14) # redondea con 15 digitos..ya que es 10E-13
#cmax = np.round(np.max(vort_y), 14) # este con 13 porque es 10E-11
#ncont = 11
#clevs = np.linspace(cmin, cmax, ncont)
#LONMIN = 0
#LONMAX = 359
#LATMIN = -88
#LATMAX = 88
#L = [LONMIN, LONMAX, LATMIN, LATMAX]
#cmap = 'bwr'
#nombre_titulo = 'Gradiente meridional de vorticidad relativa simulacion 1'
#nombre_archivo = 'vorticidad_gradiente_relativa_EC1'


#fig = mapa(cmin,cmax,ncont,lat,lon,L,VAR,cmap,nombre_titulo,nombre_archivo)

# gradiente de vort planetaria  # ESTO TAMPOCO
#VAR= beta_m
#cmin = np.round(np.min(beta_m), 15) # redondea con 15 digitos..ya que es 10E-13
#cmax = np.round(np.max(beta_m), 12) # este con 13 porque es 10E-11
#ncont = 11
#clevs = np.linspace(cmin, cmax, ncont)
#LONMIN = 0
#LONMAX = 359
#LATMIN = -88
#LATMAX = 88
#L = [LONMIN, LONMAX, LATMIN, LATMAX]
#cmap = 'YlOrRd'
#nombre_titulo = 'Gradiente meridional de vorticidad planetaria simulacion 1'
#nombre_archivo = 'vorticidad_gradiente_planetaria_EC1'


#fig = mapa(cmin,cmax,ncont,lat,lon,L,VAR,cmap,nombre_titulo,nombre_archivo)


VAR= vort_abs #es la vorticidad relativa
cmin = 0#np.round(np.min(vort_abs), 15) # redondea con 15 digitos..ya que es 10E-13
cmax = 1.5e-11#np.round(np.max(vort_abs), 13) # este con 13 porque es 10E-11
ncont = 11
clevs = np.linspace(cmin, cmax, ncont)
LONMIN = 0
LONMAX = 359
LATMIN = -88
LATMAX = 88
L = [LONMIN, LONMAX, LATMIN, LATMAX]
cmap = 'YlOrRd'
nombre_titulo = 'Gradiente meridional de vorticidad absoluta simulacion 1'
nombre_archivo = 'vorticidad_gradiente_EC1'

fig = mapa(cmin,cmax,ncont,lat,lon,L,VAR,cmap,nombre_titulo,nombre_archivo)

#%% KS 
# necesitamos la derivada 2da de U respecto de y
uy = derivy(u[49,:,:],dy)
uyy = derivy(uy,dy)

ks = np.sqrt((beta_m-uyy)/u[49,:,:])

# por circulo de latitud. KS tiene los mismo valores para cada longitud, solo varia latitud
ks_c = R*np.cos(lat_g_m)*ks

VAR = ks_c #es la vorticidad relativa
cmin = np.round(np.min(ks_c)) # redondea con 15 digitos..ya que es 10E-13
cmax = 20#np.round(np.max(ks_c)) # este con 13 porque es 10E-11
ncont = 11
clevs = np.linspace(cmin, cmax, ncont)
LONMIN= 0
LONMAX= 359
LATMIN= -88
LATMAX= 88
L = [LONMIN, LONMAX, LATMIN, LATMAX]
cmap = 'YlOrRd'
nombre_titulo = 'KS por circulo de latitud Simulacion 1'
nombre_archivo = 'KS_ED1'


fig = mapa(cmin,cmax,ncont,lat,lon,L,VAR,cmap,nombre_titulo,nombre_archivo)



#%%  SIMULACION 2
# dir = '/Users/mini/Documents/Circulación/Atmósfera/Simulacion2/shallow.nc' # Mili
dir = '/home/auri/Facultad/Materias/Circulacion/TP4/Simulacion2/shallow.nc' # Luchi
dS = xr.open_dataset(dir, decode_times=False) #Abro el NetCdf
print(dS)       # visualizo la info del .nc

# Las variables están dimensionalizadas
forzante = dS['fr'].values
u=dS['ucomp'].values
v=dS['vcomp'].values
forzante = dS['fr'].values
vort=dS['vor'].values


lat=dS['lat'].values
lon=dS['lon'].values



#%% Grafico la velocidad zonal en el último paso temporal (el 50)

VAR = u[49,:,:]
cmin = -15
cmax = 15
ncont = 11
clevs = np.linspace(cmin, cmax, ncont)
LONMIN = 0
LONMAX = 359
LATMIN = -88
LATMAX = 88
L = [LONMIN, LONMAX, LATMIN, LATMAX]
cmap = 'RdYlBu_r'
nombre_titulo = 'Componente Zonal del viento Simulacion 2'
nombre_archivo = 'u_tiempo_50_EB2'


fig = mapa(cmin,cmax,ncont,lat,lon,L,VAR,cmap,nombre_titulo,nombre_archivo)

#%%
#Grafico forzante en el "estado estacionario"

VAR=forzante[49,:,:]
cmin = np.round(np.min(forzante[49,:,:]))
cmax = 60000#np.round(np.max(forzante[49,:,:])) # para q este a la misma escala que el EB1 y que se note la itcz
clevs = np.linspace(cmin, cmax, ncont)
LONMIN= 0
LONMAX= 359
LATMIN= -88
LATMAX= 88
L = [LONMIN, LONMAX, LATMIN, LATMAX]
cmap = 'YlOrRd'
nombre_titulo = 'Forzante simulacion 2'
nombre_archivo = 'forzante_tiempo_50_EA2'


fig = mapa(cmin,cmax,ncont,lat,lon,L,VAR,cmap,nombre_titulo,nombre_archivo)

#%% Graficar el gradiente meridional de vorticidad absoluta

# gradiente vorticidad planetaria
R = 6370000
omega = 7.27*10**-5

# gradiente de vorticidad relativa

# longitud de arco en radianes es R*angulo--> 6370000*pi
# para tener el dy--> longitud de arco/128 (puntos de grilla)

lat_g = lat*np.pi/180 # regla de tres para pasar de grados a radianes.
beta = omega*np.cos(lat_g)/R
long_arco = R*lat_g

dy = R*np.pi/128

vort_y = derivy(vort[49,:,:], dy)

# haciendo lo mismo que antes pero de forma matricial simplifica los proximos pasos

lon_m, lat_m = np.meshgrid(lon, lat) 
lat_g_m = lat_m*np.pi/180 # regla de tres para pasar de grados a radianes.
beta_m = omega*np.cos(lat_g_m)/R
long_arco_m = R*lat_g

vort_abs = vort_y + beta_m



# gradiente de vorticidad relativa
#VAR= vort_y 
#cmin = np.round(np.min(vort_y), 14) # redondea con 15 digitos..ya que es 10E-13
#cmax = np.round(np.max(vort_y), 14) # este con 13 porque es 10E-11
#ncont = 11
#clevs = np.linspace(cmin, cmax, ncont)
#LONMIN = 0
#LONMAX = 359
#LATMIN = -88
#LATMAX = 88
#L = [LONMIN, LONMAX, LATMIN, LATMAX]
#cmap = 'winter'
#nombre_titulo = 'Gradiente meridional de vorticidad relativa simulacion 2'
#nombre_archivo = 'vorticidad_gradiente_relativa_EC2'


#fig = mapa(cmin,cmax,ncont,lat,lon,L,VAR,cmap,nombre_titulo,nombre_archivo)

# gradiente de vort planetaria
#VAR= beta_m
#cmin = np.round(np.min(beta_m), 15) # redondea con 15 digitos..ya que es 10E-13
#cmax = np.round(np.max(beta_m), 12) # este con 13 porque es 10E-11
#ncont = 11
#clevs = np.linspace(cmin, cmax, ncont)
#LONMIN = 0
#LONMAX = 359
#LATMIN = -88
#LATMAX = 88
#L = [LONMIN, LONMAX, LATMIN, LATMAX]
#cmap = 'winter'
#nombre_titulo = 'Gradiente meridional de vorticidad planetaria simulacion 2'
#nombre_archivo = 'vorticidad_gradiente_planetaria_EC2'


#fig = mapa(cmin,cmax,ncont,lat,lon,L,VAR,cmap,nombre_titulo,nombre_archivo)


VAR= vort_abs 
cmin = -1.5e-11 # redondea con 14 digitos..ya que es 10E-12
cmax = 1.5e-11 # este con 13 porque es 10E-11
ncont = 11
clevs = np.linspace(cmin, cmax, ncont)
LONMIN = 0
LONMAX = 359
LATMIN = -88
LATMAX = 88
L = [LONMIN, LONMAX, LATMIN, LATMAX]
cmap = 'RdYlBu_r'
nombre_titulo = 'Gradiente meridional de vorticidad absoluta simulacion 2'
nombre_archivo = 'vorticidad_gradiente_EC2'


fig = mapa(cmin,cmax,ncont,lat,lon,L,VAR,cmap,nombre_titulo,nombre_archivo)

#%% KS 
# necesitamos la derivada 2da de U respecto de y
uy = derivy(u[49,:,:],dy)
uyy = derivy(uy,dy)

ks = np.sqrt((beta_m-uyy)/u[49,:,:])

# por circulo de latitud. KS tiene los mismo valores para cada longitud, solo varia latitud
ks_c = R*np.cos(lat_g_m)*ks

VAR = ks_c #es la vorticidad relativa
cmin = np.round(np.nanmin(ks_c))
cmax = 20 #np.round(np.nanmax(ks_c)) #maximo igual al EB1
ncont = 11
clevs = np.linspace(cmin, cmax, ncont)
LONMIN= 0
LONMAX= 359
LATMIN= -88
LATMAX= 88
L = [LONMIN, LONMAX, LATMIN, LATMAX]
cmap = 'YlOrRd'
nombre_titulo = 'KS por circulo de latitud Simulacion 2'
nombre_archivo = 'KS_ED2'


fig = mapa(cmin,cmax,ncont,lat,lon,L,VAR,cmap,nombre_titulo,nombre_archivo)

