import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation
datos = np.loadtxt('planetas.csv', delimiter=',')
datos = datos[::1000]
n_points=len(datos[:,0])
l=np.size(datos[0])
t = datos[:,0]
n =['Sun','Mercury','Venus','Earth','Mars','Jupiter','Saturn','Uranus','Neptune','Pluto']
c=['gold','k','y','g','r','c','m','b','lime','gray']
for i in range(1,l):
	ii = i-1
	globals()['d%s' % ii] = datos[:,i]
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
for i in range(10):
	ax.plot(globals()['d%s' % i],globals()['d1%s' % i],globals()['d2%s' % i],color=c[i], label=n[i])
	globals()['line%s' % i], = ax.plot([],[],[],'o',color=c[i])
ax.set_title('Orbitas de los Planetas')
ax.set_xlabel('x (AU)')
ax.set_ylabel('y (AU)')
ax.set_zlabel('z (AU)')
ax.legend(loc='upper left',fontsize=9)
plt.savefig('orbitas.png')
def animate(i):
	for j in range(10):
		globals()['line%s' % j].set_data([globals()['d%s' % j][i]],[globals()['d1%s' % j][i]])
		globals()['line%s' % j].set_3d_properties([globals()['d2%s' % j][i]])
	lines = [globals()['line%s' % j] for j in range(10)]
	return tuple(lines)	
ani = animation.FuncAnimation(fig, animate, np.arange(1, n_points),interval=8, blit=False)
ani.save('Planetas.mp4')
plt.close()
