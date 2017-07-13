import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation
datos = np.loadtxt('planetas.csv', delimiter=',')
n_points=len(datos[:,0])
t = datos[:,0]
x0=datos[:,1]
y0=datos[:,2]
z0=datos[:,3]
x1=datos[:,4]
y1=datos[:,5]
z1=datos[:,6]
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
line, = ax.plot([],[],[],'ko')
def animate(i):
	line.set_data([x0[i],x1[i]],[y0[i],y1[i]],[z0[i],z1[i]])
	return line,
ani = animation.FuncAnimation(fig, animate, np.arange(1, n_points),interval=250, blit=True)
plt.show()

