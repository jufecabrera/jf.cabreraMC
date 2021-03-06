import numpy as np
import matplotlib.pyplot as plt
datos = np.genfromtxt('datos.txt',delimiter=',')
datos = np.delete(datos,0,0)
def p(x):
	return np.sum(x)/len(x)
def pm(x):
	return np.sum(x)/(len(x)-1)
def cov(array):
	leng = len(array[0])
	matrix = np.ones((leng-1,leng-1))
	for i in range(1,leng):
		for j in range(1,leng):
			dat1 = array[:,i]
			dat2 = array[:,j]
			exp = pm((dat1-p(dat1))*(dat2-p(dat2)))
			matrix[i-1,j-1]= exp

	return matrix
matrix= cov(datos)
print "matrix\n", matrix
values, vectors = np.linalg.eig(matrix)
print "values", values
print "vectors\n", vectors
valueso = []
vectorso = []
for i in range(len(values)):
	valueso.append(np.max(values))
	vectorso.append(vectors[:,np.where(values == np.max(values))])
	values[np.where(values == np.max(values))] = -999
vectorso = np.array(vectorso).T 
print "arraged values", valueso
print "arranged vectors\n", vectorso
