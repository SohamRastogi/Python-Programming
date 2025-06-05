import matplotlib.pyplot as plt
import numpy as np

temp = np.array([20,21,22,23,24])
humid = np.array([5,6,7,5,6])
rain = np.array([0,1,0,1,0])

time = np.array([1,2,3,4,5])

plt.plot(time,temp)
plt.plot(time,humid)
plt.plot(time,rain)

plt.legend(title = "cumulative graph")
plt.show()
