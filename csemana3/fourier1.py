import numpy as np
import matplotlib.pyplot as plt
N = 200. #puntos 
f = 60. #Hz 
T = 1/f #periodo
dt= T/32 #muestras por periodo
t = np.linspace(0, (N-1)*dt, N)
n = np.linspace(-500,500,1001)

sr=1/(t[1]-t[0])
def func(x):
	return np.cos(2*np.pi*f*x)
y = func(t)
plt.plot(t,y)
plt.plot(t,y, 'ko')
plt.xlabel('time(s)')
plt.ylabel('y(t)')
plt.show()
def Gf(ni):
	e = np.exp(-1j*2*np.pi*t*ni*sr/N)
	#print y
	return np.sum(y*e)
G = []
for i in n:
	G.append(Gf(i))	
plt.plot(n,(G))
print np.real(G)
from scipy.fftpack import fft, fftfreq
fft_x = fft(y) / int(N) # FFT Normalized
freq = fftfreq(int(N), dt) # Recuperamos las frecuencias
plt.plot(freq,abs(fft_x))
plt.show()
