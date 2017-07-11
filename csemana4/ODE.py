import numpy as np
import matplotlib.pyplot as plt
h=0.01
min_x = 0.0
max_x = 4.0
n_points = int((max_x - min_x)/h)
def func_prime(x,y):
    return y
#Euler
xe = np.zeros(n_points)
ye = np.zeros(n_points)
xe[0] = min_x
ye[0] = 1.0
for i in range(1,n_points):
    xe[i] = xe[i-1] + h
    ye[i] = ye[i-1] + h * func_prime(xe[i-1],ye[i-1])
#leap frog
xl = np.zeros(n_points)
yl = np.zeros(n_points)
xl[0] = min_x
yl[0] = 1.0
xl[1] = min_x + h
yl[1] = yl[0] + h*func_prime(xl[0],yl[0])
for i in range(2,n_points):
    xl[i] = xl[i-1] + h
    yl[i] = yl[i-2] + 2 * h * func_prime(xl[i-1],yl[i-1])
#Runge-kutta 4th
xk = np.zeros(n_points)
yk = np.zeros(n_points)
xk[0] = min_x
yk[0] = 1.0
for i in range(1,n_points):
    k1 = h * func_prime(xk[i-1]          , yk[i-1])
    k2 = h * func_prime(xk[i-1] + 0.5 * h, yk[i-1] + 0.5 * k1)
    k3 = h * func_prime(xk[i-1] + 0.5 * h, yk[i-1] + 0.5 * k2)
    k4 = h * func_prime(xk[i-1] + h      , yk[i-1] + k3)
    average_k = (k1 + 2.0*k2 + 2.0*k3 + k4)/6.    
    xk[i] = xk[i-1] + h
    yk[i] = yk[i-1] + average_k
#Graficas
fig = plt.figure()
ax1 = fig.add_subplot(321)
ax1.plot(xe,ye, 'ko')
ax1.plot(xe,np.exp(xe))
ax1.set_xlabel('x')
ax1.set_ylabel('y(x)')
ax1.set_title('euler')
ax2 = fig.add_subplot(322)
ax2.plot(xe,abs(np.exp(xe)-ye), 'ko')
ax2.set_xlabel('$x$')
ax2.set_ylabel('$|y_{\mathrm{true}}-y_{\mathrm{euler}}|$')
ax2.set_title('error')
ax3 = fig.add_subplot(323)
ax3.plot(xl,yl, 'ko')
ax3.plot(xl,np.exp(xl))
ax3.set_xlabel('x')
ax3.set_ylabel('y(x)')
ax3.set_title('leap frog')
ax4 = fig.add_subplot(324)
ax4.plot(xl,abs(np.exp(xl)-yl), 'ko')
ax4.set_xlabel('$x$')
ax4.set_ylabel('$|y_{\mathrm{true}}-y_{\mathrm{euler}}|$')
ax4.set_title('error')
ax5 = fig.add_subplot(325)
ax5.plot(xk,yk, 'ko')
ax5.plot(xk,np.exp(xk))
ax5.set_xlabel('x')
ax5.set_ylabel('y(x)')
ax5.set_title('Runge-kutta 4th')
ax6 = fig.add_subplot(326)
ax6.plot(xk,abs(np.exp(xk)-yk), 'ko')
ax6.set_xlabel('$x$')
ax6.set_ylabel('$|y_{\mathrm{true}}-y_{\mathrm{euler}}|$')
ax6.set_title('error')
plt.tight_layout()
plt.show()
