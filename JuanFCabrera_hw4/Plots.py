import numpy as np
import matplotlib.pyplot as plt
data = np.loadtxt('map_data.txt')
plt.imshow(data)
print np.shape(data)
