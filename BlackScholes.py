# Black-Scholes equation

import matplotlib.pyplot as plt
import numpy as np
from scipy import special

S_low = 150.0
S_high = 220.0
dS = 1.0
K = 190.0
T = 0.45
dt = 0.1
r = 0.001
sigma = 0.9

#S_low = 70.0
#S_high = 130.0
#dS = 1.0
#K = 100.0
#T = 1.0
#dt = 0.1
#r = 0.12
#sigma = 0.1

t = np.arange(0.0, T, dt)
S = np.arange(S_low, S_high, dS)
t, S = np.meshgrid(t, S)

d1 = ( np.log(S/K) + (r + 0.5*(sigma**2))*(T-t) ) / sigma*np.sqrt(T-t)
d2 = ( np.log(S/K) + (r - 0.5*(sigma**2))*(T-t) ) / sigma*np.sqrt(T-t)

Phi1_call = 0.5*(special.erf(d1/np.sqrt(2.0)) + 1.0)
Phi2_call = 0.5*(special.erf(d2/np.sqrt(2.0)) + 1.0)
Phi1_put = 0.5*(special.erf(-d1/np.sqrt(2.0)) + 1.0)
Phi2_put = 0.5*(special.erf(-d2/np.sqrt(2.0)) + 1.0)

V_call = S*Phi1_call - K*np.exp(-r*(T-t))*Phi2_call
V_put = K*np.exp(-r*(T-t))*Phi2_put - S*Phi1_put

call_zeros = V_call < 0.0
V_call[call_zeros] = 0.0

put_zeros = V_put < 0.0
V_put[put_zeros] = 0.0

# Plot results
fig_call = plt.figure()
ax_call = fig_call.gca(projection='3d')
surf_call = ax_call.plot_surface(S, t, V_call)

fig_put = plt.figure()
ax_put = fig_put.gca(projection='3d')
surf_put = ax_put.plot_surface(S, t, V_put)

plt.show()
