import numpy as np
import matplotlib.pyplot as plt
x = linspace(-4.0,4.0,1000)
def nasty_function(x):
    x_0 = 3.0
    a = 0.01
    return exp(-(x**2))/((x-x_0)**2 + a**2)
plt.plot(x,nasty_function(x))
n_iterations = 200000
x_walk = np.empty((0)) 
x_0 = 8.0*((np.random.rand())-0.5) 
x_walk = np.append(x_walk,x_0)
for i in range(n_iterations):
	x_pr = np.random.normal(x_walk[i],0.1)
	alpha = nasty_function(x_prime)
