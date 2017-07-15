import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
dat = pd.read_csv('DatosBancoMundial5.csv', ',')
var = dat['Series Name'].values
dat = dat.drop(['Time','Time Code','Series Name','Series Code'], axis=1).values
dat = dat.T
nvar=len(var)
ndat=np.linspace(1,len(dat[:,0]),len(dat[:,0]))
#normalizacion
for i in range(nvar):
	dat[:,i]=(dat[:,i]-np.mean(dat[:,i]))/np.std(dat[:,i])
#exploracion
fig = plt.figure(figsize=(10,5))
ax1=fig.add_subplot(151)
ax1.barh(ndat,dat[:,0],height=1)	
ax1.set_ylabel('Pais Numero')
ax1.set_title('Tax Rate')
ax2=fig.add_subplot(152)
ax2.barh(ndat,dat[:,1],height=1)
ax2.set_title('Cost of Business start-up')
ax3=fig.add_subplot(153)
ax3.barh(ndat,dat[:,2],height=1)
ax3.set_title('Unemplyment (F)')
ax4=fig.add_subplot(154)
ax4.barh(ndat,dat[:,3],height=1)
ax4.set_title('Unemployment (M)')
ax5=fig.add_subplot(155)
ax5.barh(ndat,dat[:,4],height=1)
ax5.set_title('(F) to (M) LFP rate')
plt.tight_layout()
plt.savefig('ExploracionDatos.pdf')
plt.close()
#matriz de covarinza
def pm(x):
	return np.sum(x)/(len(x)-1)
def cov(array):
	leng = len(array[0])
	matrix = np.ones((leng,leng))
	for i in range(leng):
		for j in range(leng):
			dat1 = array[:,i]
			dat2 = array[:,j]
			exp = pm((dat1-np.mean(dat1))*(dat2-np.mean(dat2)))
			matrix[i,j]= exp
	return matrix
covar=cov(dat)
#componentes principales
values, vectors = np.linalg.eig(covar)
pc1=vectors[:,0]
pc2=vectors[:,1]
print "el componente principal es:\n",pc1
print "el segundo componente principal es:\n",pc2
#nuevo sistema
PC=[pc1,pc2]
new_dat=np.dot(PC,dat.T)
plt.scatter(new_dat[0,:], new_dat[1,:])
plt.title('Datos en terminos de PC1 y PC2')
plt.xlabel('PC1')
plt.ylabel('PC2')
plt.savefig('PCAdatos.pdf')
plt.close()
#agrupacion
#(parte del codigo a cuntinuacion se obtuvo de https://matplotlib.org/users/legend_guide.html para lograr poner la legend afuera de la grafica)
fig1=plt.figure(figsize=(7,5))
ax = fig1.add_subplot(111)
for i in range(nvar):
	ax.scatter(pc1[i],pc2[i],label=var[i])
ax.set_title('Agrupacion de variables')
ax.set_xlabel('PC1')
ax.set_ylabel('PC2')
box = ax.get_position()
ax.set_position([box.x0,box.y0+box.height*0.25,box.width,box.height*0.75])
ax.legend(loc='upper center', bbox_to_anchor=(0.5,-0.12))
plt.savefig('PCAvariables.pdf')
plt.close()
print "las variables que estan correlacionadas son\n",var[0]+"\n","con\n",var[1]+"\n","y\n",var[2]+"\n","con\n",var[3]


