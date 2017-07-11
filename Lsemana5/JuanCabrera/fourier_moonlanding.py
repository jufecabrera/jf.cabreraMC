import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
#Lecura y transformada
img = plt.imread('moonlanding.png')
FT = np.fft.fft2(img)
#Grficas de imagen original y su transformada
fig=plt.figure()
ax1=fig.add_subplot(221)
ax1.imshow(img,cmap='gray')
ax1.set_title('Imagen original')
ax2=fig.add_subplot(222)
ax2.set_title('Espectro de potencias im original')
img=ax2.imshow(abs(FT)**2)
power_cut = 95.0
clipped_power = mlab.prctile((abs(FT)**2).flatten(), power_cut)
img.set_clim(0, clipped_power)
#Filtrado
new_FT=FT.copy()
new_FT[50:-50,:]= 0
new_FT[:,50:-50]= 0
#Graicas de imagen filtrada y su transformada
ax3=fig.add_subplot(224)
ax3.set_title('Espectro de potencias im modificada')
img1=ax3.imshow(abs(new_FT)**2)
img1.set_clim(0, clipped_power)
new_img= np.fft.ifft2(new_FT).real
ax4=fig.add_subplot(223)
ax4.set_title('Imagen modificada')
ax4.imshow(new_img,cmap='gray')
plt.tight_layout()
plt.savefig('moon_landing.png')
plt.close()
