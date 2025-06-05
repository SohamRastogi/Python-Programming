list = [[1,2,3] , [2,4,6]]

empty_list = []

for i in list :
    for j in i :
        empty_list.append(j) 

# print(empty_list)

for k in empty_list :
    if (k % 2 == 1) :
        empty_list.remove(k)

# print(empty_list)  
# till now we have obtained all the even numbers in the list.

# exit()

# NOTE :
# for i in range (0 , len(empty_list)) :
#     for j in range (0 , len(empty_list)) :
#         if(empty_list[i] == empty_list[j] and i != j) :
#             empty_list.remove(empty_list[i])

# exit()

final_list = []

for i in empty_list :
    if(i not in final_list) :
        final_list.append(i)

# print(final_list)

sum = 0

for i in final_list :
    sum = sum + i ** 2

print(f"The final answer is : {sum}")


