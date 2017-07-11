import numpy as np
import matplotlib.pyplot as plt
datos = np.loadtxt('food-texture.csv', skiprows=1, usecols=[1,2,3,4,5], delimiter=',') 
datos[:,0]=(datos[:,0]-np.mean(datos[:,0]))/np.std(datos[:,0])
datos[:,1]=(datos[:,1]-np.mean(datos[:,1]))/np.std(datos[:,1])
datos[:,2]=(datos[:,2]-np.mean(datos[:,2]))/np.std(datos[:,2])
datos[:,3]=(datos[:,3]-np.mean(datos[:,3]))/np.std(datos[:,3])
datos[:,4]=(datos[:,4]-np.mean(datos[:,4]))/np.std(datos[:,4])
fig,textures=plt.subplots(5,1)
textures[0].hist(datos[:,0])
textures[1].hist(datos[:,1])
textures[2].hist(datos[:,2])
textures[3].hist(datos[:,3])
textures[4].hist(datos[:,4])
plt.tight_layout()
#plt.show()
plt.close()
cov= np.cov(datos.T)
values, vectors = np.linalg.eig(cov)
print "values", values
print "vectors\n", vectors
#oil den
pc1oil=[10*vectors[0,0],-10*vectors[0,0]]
pc1den=[10*vectors[1,0],-10*vectors[1,0]]
pc2oil=[10*vectors[0,1],-10*vectors[0,1]]
pc2den=[10*vectors[1,1],-10*vectors[1,1]]
plt.scatter(datos[:,0],datos[:,1])
plt.plot(pc1oil,pc1den)
plt.plot(pc2oil,pc2den)
plt.xlabel('oil')
plt.ylabel('density')
plt.show()
plt.close()
#cri har
pc1cri=[10*vectors[2,0],-10*vectors[2,0]]
pc1har=[10*vectors[4,0],-10*vectors[4,0]]
pc2cri=[10*vectors[2,1],-10*vectors[2,1]]
pc2har=[10*vectors[4,1],-10*vectors[4,1]]
plt.scatter(datos[:,2],datos[:,4])
plt.plot(pc1cri,pc1har)
plt.plot(pc2cri,pc2har)
plt.xlabel('crispy')
plt.ylabel('hardness')
plt.show()
plt.close()
