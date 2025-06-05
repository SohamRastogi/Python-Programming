import matplotlib.pyplot as plt
import numpy as np

temp = np.array([20,21,22,23,24,25,26,27,28,29,20,21,22,23,24,25,26,27,28,29,20,21,22,23,24,25,26,27,28,29])
windspeed = np.array([5,6,7,5,6,7,5,6,7,5,6,7,5,6,7,5,6,7,5,6,7,5,6,7,5,6,7,5,6,7])

plt.plot(temp , windspeed , marker = 'o' , mec = 'r' , mfc = 'r')

plt.xlabel("Temperature")
plt.ylabel("WindSpeed")

plt.show()