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
plt.plot(t,x0)
plt.plot(t,x1)
#plt.show()
plt.close()
plt.plot(t,y0)
plt.plot(t,y1)
#plt.show()
plt.close()
plt.plot(t,z0)
plt.plot(t,z1)
#plt.show()
plt.close()

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(x1,y1,z1)
ax.plot(x0,y0,z0)
line, = ax.plot([],[],[],'o')
line1, = ax.plot([],[],[],'o')
def animate(i):
	line.set_data([x1[i]],[y1[i]])
	line.set_3d_properties([z1[i]])
	line1.set_data([x0[i]],[y0[i]])
	line1.set_3d_properties([z0[i]])
	return line,line1,
ani = animation.FuncAnimation(fig, animate, np.arange(1, n_points),interval=25, blit=True)
plt.show()

