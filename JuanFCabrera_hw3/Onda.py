import numpy as np
import matplotlib.pyplot as plt
M = np.zeros((300,300))
M[100,150]=-0.5
dx,dy=30./len(M[0])
t_max=60
points = 600
dt = float(t_max)/points
for k in range(points):
	M_past = M.copy()
	for j in range(1,points-1):
		 
	 
