import numpy as np

mat = np.array([[1,2,3,4] , [2,4,6,8] , [1,4,6,7] , [4,6,8,2]])

n = int(input("enter the power that is raised to the matrix : "))

answer_array = np.linalg.matrix_power(mat , n)
print("the power raised matrix is : ")
print(answer_array)