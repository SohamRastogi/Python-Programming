import numpy as np
import matplotlib.pyplot as plt

def generate_2d_gaussian(size=100, mean=0, std=1):
   
    x = np.linspace(-3*std, 3*std, size)
    y = np.linspace(-3*std, 3*std, size)
    X, Y = np.meshgrid(x, y) 
   
    Z = (1 / (2 * np.pi * std**2)) * np.exp(-((X - mean)**2 + (Y - mean)**2) / (2 * std**2))
    return X, Y, Z


X, Y, Z = generate_2d_gaussian(size=100, mean=0, std=1)

plt.figure(figsize=(6, 5))
plt.contourf(X, Y, Z, cmap='viridis')
plt.colorbar(label='Density')
plt.title('2D Gaussian Distribution (mean=0, std=1)')
plt.xlabel('X')
plt.ylabel('Y')
plt.axis('equal')
plt.show()
