import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
sigma = 10.0
rho = 28.0
beta = 8./3.
h = 0.01
N = int(40/h) #numero de puntos
def dxdt(x,y,z):
	return sigma*(y-x)
def dydt(x,y,z):
	return x*(rho-z)-y
def dzdt(x,y,z):
	return x*y-beta*z
def euler(x_old,y_old,z_old):
	x_new=x_old+h*dxdt(x_old,y_old,z_old)
	y_new=y_old+h*dydt(x_old,y_old,z_old)
	z_new=z_old+h*dzdt(x_old,y_old,z_old)
	return x_new, y_new, z_new
x=range(N)
y=range(N)
z=range(N) 
#condiciones iniciales
x[0]=1.
y[0]=1.
z[0]=1.
for i in range(1,N):
	step=euler(x[i-1],y[i-1],z[i-1])
	x[i]= step[0]
	y[i]= step[1]
	z[i]= step[2]
#grafica 3D
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot(x, y, z, linewidth=0.8)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Solucion al sistema de Lorenz')
plt.savefig('lorenz.png')
