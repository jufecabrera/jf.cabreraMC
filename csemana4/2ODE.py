import numpy as np
import matplotlib.pyplot as plt
h=0.01
min_x = 0.0
max_x = 6.0
n_points = int((max_x-min_x)/h)
#y_1'=y_2
#y''= -4y ==> y_2'=-4y_1
#Euler
x = np.zeros(n_points)
y_1e = np.zeros(n_points)
y_2e = np.zeros(n_points)
def func_prime_1(x, y_1, y_2):
    return y_2
def func_prime_2(x, y_1, y_2):
    return -4*y_1
#initial conditions
x[0] = min_x
y_1e[0] = 1.0
y_2e[0] = 0.0
for i in range(1,n_points):
    y_prime_1 = func_prime_1(x[i-1], y_1e[i-1], y_2e[i-1])
    y_prime_2 = func_prime_2(x[i-1], y_1e[i-1], y_2e[i-1])
    x[i] = x[i-1] + h
    y_1e[i] = y_1e[i-1] + h * func_prime_1(x[i-1], y_1e[i-1], y_2e[i-1])
    y_2e[i] = y_2e[i-1] + h * func_prime_2(x[i-1], y_1e[i-1], y_2e[i-1])
#Runge-kutta 4th
x = np.zeros(n_points)
y_1k = np.zeros(n_points)
y_2k = np.zeros(n_points)
#initial conditions
x[0] = min_x
y_1k[0] = 1.0
y_2k[0] = 0.0
def func_prime_1(x, y_1, y_2):
    return y_2
def func_prime_2(x, y_1, y_2):
    return -4*y_1
def RungeKuttaFourthOrderStep(x_old, y1_old, y2_old):
    k_1_prime1 = func_prime_1(x_old,y1_old, y2_old)
    k_1_prime2 = func_prime_2(x_old,y1_old, y2_old)
    #first step
    x1 = x_old+ (h/2.0)
    y1_1 = y1_old + (h/2.0) * k_1_prime1
    y2_1 = y2_old + (h/2.0) * k_1_prime2
    k_2_prime1 = func_prime_1(x1, y1_1, y2_1)
    k_2_prime2 = func_prime_2(x1, y1_1, y2_1)
    #second step
    x2 = x_old + (h/2.0)
    y1_2 = y1_old + (h/2.0) * k_2_prime1
    y2_2 = y2_old + (h/2.0) * k_2_prime2
    k_3_prime1 = func_prime_1(x2, y1_2, y2_2)
    k_3_prime2 = func_prime_2(x2, y1_2, y2_2)
    #third
    x3 = x_old + h
    y1_3 = y1_old + h * k_3_prime1
    y2_3 = y2_old + h * k_3_prime2
    k_4_prime1 = func_prime_1(x3, y1_3, y2_3)
    k_4_prime2 = func_prime_2(x3, y1_3, y2_3)
    #fourth step
    average_k_1 = (1.0/6.0)*(k_1_prime1 + 2.0*k_2_prime1 + 2.0*k_3_prime1 + k_4_prime1)
    average_k_2 = (1.0/6.0)*(k_1_prime2 + 2.0*k_2_prime2 + 2.0*k_3_prime2 + k_4_prime2)
    x_new = x_old + h
    y_1_new = y1_old + h * average_k_1
    y_2_new= y2_old + h * average_k_2
    return x_new, y_1_new, y_2_new
for i in range(1,n_points):
    x[i],y_1k[i],y_2k[i] = RungeKuttaFourthOrderStep(x[i-1], y_1k[i-1], y_2k[i-1])
#Graficas
fig = plt.figure()
ax1 = fig.add_subplot(221)
ax1.plot(x,y_1e, 'ko')
ax1.plot(x,np.cos(2.*x))
ax1.set_xlabel('x')
ax1.set_ylabel('y(x)')
ax1.set_title('euler')
ax2 = fig.add_subplot(222)
ax2.plot(x,abs(np.cos(2.*x)-y_1e), 'ko')
ax2.set_xlabel('$x$')
ax2.set_ylabel('$|y_{\mathrm{true}}-y_{\mathrm{euler}}|$')
ax2.set_title('error')
ax3 = fig.add_subplot(223)
ax3.plot(x,y_1k, 'ko')
ax3.plot(x,np.cos(2.*x))
ax3.set_xlabel('x')
ax3.set_ylabel('y(x)')
ax3.set_title('Runge-kutta 4th')
ax4 = fig.add_subplot(224)
ax4.plot(x,abs(np.cos(2.*x)-y_1k), 'ko')
ax4.set_xlabel('$x$')
ax4.set_ylabel('$|y_{\mathrm{true}}-y_{\mathrm{euler}}|$')
ax4.set_title('error')
plt.tight_layout()
plt.show()
