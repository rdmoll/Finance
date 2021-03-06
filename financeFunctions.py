# Geometric Brownian Motion

import numpy as np

# Simulate stock data

def gbmSimulation(num_ts, mu, sigma, S0 = 1.0):
    sigma2 = sigma * sigma   # Calculate sigma^2
    drift = mu - 0.5*sigma2  # Calculate drift
    
    S = np.zeros(num_ts)     # Initialize stock price array
    Wt = np.zeros(num_ts)    # Initialize Wiener process array

    N = np.random.normal(0.0, 1.0, num_ts-1)  # Normally distributed array of values

    S[0] = S0  # Set initial stock price
    Wt[0] = 0.0   # Set initial value for Wiener process
    for i in np.arange(1, num_ts):
        Wt[i] = Wt[i-1] + N[i-1]                         # Wiener process
        S[i] = S0 * np.exp( (drift*i) + (sigma*Wt[i]) )  # Calculate simulated stock price

    return S

def kellySimulation(f, S, V_i, V_c):
  num_ts = S.shape[0]
  V = np.zeros((num_ts,3))
  V[0,0] = V_i
  V[0,1] = V_c
  V[0,2] = V_i + V_c
  for i in np.arange(1,num_ts):
    V_i = V_i * S[i] / S[i-1]
    V_tot = V_i + V_c
    V_i = f * V_tot
    V_c = (1 - f) * V_tot
    V[i,0] = V_i
    V[i,1] = V_c
    V[i,2] = V_tot
  
  return V
