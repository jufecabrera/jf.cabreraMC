import numpy as np
#7
x7 = np.random.rand(3,3)
print x7
x7 = (x7-x7.min())/(x7.max()-x7.min())
print x7
#11
x11 = np.random.rand(15)
print x11
x11[np.where(x11==x11.max())]=-1
print x11
#13
x13 = np.random.randint(0,10,40)
print x13
print(np.bincount(x13).argmax())
