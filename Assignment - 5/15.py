# let the value of 'n' be 3

import numpy as np

list1 = [1,2,3]
list2 = [2,3,4]
list3 = [4,5,6]

sample_array = np.array([list1 , list2 , list3])
print("the original matrix is : ")
print(sample_array)

print("\n")

deter = np.linalg.det(sample_array)
print("the determinant of the matrix is : " , deter)