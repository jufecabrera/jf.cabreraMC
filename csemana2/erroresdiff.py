import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
def f(x):
	return np.sin(x)
def fprtr(x):
	return np.cos(x)
x = np.linspace(-5.,5.,1000)
#forward
def forward(h,x):
	return (f(x+h)-f(x))/h
#central
def central(h,x):
	return (f(x+(h/2.))-(f(x-(h/2.))))/h
#extrapol
def extrapol(h,x):
	return (4*central(h/2.,x)-central(h,x))/3
hd = np.logspace(-9,0,200)
ef = []
ec = []
eex = []
def intprom(f):
	x = np.linspace(-5.,5.,1000)
	odd = np.sum(f[1:-1:2])
	even = np.sum(f[2:-1:2])
	w = (5.-(-5.))/100
	return (f[0]/3. + f[-1]/3. + odd*(4/3.)+ even*(2/3.))*w/(5.-(-5.))
for i in hd:
	eff = abs(fprtr(x)-forward(i,x))
	ef.append(intprom(eff))
	ecc = abs(fprtr(x)-central(i,x))
	ec.append(intprom(ecc))
	eexx = abs(fprtr(x)-extrapol(i,x))
	eex.append(intprom(eexx))
plt.plot(hd,ef, label=("forward"))
plt.plot(hd,ec, label=("central"))
plt.plot(hd,eex, label=("extrapolated"))
plt.xscale('log')
plt.yscale('log')
plt.legend(loc='upper left')
plt.title('error promedio en el rango x de -5 a 5')
plt.xlabel('h')
plt.ylabel('error')
plt.show()
#3D
X,H = np.meshgrid(x,hd)
def error(x,h):
	return abs(fprtr(x)-central(h,x))
E = error(X,H)
fig = plt.figure()
ax = fig.gca(projection='3d')
surf = ax.plot_surface(X, np.log(H), np.log(E))
ax.set_xlabel('x')
ax.set_ylabel('h')
ax.set_zlabel('error')
ax.set_title('error en x y h (central)')
plt.show()
