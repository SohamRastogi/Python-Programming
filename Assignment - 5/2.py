import numpy as np

list1 = [1,2,3,4]
list2 = [2,4,6,8]
list3 = [1,3,4,6]
list4 = [4,5,6,7]

final_array = np.array([list1 , list2 , list3 , list4])
eigen_values = np.linalg.eigvals(final_array)

print("the eigen values of the matrix are : ")
print(eigen_values)
