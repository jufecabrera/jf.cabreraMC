import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile
import copy
Dor, Do = scipy.io.wavfile.read('Do.wav')
Solr, Sol = scipy.io.wavfile.read('Sol.wav')
dtDo = 1/float(Dor)
dtSol = 1/float(Solr)
NDo = len(Do)
NSol = len(Sol)
nDo =np.array(range(NDo))
nSol =np.array(range(NSol))
nDo2 =np.array(range(NDo/2)) #estas dos listas tienen la mitad de los datos para realizar un metodo mas corto
nSol2 =np.array(range(NSol/2))
#Transformada Do y Sol
def FTfunc(k,n,N,y):
	e = np.exp(-1j*2*np.pi*n*k/N)
	return np.sum(y*e)
FTDo=[]
FTSol=[]
for i in nDo2:
	FTDo.append(FTfunc(i,nDo,NDo,Do))
for i in nSol2:
	FTSol.append(FTfunc(i,nSol,NSol,Sol))
FTDo=np.array(FTDo)
frDo = np.linspace(0,NDo/2-1,NDo/2)/(dtDo*NDo)
FTSol=np.array(FTSol)
frSol = np.linspace(0,NSol/2-1,NSol/2)/(dtSol*NSol)
#Filtro del maximo pico
def filtrmax(x):
	c = copy.copy(x)
	xmax=np.where(x==(np.max(x)))[0]
	c[int(xmax)-70:int(xmax)+71]=0
	return c
FTDopico = filtrmax(FTDo)
#Filtro pasa bajos
def filtrLP(x,f):
	c = np.ones(len(f))
	c[np.where(abs(f)>1000)]=0
	return c*x
FTDoLP = filtrLP(FTDo,frDo)
#Graficas de filtros de Do
fig=plt.figure()
ax1=fig.add_subplot(311)
ax1.plot(frDo,abs(FTDo))
ax1.set_xlabel('Frecuencia (Hz)')
ax1.set_ylabel('$|FT|$')
ax1.set_title('Original')
ax2=fig.add_subplot(312)
ax2.plot(frDo,abs(FTDopico))
ax2.set_xlabel('Frecuencia (Hz)')
ax2.set_ylabel('$|FT|$')
ax2.set_title('Filtro Pico')
ax3=fig.add_subplot(313)
ax3.plot(frDo,abs(FTDoLP))
ax3.set_xlabel('Frecuencia (Hz)')
ax3.set_ylabel('$|FT|$')
ax3.set_title('Filtro Pasa Bajos')
plt.tight_layout()
plt.savefig('DoFiltros.pdf')
plt.close()
#Do>Sol
#el calculo del nuevo dtDoSol se hace siguiendo la documentacion de fftfreq en https://docs.scipy.org/doc/numpy/reference/generated/numpy.fft.fftfreq.html
posmax=np.where(frDo==260)[0]
dtDoSol=posmax/float(NDo*391)
DoSolr=int(1/float(dtDoSol))
frDoSol = np.linspace(0,NDo/2-1,NDo/2)/(dtDoSol*NDo)
plt.plot(frDoSol,abs(FTDo),label='Do > Sol')
plt.plot(frSol,abs(FTSol),label='Sol')
plt.title('Transformadas del Sol y Do alterada')
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('$|FT|$')
plt.legend()
plt.tight_layout()
plt.savefig('DoSol.pdf')
plt.close()
#inversas
def FTif(k,n,N,FT):
	e = np.exp(1j*2*np.pi*n*k/(N/2))
	return np.sum(FT*e)/(N/2)
Dopico = []
DoLP = []
for i in nDo2:
	Dopico.append(FTif(i,nDo2,NDo,FTDopico))
	DoLP.append(FTif(i,nDo2,NDo,FTDoLP))
Dopico = np.array(Dopico)
DoLP = np.array(DoLP)
#archivos wav
scipy.io.wavfile.write("Do_pico.wav",Dor/2,Dopico.astype(Do.dtype))
scipy.io.wavfile.write("Do_pasabajos.wav",Dor/2,DoLP.astype(Do.dtype))
scipy.io.wavfile.write("DoSol.wav",DoSolr,Do)

