# Kelly criterion solver

import matplotlib.pyplot as plt
import numpy as np
import financeFunctions as ff

# Single asset

num_ts = 100
mu = 0.009
sigma = 0.06
r = 0.0085

f = (mu - r) / (sigma * sigma)

print(f)
print()

V_c = 100.0
V_i = f * V_c

t = np.arange(num_ts)
S = ff.gbmSimulation(num_ts, mu, sigma)

V1 = ff.kellySimulation(0.5*f, S, V_i, V_c)
V2 = ff.kellySimulation(1.0*f, S, V_i, V_c)
V3 = ff.kellySimulation(1.5*f, S, V_i, V_c)

# Multi asset

# Plot results
plt.figure()
plt.plot(t,S)

plt.figure()
plt.plot(t,V1[:,2])
plt.plot(t,V2[:,2])
plt.plot(t,V3[:,2])
plt.show()
