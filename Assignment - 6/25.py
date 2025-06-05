import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

temperature = np.array([20, 21, 22, 23, 24, 25, 26, 27])
humidity = np.array([60, 61, 62, 63, 64, 60, 61, 62])
windspeed = np.array([5, 6, 7, 5, 6, 7, 5, 6])

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(temperature, humidity, windspeed, c='green', marker='o', s=50)

ax.set_xlabel('Temperature')
ax.set_ylabel('Humidity')
ax.set_zlabel('WindSpeed')

plt.title('3D Scatter Plot: Temperature vs Humidity vs WindSpeed')
plt.tight_layout()
plt.show()
