""" 
Funcion para derivar en la direccion x tomando en cuenta la esfericidad de la tierra

INPUTS
array: numpy array de dos/tres dimensiones (si es 3D, primer dimension deben ser los tiempos)
dx: paso espacial en direccion x

OUTPUTS
dUx: array de dos dimensiones con las derivadas

""" 

#%%

# Funcion derivada segun x tomando en cuenta la esfericidad de la tierra
def derivx(array,dx,lat):
    import numpy as np

    # Para array 3D
    if (array.ndim==3):
    	dUx=array*0
    	a=len(array[0,:,0])
    	b=len(array[0,0,:])
    	for time in range(0,np.size(array,0)):
        	i=0
        	while i<a:
            		j=0
            		while j<b:
                		if j==0:
                    			dUx[time,i,j]=(array[time,i,j+1]-array[time,i,j-1])/(dx*np.cos(lat[i]*np.pi/180))/2
                		elif j==b-1:
                    			dUx[time,i,j]=(array[time,i,j-j]-array[time,i,j-1])/(dx*np.cos(lat[i]*np.pi/180))/2
                		else:
                    			dUx[time,i,j]=(array[time,i,j+1]-array[time,i,j-1])/(dx*np.cos(lat[i]*np.pi/180))/2
                		j=j+1
            		i=i+1

    # Para array 2D
    if (array.ndim==2):
    	dUx=array*0
    	a=len(array[:,0])
    	b=len(array[0,:])
    	i=0
    	while i<a:
    		j=0
    		while j<b:
    			if j==0:
    				dUx[i,j]=(array[i,j+1]-array[i,j-1])/(dx*np.cos(lat[i]*np.pi/180))/2
    			elif j==b-1:
    				dUx[i,j]=(array[i,j-j]-array[i,j-1])/(dx*np.cos(lat[i]*np.pi/180))/2
    			else:
    				dUx[i,j]=(array[i,j+1]-array[i,j-1])/(dx*np.cos(lat[i]*np.pi/180))/2
    			j=j+1
    		i=i+1
    return dUx
