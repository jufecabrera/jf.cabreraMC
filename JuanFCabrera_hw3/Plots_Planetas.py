import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation
datos = np.loadtxt('planetas.csv', delimiter=',')
n_points=len(datos[:,0])
l=np.size(datos[0])
t = datos[:,0]
for i in range(1,l):
	ii = i-1
	globals()['d%s' % ii] = datos[:,i]
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
for i in range(5):
	j = i+10
	k = i+20
	ax.plot(globals()['d%s' % i],globals()['d%s' % j],globals()['d%s' % k])
plt.show()
