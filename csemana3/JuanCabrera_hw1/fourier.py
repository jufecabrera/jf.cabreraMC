import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft, fftfreq
mag = np.loadtxt('magnitude.dat')
fas = np.loadtxt('phase.dat')
print mag
f = mag*np.exp(1j*fas)
F= fftpack.ifft2(f)
plt.imshow(F)
plt.savefig('secret.jpg')
