#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 19:19:32 2019

@author: Luciano
"""
import numpy as np
import time


def Estado_basico(psi, lat, lon):

    # correccion a estado basico
    # promedio zonal del estados basico en tiempo 50 (49)
    from numpy import empty
    psi_prom = empty([128])
    for i in range(0,127):
        psi_prom[i] = np.mean(psi[49,i,:])
        
    
    #promedio temporal del perturbado 50-59
    
    i=0
    psi_pert_temp = np.empty_like(psi[1,:,:])
    for i in np.arange(0,np.size(lat)):
        for j in np.arange(0,np.size(lon)):
            psi_pert_temp[i,j] = np.mean(psi[50:59,i,j])
            
    # promedio zonal de lo anterior
    i = 0        
    psi_pert_prom = empty([128])
    for i in np.arange(0,np.size(lat)):
        psi_pert_prom[i] = np.mean(psi_pert_temp[i,:]) 
    
    psi_c = np.empty_like(psi[1,:,:])
    for i in np.arange(0,np.size(lat)):   
        for j in  np.arange(0,np.size(lon)):
            psi_c[i,j] = psi[49,i,j]-psi_prom[i]+psi_pert_prom[i]
   
    return psi_c     