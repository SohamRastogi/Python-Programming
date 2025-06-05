import numpy as np

# constructing the matrix :
list1 = [1,2,3,4]
list2 = [4,3,2,1]
list3 = [4,5,7,8]
list4 = [4,6,7,8]

sample_array = np.array([list1 , list2 , list3 , list4])

determinant = np.linalg.det(sample_array)

print("the determinant of the matrix is : ")
print(determinant)

if(determinant == 0) :
    print("since the determinant of the matrix is 0, the inverse of the matrix is not defined")

if (determinant != 0) :
    print("the inverse of the matrix is : ")
    inverse_mat = np.linalg.inv(sample_array)
    print(inverse_mat)
