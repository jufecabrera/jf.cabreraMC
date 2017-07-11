a= 27
b= 83
#a es impar?
if (a%2==0):
	print "%d es par" % (a)
else:
	print "%d es impar" % (a)
#divisres de a
print "los dividores de a son:"
for i in range(1,a+1):
	if (a%i == 0):
		print i
#max comun divisor
max_d=0
for j in range(1,a+1):
	if (a%j == 0 and b%j == 0):
		max_d=j
print "El maximo comun divisor entre a y b es %d" % (max_d)

