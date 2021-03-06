import numpy as np
import matplotlib.pyplot as plt
def f(x):
	return abs(np.sqrt(1-x**2))
A = 0.
B = 1.
N = 99999999
w = (B-A)/float(N-1)
x = np.linspace(A,B,N)
#simpson
odd = np.sum(f(x[1:N-2:2]))
even = np.sum(f(x[2:N-2:2]))
hs = f(x[0])/3. + f(x[N-1])/3. + odd*(4/3.)+ even*(2/3.)
#trap
h = -f(x[0])/2- f(x[N-1])/2+ np.sum(f(x))
print "trapezoide: %f" % (4*h*w)
print "simpson: %f" % (4*hs*w)
#montecarlo
def DOrigen(x,y):
	return np.sqrt(x**2+y**2)
c = 0
n = 9999999
#for i in range(n):	
#	x = np.random.random()
#	y = np.random.random()
#	if (DOrigen(x,y)<= 1):
#		c+=1
#pim=c/float(n)*4
#print "montecarlo: ", pim
xr = np.random.rand(n)
yr = np.random.rand(n)
dt = f(xr)-yr
inside = np.where(dt>0.0)
inte = 4*np.size(inside)/float(n)
print inte		
