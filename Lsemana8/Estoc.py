import numpy as np
import matplotlib.pyplot as plt
dat = np.loadtxt("E.txt")
n = dat[:,1]
y = dat[:,0]
m = dat[:,2]
t = np.linspace(0,10,1000)
plt.plot(t,y)
plt.plot(t,n)
plt.plot(t,m)
plt.show()
