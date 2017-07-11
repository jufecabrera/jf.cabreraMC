import numpy as np
import matplotlib.pyplot as plt 
from scipy.stats import norm
A = np.loadtxt('datos_CAMINATA.txt')
l,k = np.shape(A)
plt.hist(A[0],normed=True)
plt.title('histograma primera fila')
plt.savefig('binomial.png')
plt.close()
pasosPorFila = []
for i in range(0,l):
	pasosPorFila.append(np.sum(A[i])) 
mu,v=norm.fit(pasosPorFila)
xn = np.linspace(3300,3700,2000)
yn = norm.pdf(xn,mu,v)
plt.plot(xn,yn)
plt.hist(pasosPorFila,normed=True)
plt.title('histograma y fit pasos totales por fila')
plt.savefig('normal.png')
plt.close()
mub=mu/float(k)
p = mub/10.
print "mu_normal = %f \nmu_normal dividido 1000 es mu_binomial = %f" % (mu,mub)
print "Conociendo que la probabilidad es mu_b sobre N (siendo N = 10)"
print "La probabilidad de sacar una cara con esta moneda es :%f" % (p)
