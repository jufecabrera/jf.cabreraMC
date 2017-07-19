import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-4.0,4.0,1000)
def nasty_function(x):
    x_0 = 3.0
    a = 0.01
    return np.exp(-(x**2))/((x-x_0)**2 + a**2)
n_iterations = 200000
x_walk = np.empty((0)) 
x_0 = 8.0*((np.random.rand())-0.5) 
x_walk = np.append(x_walk,x_0)
for i in range(n_iterations):
	x_prime = np.random.normal(x_walk[i],0.1)
	alpha = nasty_function(x_prime)/ nasty_function(x_walk[i])
	if (alpha>=1.0):
		x_walk = np.append(x_walk,x_prime)
	else:
		beta = np.random.rand()
		if (beta<=alpha):
			x_walk = np.append(x_walk, x_prime)
		else:
			x_walk = np.append(x_walk,x_walk[i])
norm = nasty_function(x)/np.sum(nasty_function(x)*(x[1]-x[0]))
plt.plot(x,norm, linewidth=1, color='r')
plt.hist(x_walk, 1000, normed=True)
plt.show()
