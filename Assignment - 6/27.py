import matplotlib.pyplot as plt
import numpy as np

month = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
temp = np.array([20,22,21,24,25,22,26,30,32,16,18,26])

plt.plot(month , temp , marker = 'o' , ms = 10 , mec = 'r' , mfc = 'r')

plt.xlabel("Month")
plt.ylabel("Average Temperature")

plt.show()
