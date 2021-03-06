import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
t = 10000
u = np.zeros((t,1000))
x = np.linspace(0,1,1000)
dx = x[1]-x[0]
dt = 0.0005
c = 1
gamma = c*dt/dx
u[0] = np.exp(-(x-0.3)**2/0.01)
u[0,-1]= 0
u[0,0]= 0
for i in range(1,len(u[0])-1):
	u[1,i] = u[0,i]+ gamma**2/2*(u[0,i+1]-2*u[0,i]+u[0,i-1])
for i in range(1,t-1):
	for j in range(1,len(u[0])-1):
		u[i+1,j]=2*(1-gamma**2)*u[i,j]-u[i-1,j]+gamma**2*(u[i,j+1]+u[i,j-1])
		
fig = plt.figure()
line, = plt.plot([],[],)
plt.xlim(0,1)
plt.ylim(-1,1)
def animate(i):
	line.set_data([x],[u[i]])
	return line,
ani = animation.FuncAnimation(fig, animate, np.arange(1,t),interval=10, blit=True)
plt.show()
