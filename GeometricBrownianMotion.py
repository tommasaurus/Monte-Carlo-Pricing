 #%%

import matplotlib.pyplot as plt
import numpy as np
import math

#This class implements the stochastic process, Geometric Brownian Motion
class GeometricBrownianMotion:
    def __init__(self, initial_price, drift, volatility, dt, T):
        #both current and initial price begin at the input initial price
        self.current_price = initial_price
        self.initial_price = initial_price
        
        #drift is the expected return of the equity
        self.drift = drift
        
        #volatility of the equity for the period specified
        self.volatility = volatility
        
        #dt is the length of the time steps
        #ex: 1 day steps would be 1/365
        self.dt = dt
        #T is the actual length of the time period
        self.T = T
        self.prices = []
        self.sim()
    
    def sim(self):
        while (self.T -self.dt)>0: #loops through each day (step)
            dWt = np.random.normal(0, math.sqrt(self.dt)) #Brownian Motion
            #dYt = Change in Price (exp ret*1 step + exp volat*brown motion)
            dYt = self.drift*self.dt +self.volatility*dWt
            
            #inc current price by the change in price (dYt)
            self.current_price+=dYt
            self.prices.append(self.current_price)
            self.prices.append(self.current_price)  # Append new price to series
            self.T -= self.dt  # decrement by the step in time


#Example Model Paramets
paths = 50
initial_price = 10
drift = .08
volatility = .1
dt = 1/365
T = 1
price_paths = []

# Generate a set of sample paths
for i in range(0, paths):
    price_paths.append(GeometricBrownianMotion(initial_price, drift, volatility, dt, T).prices)

# Plot the set of generated sample paths
for price_path in price_paths:
    plt.plot(price_path)
plt.show()
             
            
    
# %%
