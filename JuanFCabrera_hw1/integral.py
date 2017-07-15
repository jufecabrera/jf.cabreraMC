import numpy as np
import matplotlib.pyplot as plt
def f(x):
	return (np.sum(x, axis=1))**3
#valor maximo de la funcion siendo todas las variables igual a 2
fmax=8000
#rango para numero de puntos, potencias de 2 hasta 2^19
rangoN=np.power(2,range(1,19))
#integral exacta
intAnalitica=1126400.
I=[]
#repeticiones
rep = 20
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
#grafica puntos vs integral
plt.figure(figsize=(8,5))
plt.semilogx(rangoN,I)
plt.title("Valor calculado vs numero de puntos")
plt.xlabel("Numero de puntos")
plt.ylabel("Valor de la integral")
plt.savefig('num_integral.pdf')
#grafica error
error = 100*abs(I-intAnalitica)/intAnalitica
plt.figure()
plt.semilogx((1/np.sqrt(rangoN)),error)
plt.title("Error de la integral calculada")
plt.xlabel("$1/\sqrt{N}$")
plt.ylabel("Error porcentual %")
plt.savefig('err_integral.pdf')

