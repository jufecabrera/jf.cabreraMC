import numpy as np
import matplotlib.pyplot as plt
datos = np.loadtxt('room-temperature.csv', skiprows=1, usecols=[1,2,3,4], delimiter=',') 
N=len(datos.T)
for i in range(N):
	datos[:,i] = (datos[:,i]-np.mean(datos[:,i]))/np.std(datos[:,i])
cov = np.cov(datos.T)
values, vectors = np.linalg.eig(cov)
print "PC1 es:", vectors[:,0] ,"y PC2 es", vectors[:,1] 
plt.scatter(vectors[0,0],vectors[0,1],label='T1')
plt.scatter(vectors[1,0],vectors[1,1],label='T2')
plt.scatter(vectors[2,0],vectors[2,1],label='T3')
plt.scatter(vectors[3,0],vectors[3,1],label='T4')
plt.legend()
plt.xlim(-0.6,0)
plt.title('Agrupacion de variables')
plt.xlabel('PC1')
plt.ylabel('PC2')
plt.savefig('Agrupacion.pdf')
