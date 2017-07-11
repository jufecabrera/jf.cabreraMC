import numpy as np
import matplotlib.pyplot as plt
def f(x):
	return np.sin(x)
def fprtr(x):
	return np.cos(x)
x = np.linspace(-5.,5.,1000)
h = x[1]-x[0] 
#forward
fprime = (f(x+h)-f(x))/h
#central
fprimec = (f(x+(h/2.))-(f(x-(h/2.))))/h
#segunda
def fprIItr(x):
	return -np.sin(x)
fprimeII = (f(x+h)+f(x-h)-2*f(x))/h**2
#graficas
fig = plt.figure()
ax1 = fig.add_subplot(321)
ax1.plot(x,f(x))
ax1.plot(x,fprime)
ax1.set_title("forward")
ax2 = fig.add_subplot(322)
ax2.plot(x,abs(fprime-fprtr(x)))
ax2.set_title("error forward")
ax3 = fig.add_subplot(323)
ax3.plot(x,f(x))
ax3.plot(x,fprimec)
ax3.set_title("central")
ax4 = fig.add_subplot(324)
ax4.plot(x,abs(fprimec-fprtr(x)))
ax4.set_title("error central")
ax5 = fig.add_subplot(325)
ax5.plot(x,f(x))
ax5.plot(x,fprimeII)
ax5.set_title("segunda")
ax6 = fig.add_subplot(326)
ax6.plot(x,abs(fprimeII-fprIItr(x)))
ax6.set_title("error segunda")
plt.show()
