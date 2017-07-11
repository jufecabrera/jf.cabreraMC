infile = open('pg1524.txt','r')
lines = infile.readlines()

words = []
for i in range(len(lines)):
	x = lines[i].split()
	words.extend(x)
def func(m):
	n=0
	for j in range(len(words)):
		if (len(words[j])==m):
			n=n+1
	return n
for l in range(1,30):
	print "De %d caracteres hay %d palabras" % (l,func(l))
maxlet=0
maxwor=0
for j in range(len(words)):
		if (len(words[j])>maxlet):
			maxlet=len(words[j])
			maxwor=words[j]
print "la palabra mas larga es %s con %d caracteres" % (maxwor, maxlet)
