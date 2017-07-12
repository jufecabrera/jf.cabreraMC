import numpy as np
A = np.array([[1., 2., 3., 5., 1.], [2., 2., 5., 6., 0.],[11., 7., 12., 9., 0.],[32., 1., 23., 2., 5.]])
print "la Matriz aumentada original: \n", A
l,k = np.shape(A)
for i in range(0,l):
	A[i]=A[i]/A[i][i]
	for j in range((i+1),l):
		A[j]= A[j]- A[j][i]*A[i]
print "la matriz aumentada reducida: \n", A
x = []
o = np.ones(k)
for i in reversed(range(0,l)):
	A[i] = A[i]*o
	s = np.sum(A[i][i+1:l])
	o[i] = A[i][k-1]-s
	x.insert(0,o[i])
print "El vector solucion: \n", x
