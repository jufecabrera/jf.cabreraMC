import numpy as np
# trapezio
A= float(input("inicial: "))
B= float(input("final: "))
N= int((B-A)*50)
if (N%2==0):
	N=N+1
else:
	pass
def f(x):
	y= np.exp(x)
	return y
x = np.linspace(A,B,N)
h = -f(x[0])/2- f(x[N-1])/2+ np.sum(f(x))
w = (B-A)/(N-1)
print "integral trapezio: %f" % (h*w)
# simpson
odd = np.sum(f(x[1:-1:2]))
even = np.sum(f(x[2:-1:2]))
hs = f(x[0])/3 + f(x[-1])/3 + odd*(4/3.)+ even*(2/3.)
print "integral simpson: %f" % (hs*w)
