import matplotlib.pyplot as plt
import numpy as np

# Sample 2D data
data = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

# Create the heatmap
plt.imshow(data, cmap='hot', interpolation = "nearest")
plt.colorbar()  # Show color scale
plt.title("Heat Map Example")
plt.show()