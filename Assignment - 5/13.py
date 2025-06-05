import numpy as np

list1 = np.random.randint(1,10,10)
list2 = np.random.randint(1,10,10)
list3 = np.random.randint(1,10,10)
list4 = np.random.randint(1,10,10)
list5 = np.random.randint(1,10,10)
list6 = np.random.randint(1,10,10)
list7 = np.random.randint(1,10,10)
list8 = np.random.randint(1,10,10)
list9 = np.random.randint(1,10,10)
list10 = np.random.randint(1,10,10)

sample_array = np.array([list1 , list2 , list3 , list4 , list5 , list6 , list7 , list8 , list9 , list10])
print("the original matrix is : ")
print("\n")
print(sample_array)

print("\n\n")
print("the unique rows of the original matrix are as follows : ")
print("\n")
unique_rows = np.unique(sample_array , axis = 0)
print(unique_rows)
