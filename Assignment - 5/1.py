import numpy as np
from scipy.linalg import schur


A = np.array([[4, 1, -2],
              [1, 2, 0],
              [-2, 0, 3]])


T, Q = schur(A) 

print("the matrix Q is : ")
print(Q)

print("the matrix T is : ")
print(T)

print("the matrix Q inverse is : ")
print(np.linalg.inv(Q))
