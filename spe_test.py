from scipy.stats import norm, rayleigh
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import numpy as np

samp = rayleigh.rvs(loc=5,scale=2,size=150) # samples generation

print (samp)
param = rayleigh.fit(samp) # distribution fitting

x = np.linspace(5,13,100)
# fitted distribution
pdf_fitted = rayleigh.pdf(x,loc=param[0],scale=param[1])
# original distribution
pdf = rayleigh.pdf(x,loc=5,scale=2)

plt.title('Rayleigh distribution')
plt.plot(x,pdf_fitted,'r-',x,pdf,'b-')
plt.hist(samp,normed=1,alpha=.3)
plt.show()
