""" 
Funcion para derivar en la direccion y tomando en cuenta la esfericidad de la tierra

INPUTS
array: numpy array de dos/tres dimensiones (si es 3D, primer dimension deben ser los tiempos)
dy: paso espacial en direccion y

OUTPUTS
dUy: array de dos dimensiones con las derivadas

""" 

def derivy(array,dy):
    import numpy as np

    # Para array 3D
    if (array.ndim==3):
    	dUy=array*0
    	a=len(array[0,:,0])
    	b=len(array[0,0,:])
    	for time in range(0,np.size(array,0)):
        	i=0
        	while i<a:
            		j=0
            		while j<b:
                		if i==0:
                    			dUy[time,i,j]=(array[time,i+1,j]-array[time,i,j])/dy
                		elif i==a-1:
                    			dUy[time,i,j]=(array[time,i,j]-array[time,i-1,j])/dy
                		else:
                    			dUy[time,i,j]=(array[time,i+1,j]-array[time,i-1,j])/dy/2
                		j=j+1
            		i=i+1

    # Para array 2D
    if (array.ndim==2):
    	dUy=array*0
    	a=len(array[:,0])
    	b=len(array[0,:])
    	i=0
    	while i<a:
    		j=0
    		while j<b:
    			if i==0:
    				dUy[i,j]=(array[i+1,j]-array[i,j])/dy
    			elif i==a-1:
    				dUy[i,j]=(array[i,j]-array[i-1,j])/dy
    			else:
    				dUy[i,j]=(array[i+1,j]-array[i-1,j])/dy/2
    			j=j+1
    		i=i+1

    return dUy
                    

