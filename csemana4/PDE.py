import numpy as np
import matplotlib.pyplot as plt
n_x = 100
n_t = 4000
x = np.linspace(0, 10.0, n_x)
dx = x[1]-x[0]
dt = 0.001
c = 1.0
r =c*dt/dx
u = np.ones(n_x)
u[np.where((x<1.25) & (x>0.75))] = 2.0
#linear convection
fig = plt.figure()
ax1 = fig.add_subplot(221)
ax1.set_title('Linear Convection')
ax1.plot(x,u)
for n in range(n_t):  
    u_past = u.copy() 
    for i in range(1,n_x-1): 
        u[i] = u_past[i] - r*(u_past[i]-u_past[i-1])
    if (n%500==0):
	ax1.plot(x,u)
#nonlinear convection
u = np.ones(n_x)
u[np.where((x<1.25) & (x>0.75))] = 2.0
ax2 = fig.add_subplot(222)
ax2.set_title('Nonlinear Convection')
ax2.plot(x,u)
for n in range(n_t):  
    u_past = u.copy() 
    for i in range(1,n_x-1): 
        u[i] = u_past[i] - u_past[i]*dt/dx*(u_past[i]-u_past[i-1])
    if (n%500==0):
	ax2.plot(x,u)
#Difusion
n_xd = 100
n_td = 4000
nu = 0.3
sigma = 0.2 
xd = np.linspace(0, 2.0, n_xd)
dxd = xd[1]-xd[0]
dtd = sigma*dxd**2/nu
alpha = dtd/dxd**2
u = np.ones(n_xd)
u[np.where((xd<1.25) & (xd>0.75))] = 2.0
ax3 = fig.add_subplot(223)
ax3.set_title('Difusion')
ax3.plot(xd,u)
for n in range(n_t):  
    u_past = u.copy() 
    for i in range(1,n_xd-1): 
        u[i] = nu*alpha*u_past[i+1]+(1-2*nu*alpha)*u_past[i]+nu*alpha*u_past[i-1]
    if (n%500==0):
	ax3.plot(xd,u)
#Burgers
n_xb = 100
n_tb = 4000
nub = 0.07
sigmab = 0.02 
xb = np.linspace(0, 2.0*np.pi, n_xb)
dxb = xb[1]-xb[0]
dtb = sigmab*dxb**2/nub
alphab = dtb/dxb**2
u = np.sin(xb)
ax4 = fig.add_subplot(224)
ax4.set_title('Burgers')
ax4.plot(xb,u)
for n in range(n_tb):  
    u_past = u.copy() 
    for i in range(1,n_xb-1):
        u[i] = u_past[i] - u_past[i]*dtb/dxb*(u_past[i]-u_past[i-1]) + nub * alphab * (u_past[i+1] -2.0*u_past[i]+u_past[i-1])
    u[-1] = u_past[-1] - u_past[-1]*dtb/dxb*(u_past[-1]-u_past[-2]) + nub * alphab * (u_past[0] -2.0*u_past[-1]+u_past[-2])
    if (n%500==0):
	ax4.plot(xb,u)
plt.tight_layout()
plt.show()
plt.close()

