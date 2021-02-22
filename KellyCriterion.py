# Kelly criterion solver

import matplotlib.pyplot as plt
import numpy as np
import financeFunctions as ff

# Single asset

# Define parameters
#T = 1.0
#dt = 0.001
#t = np.arange(0.0, T, dt)

#S0 = 1.0
#mu = 0.01
#r = 0.0085
#sigma = 0.05
#sigma2 = sigma**2
#f = (mu - r) / sigma2

#print(f)
#print()

# Brownian motion
#W = np.zeros(t.size)
#N = np.random.normal(0.0, sigma, t.size-1)
#for i in np.arange(t.size-1):
#    W[i+1] = W[i] + N[i]
#
#S = S0 * np.exp((mu - 0.5*sigma2)*t + sigma*W)
#drift = S0 * np.exp(mu*t)

# generate simulated stock history
# set up time step loop
#for i in np.arange(0,t.size):
    #position = f * S[i]
    #cash = prevPos + cash
    # calculate leveraged position and equity at each time step based on f

num_ts = 100
mu = 0.01
sigma = 0.05

t = np.arange(num_ts)
S = ff.gbmSimulation(num_ts, mu, sigma)

# Plot results
plt.figure()
plt.plot(t,S[:,0])
#plt.plot(t,S)
#plt.plot(t,drift)
plt.show()
