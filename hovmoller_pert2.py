#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 19:05:41 2019

@author: auri
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 21:01:02 2019

@author: auri
"""
import matplotlib.pyplot as plt 
import numpy as np
from numpy import empty

def hovmoller2(psi_c, psi, lon, lat, estado_basico, perturbacion,nombre):
    anomalia_10dias = empty([10,128,256]) 
    for i in np.arange(0,10):
        anomalia_10dias[i,:,:]= psi[50+i,:,:] - psi_c
    
    dias = np.arange(1,11)
    
    plt.figure()
    plt.contourf(lon[0:360],dias, anomalia_10dias[:,31,0:360]/100000, cmap = 'viridis') 
    cb = plt.colorbar()
    cb.set_label('$x10^{5}$', labelpad = -38, y=1.1, rotation=0,fontsize=11)
    plt.contour(lon[0:360],dias, anomalia_10dias[:,31,0:360]/100000, levels = 0, colors = "w" )
    plt.axvline(220, color = "r")
    plt.xlabel('longitud')
    plt.ylabel('Dias')
    plt.tight_layout()
    plt.title("Hovmoller zonal $\Psi$ EB " + estado_basico + " P " + perturbacion) 
    plt.axvline(x = 220,ymin = 0, ymax = 10 , color = "r")
    plt.savefig("Hovmoller_zonal_" + nombre, dpi = 200)
    
    plt.figure()
    plt.contourf(lat[0:110], dias, anomalia_10dias[:,0:110,157]/100000, cmap = 'viridis') 
    cb = plt.colorbar()
    cb.set_label('$x10^{5}$', labelpad = -38, y=1.1, rotation=0,fontsize=11)
    plt.contour(lat[0:110], dias, anomalia_10dias[:,0:110,157]/100000, levels = 0, colors = "w" )
    plt.axvline(-46, color = "r")
    plt.xlabel('Latitud')
    plt.ylabel('Dias')
    plt.tight_layout()
    plt.title("Hovmoller meridional $\Psi$ EB " + estado_basico + " P " + perturbacion) 
    plt.savefig("Hovmoller_meridonal_" + nombre, dpi = 200)
