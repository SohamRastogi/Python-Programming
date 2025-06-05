import numpy as np

a = np.array([[1,2] , [3,4]])
b = np.array([8,18])
ans = np.linalg.solve(a,b)
print(ans)