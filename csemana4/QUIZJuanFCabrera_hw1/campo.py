import numpy as np
import matplotlib.pyplot as plt
datos = np.loadtxt('pot.dat')
pos = datos[:,0]
pot = datos[:,1]
h = pos[1]-pos[0]
campo = -(pot[2:len(pot)]-pot[0:len(pot)-2])/2*h 
posn = pos[1:len(pot)-1]
plt.figure()
plt.scatter(posn,campo)
plt.title('campo electrico contra posiscion')
plt.xlabel('posicion')
plt.ylabel('magnitud del campo')
plt.savefig('campo.pdf')


