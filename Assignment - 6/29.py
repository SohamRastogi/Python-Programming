import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import griddata

temperature = np.array([20, 21, 22, 23, 24, 25, 26, 27, 28, 29])
humidity = np.array([60, 61, 62, 63, 64, 60, 61, 62, 63, 64])
windspeed = np.array([5, 6, 7, 5, 6, 7, 5, 6, 7, 5])


grid_x, grid_y = np.meshgrid(
    np.linspace(min(temperature), max(temperature), 100),
    np.linspace(min(humidity), max(humidity), 100)
)

grid_z = griddata((temperature, humidity), windspeed, (grid_x, grid_y), method='cubic')

plt.figure(figsize=(8, 6))
contour = plt.contourf(grid_x, grid_y, grid_z, levels=20, cmap='viridis')
plt.colorbar(contour, label='Wind Speed')
plt.xlabel('Temperature (°C)')
plt.ylabel('Humidity (%)')
plt.title('2D Contour Plot of Wind Speed')
plt.tight_layout()
plt.show()
