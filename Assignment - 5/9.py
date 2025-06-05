import numpy as np
from scipy.spatial import ConvexHull
import matplotlib.pyplot as plt


points = np.random.rand(10, 2)  

hull = ConvexHull(points)

print("Hull vertex indices:", hull.vertices)
print("Hull points:\n", points[hull.vertices])


plt.plot(points[:, 0], points[:, 1], 'o') 

for simplex in hull.simplices:
    plt.plot(points[simplex, 0], points[simplex, 1], 'k-')  

plt.fill(points[hull.vertices, 0], points[hull.vertices, 1], 'lightblue', alpha=0.3)
plt.title("Convex Hull")
plt.show()
