import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.fftpack import fft, fftfreq, ifft
rate, data = wavfile.read('violin.wav')
dt = 1/float(rate)
N = np.size(data)
FT = fft(data)
FTfr = fftfreq(N,dt)
plt.plot(FTfr[0:N/2],abs(FT[0:N/2]))
plt.title('Tranformada violin')
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('|FT|')
plt.savefig('Violin.pdf')
plt.close()
def BP(FT,x):
	y=FT.copy()
	y[np.where(abs(x)<1000)]=0
	y[np.where(abs(x)>2000)]=0
	return y
new_FT=BP(FT,FTfr)
fig= plt.figure()
ax1=fig.add_subplot(212)
ax1.plot(FTfr[0:N/2],abs(new_FT[0:N/2]))
ax1.set_xlabel('Frecuencia (Hz)')
ax1.set_ylabel('|FT|')
ax1.set_title('Tranformada filtrada')
ax2= fig.add_subplot(211)
ax2.plot(FTfr[0:N/2],abs(FT[0:N/2]))
ax2.set_title('Tranformada violin')
ax2.set_xlabel('Frecuencia (Hz)')
ax2.set_ylabel('|FT|')
plt.tight_layout()
plt.savefig('ViolinFiltro.pdf')
plt.close()
