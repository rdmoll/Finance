# Kelly criterion solver

import matplotlib.pyplot as plt
import numpy as np

# Single asset
T = 1.0
dt = 0.001
t = np.arange(0.0, T, dt)

S0 = 1.0
mu = 0.01
r = 0.0085
sigma = 0.05
sigma2 = sigma**2
f = (mu - r) / sigma2
print(f)
print()
if f > 1.0:
    f = 1.0
if f < 0.0:
    f = 0.0

f_array = np.arange(0.0,1.0,0.01)
totYield = np.zeros(100)
for k in np.arange(100):
    f = f_array[k]
    totRetVal = 0.0
    for j in np.arange(1000):
        # Brownian motion
        N = np.random.normal(0.0, sigma, t.size-1)
        W = np.zeros(t.size)
        for i in np.arange(t.size-1):
            W[i+1] = W[i] + N[i]

        S = S0 * np.exp((mu - 0.5*sigma2)*t + sigma*W)
        drift = S0 * np.exp(mu*t)

        retVal = S[S.size-1]
        totRetVal += retVal

    totRetVal /= 1000.0
    #print(f)
    #print(totRetVal)
    #print(totRetVal*f + (1.0 + r)*(1.0 - f))
    #print()
    totYield[k] = totRetVal*f + (1.0 + r)*(1.0 - f)

# Plot brownian motion
#plt.plot(t,np.log(S))
plt.figure()
plt.plot(t,S)
plt.plot(t,drift)

plt.figure()
plt.plot(f_array,totYield)

plt.show()
