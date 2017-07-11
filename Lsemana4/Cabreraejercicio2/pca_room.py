import numpy as np
import matplotlib.pyplot as plt
datos = np.loadtxt('room-temperature.csv', skiprows=1, usecols=[1,2,3,4], delimiter=',') 
#graficas de temperatura
fig = plt.figure()
ax1 = fig.add_subplot(221)
ax1.plot(datos[:,0])
ax1.set_xlabel('tiempo')
ax1.set_ylabel('Temperatura')
ax1.set_title('front left')
ax2 = fig.add_subplot(222)
ax2.plot(datos[:,1])
ax2.set_xlabel('tiempo')
ax2.set_ylabel('Temperatura')
ax2.set_title('front right')
ax3 = fig.add_subplot(223)
ax3.plot(datos[:,2])
ax3.set_xlabel('tiempo')
ax3.set_ylabel('Temperatura')
ax3.set_title('back left')
ax4 = fig.add_subplot(224)
ax4.plot(datos[:,3])
ax4.set_xlabel('tiempo')
ax4.set_ylabel('Temperatura')
ax4.set_title('back right')
plt.tight_layout()
plt.savefig('temp.png')
plt.close()
#centrado y normalizado
datos[:,0]=(datos[:,0]-np.mean(datos[:,0]))/np.std(datos[:,0])
datos[:,1]=(datos[:,1]-np.mean(datos[:,1]))/np.std(datos[:,1])
datos[:,2]=(datos[:,2]-np.mean(datos[:,2]))/np.std(datos[:,2])
datos[:,3]=(datos[:,3]-np.mean(datos[:,3]))/np.std(datos[:,3])
#matriz de covarianza
cov= np.cov(datos.T)
print cov
#vectores y valores propios
values, vectors = np.linalg.eig(cov)
print 'La primera componente principal es', vectors[:,0], 'con valor', values[0]
print 'La segunda componente principal es',vectors[:,1], 'con valor',values[1]
#contribucion de varianza
cont1 = values[0]/np.sum(values)*100
cont2 = values[1]/np.sum(values)*100
print 'La primera componente principal explica el',cont1, '% de la varianza'
print 'La segunda componente principal explica el',cont2, '% de la varianza'
#Graficas
#FR FL
pc1FR=[7*vectors[1,0],-7*vectors[1,0]]
pc1FL=[7*vectors[0,0],-7*vectors[0,0]]
pc2FR=[7*vectors[1,1],-7*vectors[1,1]]
pc2FL=[7*vectors[0,1],-7*vectors[0,1]]
plt.scatter(datos[:,1],datos[:,0])
plt.title('Front Right vs Front Left')
plt.xlabel('Front Right')
plt.ylabel('Front Left')
plt.plot(pc1FR,pc1FL, label='PC1')
plt.plot(pc2FR,pc2FL, label='PC2')
plt.legend()
plt.savefig('pca_fr_fl.pdf')
plt.close()
#BL FL
pc1BL=[5*vectors[2,0],-5*vectors[2,0]]
pc1FL=[5*vectors[0,0],-5*vectors[0,0]]
pc2BL=[5*vectors[2,1],-5*vectors[2,1]]
pc2FL=[5*vectors[0,1],-5*vectors[0,1]]
plt.scatter(datos[:,2],datos[:,0])
plt.title('Back Left vs Front Left')
plt.xlabel('Back Left')
plt.ylabel('Front Left')
plt.plot(pc1BL,pc1FL, label='PC1')
plt.plot(pc2BL,pc2FL, label='PC2')
plt.legend()
plt.savefig('pca_bl_fl.pdf')
plt.close()
