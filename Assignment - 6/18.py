# temp , rainfall , humidity , windspeed

import matplotlib.pyplot as plt
import numpy as np

temp = np.array([20,21,22,23,24,25])
rain = np.array([0,1,0,1,0,1])

plt.scatter(temp , rain)

humid = np.array([5,6,7,5,6,7])
wind = np.array([1,2,3,4,5,6])

plt.scatter(humid , wind)
plt.show()