import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
#theta''+ g/l theta = 0
#th_1'=th_2
#th''= -(g/l)sin(th)-b*th' ==> th_2'=-(g/l)sin(th_1)
g=9.8
l=0.4
blib=0
bsub=0.5
bcrit=9.899
bsob=20.
h=0.01
min_t = 0.0
max_t = 15.0
n_points = int((max_t-min_t)/h)
t = np.zeros(n_points)
th_1 = np.zeros(n_points)
th_2 = np.zeros(n_points)
t[0] = min_t
th_1[0] = np.pi/4.
th_2[0] = 0.
def func_prime_1(x, y_1, y_2):
    return y_2
def func_prime_2(x, y_1, y_2):
    return -(g/l)*np.sin(y_1)-bsub*y_2
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
    t[i],th_1[i],th_2[i] = RungeKuttaFourthOrderStep(t[i-1], th_1[i-1], th_2[i-1])
plt.plot(t,th_1, 'ko')
#plt.show()
plt.close()
x = l*np.sin(th_1)
y = -l*np.cos(th_1)
fig = plt.figure(figsize=(5,5))
line, = plt.plot([],[],'-o')
plt.xlim(-(l+0.05),l+0.05)
plt.ylim(-(l+0.05),l+0.05)
def animate(i):
	line.set_data([0,x[i]],[0,y[i]])
	return line,
ani = animation.FuncAnimation(fig, animate, np.arange(1, n_points),interval=25, blit=True)
plt.show()

