import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 

gas = pd.read_csv('gas_prices.csv')
# print(gas.head())

plt.plot(gas.Year, gas.USA)
plt.plot(gas.Year, gas.Canada)
plt.show()