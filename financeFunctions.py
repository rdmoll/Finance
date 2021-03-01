# Geometric Brownian Motion

import numpy as np

# Simulate stock data

def gbmSimulation(num_ts, mu, sigma, S0 = 1.0):
    sigma2 = sigma * sigma
    drift = mu - 0.5*sigma2
    S = np.zeros((num_ts,3))

    N = np.random.normal(0.0, 1.0, num_ts-1)

    S[0,0] = S0
    S[0,1] = 0.0
    S[0,2] = 0.0
    for i in np.arange(1, num_ts):
        S[i,2] = S[i-1,2] + N[i-1]
        pctChange = np.exp( (drift*i) + (sigma*S[i,2]) )
        S[i,0] = S0 * pctChange
        S[i,1] = S[i,0] / S[i-1,0]

    return S

def kellySimulation(f, S, V_i, V_c):
  num_ts = S.shape[0]
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
  
  return V
