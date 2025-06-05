import numpy as np

def factorial (n) :
    res = 1
    for i in range(1 , n+1) :
        res = res * i
    return res

list1 = np.random.randint(1,2,10)
list2 = np.random.randint(1,2,10)
list3 = np.random.randint(1,2,10)
list4 = np.random.randint(1,2,10)
list5 = np.random.randint(1,2,10)
list6 = np.random.randint(1,2,10)
list7 = np.random.randint(1,2,10)
list8 = np.random.randint(1,2,10)
list9 = np.random.randint(1,2,10)
list10 = np.random.randint(1,2,10)

sample_array = np.array([list1, list2, list3, list4, list5, list6, list7, list8, list9, list10])
for i in range(0,10) :
    for j in range(0,10) :
        sample_array[i][j] = factorial(i+j) / (factorial(i) * factorial(j))

print("the final required array is : ")
print(sample_array)