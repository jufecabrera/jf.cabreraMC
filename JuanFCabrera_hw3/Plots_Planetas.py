import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation
datos = np.loadtxt('planetas.csv', delimiter=',')
datos = datos[::1000]
n_points=len(datos[:,0])
l=np.size(datos[0])
t = datos[:,0]
for i in range(1,l):
	ii = i-1
	globals()['d%s' % ii] = datos[:,i]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
for i in range(10):
	ax.plot(globals()['d%s' % i],globals()['d1%s' % i],globals()['d2%s' % i])
	globals()['line%s' % i], = ax.plot([],[],[],'o')
def animate(i):
	for j in range(10):
		globals()['line%s' % j].set_data([globals()['d%s' % j][i]],[globals()['d1%s' % j][i]])
		globals()['line%s' % j].set_3d_properties([globals()['d2%s' % j][i]])
	lines = [globals()['line%s' % j] for j in range(10)]
	return tuple(lines)	
ani = animation.FuncAnimation(fig, animate, np.arange(1, n_points),interval=8, blit=False)
plt.show()
