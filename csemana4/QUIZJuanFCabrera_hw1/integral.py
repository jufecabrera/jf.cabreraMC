import numpy as np
def f(x):
	return np.sin(x)
repeticiones = 20
N = 10000
resultados = 0
for i in range(repeticiones):
	x = np.pi*np.random.rand(N)
	y = f(x)
	res = (np.sum(y)/float(N))*np.pi
	resultados += res
result= resultados/float(repeticiones)
print "el valor de la integral es %f" % (result)
