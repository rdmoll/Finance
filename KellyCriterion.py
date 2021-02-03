# Kelly criterion solver

import matplotlib.pyplot as plt
import numpy as np

# Single asset
T = 1.0
dt = 0.001
t = np.arange(0.0, T, dt)

mu = 0.1
r = 0.0085
sigma = 0.03
sigma2 = sigma**2
f = (mu - r) / sigma2
print(f)

# Brownian motion
N = np.random.normal(0.0, sigma, t.size-1)
W = np.zeros(t.size)
for i in np.arange(t.size-1):
    W[i+1] = W[i] + N[i]

S0 = 1.0
S = S0 * np.exp((mu - 0.5*sigma2)*t + sigma*W)
drift = S0 * np.exp(mu*t)

# Plot brownian motion
#plt.plot(t,np.log(S))
plt.plot(t,S)
plt.plot(t,drift)
plt.show()
