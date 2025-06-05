import numpy as np

list1 = [1,2,4,5]
list2 = [4,6,7,8]
list3 = [2,4,5,6]
list4 = [6,7,8,9]

list5 = [2,3,4,8]
list6 = [6,5,7,8]
list7 = [1,4,5,6]
list8 = [8,6,4,9]

mat1 = np.array([list1 , list2 , list3 , list4])
mat2 = np.array([list5 , list6 , list7 , list8])

ans_matrix = np.multiply(mat1 , mat2)
print("the element wise multiplication of two matrixes (mat1 and mat2) is the following matrix : ")
print(ans_matrix)
