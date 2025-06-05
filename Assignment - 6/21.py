import matplotlib.pyplot as plt
import numpy as np

# #plot 1:
# x = np.array([0, 1, 2, 3])
# y = np.array([3, 8, 1, 10])

# plt.subplot(1, 2, 1)
# plt.plot(x,y)

# #plot 2:
# x = np.array([0, 1, 2, 3])
# y = np.array([10, 20, 30, 40])

# plt.subplot(1, 2, 2)
# plt.plot(x,y)

# plt.show()

temp = np.array([20,21,22,23,24,25])
time = np.array([1,2,3,4,5,6])

plt.subplot(1,2,1)
plt.plot(time , temp)

rain = np.array([0,1,0,1,0,1])
time = np.array([1,2,3,4,5,6])

plt.subplot(1,2,2)
plt.plot(time , rain)

plt.show()