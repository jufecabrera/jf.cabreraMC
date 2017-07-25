import numpy as np
import matplotlib.pyplot as plt
data = np.loadtxt("CircuitoRC.txt")
t= data[:,0]
q= data[:,1]
v0=10
def likelihood(y_obs, y_model):
    chi_squared = np.sum((y_obs-y_model)**2)*0.0001
    return np.exp(-chi_squared*0.5)

def my_model(x_obs, C, R):
    return v0*C*(1-np.exp(-x_obs/(R*C)))
C_walk = np.empty((0))
R_walk = np.empty((0))
l_walk = np.empty((0))
C_walk = np.append(C_walk, np.random.random())
R_walk = np.append(R_walk, np.random.random())
y_init = my_model(t, C_walk[0], R_walk[0])
l_walk = np.append(l_walk, likelihood(q, y_init))
n_iterations = 20000
for i in range(n_iterations):
    C_prime = np.random.normal(C_walk[i], 0.1) 
    R_prime = np.random.normal(R_walk[i], 0.1)

    y_init = my_model(t, C_walk[i], R_walk[i])
    y_prime = my_model(t, C_prime, R_prime)
    
    l_prime = likelihood(q, y_prime)
    l_init = likelihood(q, y_init)
    
    alpha = l_prime/l_init
    if(alpha>=1.0):
        C_walk  = np.append(C_walk,C_prime)
        R_walk  = np.append(R_walk,R_prime)
        l_walk = np.append(l_walk, l_prime)
    else:
        beta = np.random.random()
        if(beta<=alpha):
            C_walk = np.append(C_walk,C_prime)
            R_walk = np.append(R_walk,R_prime)
            l_walk = np.append(l_walk, l_prime)
        else:
            C_walk = np.append(C_walk,C_walk[i])
            R_walk = np.append(R_walk,R_walk[i])
            l_walk = np.append(l_walk, l_init)

max_likelihood_id = np.argmax(l_walk)
best_C = C_walk[max_likelihood_id]
best_R = R_walk[max_likelihood_id]
best_y = my_model(t, best_C, best_R)
print "C = ", best_C
print "R = ", best_R
print "Qmax = ", v0*best_C
fig = plt.figure()
ax1=fig.add_subplot(211)
ax1.scatter(C_walk, -np.log(l_walk))
ax1.set_xlabel('C_walk')
ax1.set_ylabel('-log(l_walk)')
ax1.set_title('C_walk')
ax2=fig.add_subplot(212)
ax2.scatter(R_walk, -np.log(l_walk))
ax2.set_xlabel('R_walk')
ax2.set_ylabel('-log(l_walk)')
ax2.set_title('R_walk')
plt.tight_layout()
plt.savefig('walk.pdf')
plt.close()

fig1 = plt.figure()
ax1=fig1.add_subplot(211)
ax1.hist(C_walk, 20, normed=True)
ax2=fig1.add_subplot(212)
ax2.hist(R_walk, 20, normed=True)
plt.savefig('hist.pdf')
plt.close()

plt.scatter(t,q,edgecolor='k', label='observados')
plt.plot(t, best_y,color='r',label='fit')
plt.xlabel('T (s)')
plt.ylabel('Q (C)')
plt.title('Bayesian')
plt.savefig('bayesian.pdf')

