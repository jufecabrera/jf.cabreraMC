import numpy as np
import matplotlib.pyplot as plt
data = np.loadtxt('map_data.txt')
coor = np.loadtxt('m.txt')
x = coor[:,0]
y = coor[:,1]
#r = float(coor[2])
fig = plt.figure()
ax= fig.add_subplot(111) 
ax.imshow(data)
ax.plot(x,y,'-o')
#circle = plt.Circle((x, y), r, color='b', fill=False)
#ax.add_artist(circle)
plt.show()
#plt.savefig('PuntoNemo.pdf')
