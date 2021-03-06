import numpy as np
import matplotlib.pyplot as plt
points = 10000
x=np.zeros(points)
x1=np.zeros(points)
x2=np.zeros(points)
x[0]=0.5#m
x1[0]=0.0#m/s
k=42.0#N/m
g=9.8#m/s**2
m=0.25#kg
mu=0.15
h=0.001
for i in range(points-1):
	sign = 1
	if (x1[i]>0):
		sign = -1
	x2[i]=-k/m*x[i]+(sign*mu*g)
	x[i+1]=x1[i]*h+x[i]
	x1[i+1]=x2[i]*h+x1[i]
plt.plot(x)
plt.show()
