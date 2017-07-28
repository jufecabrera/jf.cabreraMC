import numpy as np
import matplotlib.pyplot as plt
data = np.loadtxt('obs_data.dat')
xobs = data[:,0]
yobs = data[:,1]
def likelihood(mod):
	chisq = np.sum((yobs-mod)**2)
	return np.exp(-0.5*chisq)
def model(m,b):
	return m*xobs+b 
itera = 1000
mwalk = np.zeros((itera))
bwalk = np.zeros((itera))
lwalk = np.zeros((itera))
mwalk[0] = np.random.random()
bwalk[0] = np.random.random()
lwalk[0] = likelihood(model(mwalk[0],bwalk[0]))
for i in range(1,itera):
	mprime = np.random.normal(mwalk[i-1],0.1)
	bprime = np.random.normal(bwalk[i-1],0.1)
	alpha = likelihood(model(mprime,bprime))/lwalk[i-1]
	if (alpha>1):
		mwalk[i]= mprime
		bwalk[i]= bprime
		lwalk[i]= likelihood(model(mprime,bprime))
	else:
		beta = np.random.random()
		if (alpha>beta):
			mwalk[i]= mprime
			bwalk[i]= bprime
			lwalk[i]= likelihood(model(mprime,bprime))
		else:
			mwalk[i]= mwalk[i-1]
			bwalk[i]= bwalk[i-1]
			lwalk[i]= lwalk[i-1]
ibest = np.argmax(lwalk)
mbest = mwalk[ibest]
bbest = bwalk[ibest]
print  "los parametro encontrados son m=",mbest, "y b=",bbest
plt.scatter(mwalk,-np.log(lwalk))
plt.title('Parametro m')
plt.xlabel('m')
plt.ylabel('-log(L)')
plt.savefig('Param_m.pdf')
plt.close()
plt.scatter(bwalk,-np.log(lwalk))
plt.title('Parametro b')
plt.xlabel('b')
plt.ylabel('-log(L)')
plt.savefig('Param_b.pdf')
plt.close()
plt.scatter(xobs,yobs,label='Observados')
plt.plot(xobs,model(mbest,bbest),label='Modelo')
plt.title('Modelo')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.savefig('Modelo.pdf')
plt.close()
