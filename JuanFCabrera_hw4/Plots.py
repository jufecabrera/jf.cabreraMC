import numpy as np
import matplotlib.pyplot as plt
data = np.loadtxt('map_data.txt')
coor = np.loadtxt('m.txt')
x = coor[0]
y = coor[1]
r = coor[2]
rx = r*(360./744.)
ry = r*(180./500.)
thet=np.linspace(0,2*np.pi,1000)
xr = rx*np.cos(thet)+x
yr = ry*np.sin(thet)+y
plt.imshow(data,extent=[-180,180,-90,90])
plt.plot(x,y,'o',c='b')
plt.plot(xr,yr,c='b')
plt.title('Punto Nemo')
plt.xlabel('Longitud (grados)')
plt.ylabel('Latitud (grados)')
plt.savefig('PuntoNemo.pdf')
