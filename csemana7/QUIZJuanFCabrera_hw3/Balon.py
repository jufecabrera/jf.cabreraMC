import numpy as np
import matplotlib.pyplot as plt
g = -9.8 #m/s^2
dt = 0.001 #s
y = []
vy = []
t = []
#condiciones iniciales
y.append(0)
vy.append(5)
t.append(0)
#euler
b = True
i = 1
while(b):
	a = g
	t.append(t[i-1]+dt)
	vy.append(vy[i-1]+dt*a)
	y.append(y[i-1]+dt*vy[i-1])
	i += 1
	if(y[i-1]<=0.001):
		b = False
#graficas
plt.plot(t,y)
plt.title('posicion en funcion de tiempo')
plt.xlabel('tiempo (s)')
plt.ylabel('posicion y (m)')
plt.savefig('posBalon.pdf')
plt.close()
plt.plot(t,vy)
plt.title('velosidad en funcion de tiempo')
plt.xlabel('tiempo (s)')
plt.ylabel('velosidad y (m)')
plt.savefig('velBalon.pdf')
plt.close()
#altura maxima
amax = max(y)
print 'la altura maxima alcanzada es ',amax , 'm'
#tiempo total
Ttotal = (t[-1]+t[-2])/2
print 'el tiempo que el balon permanece en el aire es: ', Ttotal, 's mas o menos', dt/2,'s'
