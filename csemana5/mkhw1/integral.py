import numpy as np
import matplotlib.pyplot as plt
def f(x):
	return (np.sum(x, axis=1))**3
#valor maximo de la funcion siendo todas las variables igual a 2
fmax=8000
#rango para numero de puntos
rangoN=np.power(2,range(1,18))
#integral exacta
intAnalitica=1126400.
I=[]
#repeticiones
rep = 30
for N in rangoN:
	resultados = 0	
	for i in range(rep):
		x=2*np.random.rand(N,10)
		y=fmax*np.random.rand(N)
		delta = f(x)-y
		c = np.size(np.where(delta>0.))
		r=(c/float(N))*(2**10)*fmax
		resultados =resultados +r
	I.append(resultados/float(rep))
I=np.array(I)
plt.semilogx(rangoN,I)
plt.title("valor calculado vs numero de puntos")
plt.xlabel("numero de puntos")
plt.savefig('integral.pdf')
plt.close()
error = abs(I-intAnalitica)/intAnalitica
plt.loglog((1/np.sqrt(rangoN)),error)
plt.savefig('err.pdf')

