# Kelly criterion solver

import matplotlib.pyplot as plt
import numpy as np
import financeFunctions as ff

# Single asset

num_ts = 100
mu = 0.01
sigma = 0.06
r = 0.0085

f = (mu - r) / (sigma * sigma)

print(f)
print()

V_c = 100.0
V_i = f * V_c

t = np.arange(num_ts)
S = ff.gbmSimulation(num_ts, mu, sigma)

V = np.zeros((num_ts,3))
V[0,0] = V_i
V[0,1] = V_c
V[0,2] = V_i + V_c
for i in np.arange(1,num_ts):
  V_i = V_i * S[i,1]
  V_tot = V_i + V_c
  V_i = f * V_tot
  V_c = (1 - f) * V_tot
  V[i,0] = V_i
  V[i,1] = V_c
  V[i,2] = V_tot

# Plot results
plt.figure()
plt.plot(t,S[:,0])
plt.figure()
plt.plot(t,S[:,1])
plt.figure()
plt.plot(t,V[:,2])
plt.show()
