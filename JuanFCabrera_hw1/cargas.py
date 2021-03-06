import numpy as np
import matplotlib.pyplot as plt
k = 8.987E9 #Nm^2C^-2
e = 1.602176E-19 #C
#Para facilitar el calculo numerico, se cambia la constante k por kn con unidades de nm y e en vez de C y m
kn = k*e**2/(1E-9)**2 #Nnm^2e^-2
class Carga:
	def __init__(self,x,y,q):
		self.x = x
		self.y = y
		self.q = q
	def V(self,x,y):
		R = np.sqrt((x-self.x)**2+(y-self.y)**2)
		return kn*self.q/R
Q1 = Carga(0.5,0.5,-1.)
Q2 = Carga(-0.5,0.5,1.)
Q3 = Carga(-0.5,-0.5,-1.)
Q4 = Carga(0.5,-0.5,1.)
x =np.linspace(-1.,1.,200)
y =np.linspace(-1.,1.,200)
h=x[1]-x[0]
X,Y = np.meshgrid(x,y)
#potencial
def pot(x,y):
	return Q1.V(x,y)+Q2.V(x,y)+Q3.V(x,y)+Q4.V(x,y)
#campo
Ex=-(pot(X+(h/2.),Y)-pot(X-(h/2.),Y))/h
Ey=-(pot(X,Y+(h/2.))-pot(X,Y-(h/2.)))/h
#graficas
plt.figure()
plt.pcolormesh(x,y,pot(X,Y),cmap='gnuplot2')
plt.xlabel('x (nm)')
plt.ylabel('y (nm)')
plt.colorbar()
plt.title('Potencial y Campo Electrico')
plt.streamplot(X,Y,Ex,Ey,linewidth=1,density=1.5,color='0')
plt.savefig('cargas.pdf')
