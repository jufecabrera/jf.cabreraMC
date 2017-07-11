import numpy as np
A = np.matrix('1. 2. 3. 0.; 4. 5. 6. 0.; 7. 12. 9. 0.') 
for i in range(0,len(A)):
	A[i]=A[i]/A[i,i]
	for j in range((i+1),len(A)):
		if (j==len(A)):
			break
		A[j]= A[j]- A[j,i]*A[i]
print A
x = []
k = len(A)-1
while (k>=0):
	for i in range(k,len(A))
	s = np.sum()
	np.insertA[]
