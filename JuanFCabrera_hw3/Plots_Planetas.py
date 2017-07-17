import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation
datos = np.loadtxt('planetas.csv', delimiter=',')
n_points=len(datos[:,0])
l=np.size(datos[0])
print l
t = datos[:,0]
for i in range(1,l):
	ii = i-1
	globals()['d%s' % ii] = datos[:,i]
plt.plot(t,d0)
plt.plot(t,d3)
plt.show()
 
