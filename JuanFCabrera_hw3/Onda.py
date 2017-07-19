import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
x = y =np.linspace(0,30,300)
dx = dy = 30./300
dt = dx*np.sqrt(0.5)
r2=(dt/dx)**2
t_max= 60
steps = t_max/dt
M = np.zeros((int(steps),300,300))
for i in range(191,209):
	for j in range(141,159):
		M[0,i,j]=-0.5*np.exp(-((i-200)**2+(j-150)**2)/2)
M[:,100,0:130]=-2
M[:,100,-130:-1]=-2
#t=1
for i in range(1,299):
	for j in range(1,299):
		if (i==99 or i==100 or i==101):
			if (j<=131 or j>=169):
				continue
		M[1,i,j] =r2/2*(M[0,i+1,j]+M[0,i-1,j]-4*M[0,i,j]+M[0,i,j+1]+M[0,i,j-1])+M[0,i,j]
#todos los tiempos
for k in range(1,int(steps)-1):
	for i in range(1,299):
		for j in range(1,299):
			if (i==99 or i==100 or i==101):
				if (j<=131 or j>=169):
					continue
			M[k+1,i,j] = r2*(M[k,i+1,j]+M[k,i-1,j]-4*M[k,i,j]+M[k,i,j+1]+M[k,i,j-1])+2*M[k,i,j]-M[k-1,i,j]
M = M+2
plt.pcolormesh(x,y,M[423])
plt.title('T = 30')
plt.figsave('30.png')
plt.close()
plt.pcolormesh(x,y,M[847])
plt.title('T = 60')
plt.figsave('60.png')
plt.close()
fig, ax = plt.subplots(figsize=(7, 6))
cax = ax.pcolormesh(x,y,M[0,:-1, :-1],vmin=1.99, vmax=2.01,cmap='seismic')
fig.colorbar(cax)
def animate(i):
	cax.set_array(M[i,:-1, :-1].flatten())
	return cax	
ani = FuncAnimation(fig, animate, np.arange(1,int(steps)),interval=5, blit=False)
plt.show()
#ani.save('Onda.mp4')
plt.close()




