import numpy as np


a = np.array([1, 2, 3, 4, 5])
b = np.array([4, 5, 6, 7, 8])

intersection = np.intersect1d(a, b)

union = np.union1d(a, b)

print("Intersection:", intersection)
print("Union:", union)
