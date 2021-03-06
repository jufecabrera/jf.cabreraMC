import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import expon
from scipy.stats import norm
#exponcial
lista = np.random.exponential(0.1,1000)
loc,scale=expon.fit(lista)
print "scale(exp): %s" % (scale)
x = np.linspace(0,2,100)
y = expon.pdf(x,loc,scale)
plt.plot(x,y)
plt.hist(lista, normed=True, bins=20)
plt.show()
#TLC(normal)
sumas = []
for i in range(1,1000):
	s = np.sum(np.random.exponential(0.1,1000))
	sumas.append(s)
mu,v=norm.fit(sumas)
print "media: %f, varianza: %f" % (mu,v)
xn = np.linspace(80,120,100)
yn = norm.pdf(xn,mu,v)
plt.plot(xn,yn)
plt.hist(sumas, normed=True, bins=20)
plt.show()
