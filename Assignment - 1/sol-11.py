sentence = "hello world welcome to python programming"

list = sentence.split(" ")
final_list = []

for i in list :
    flag = 0
    for j in range(0 , len(i)) :
        for k in range(0 , len(i)) :
            if(i[j] == i[k] and j != k) :
                flag = 1
    
    if(flag == 0) :
        final_list.append(i)

max = -1


for str in final_list :
    if(max < len(str)) :
        max = len(str)
        ptr = str


print(f"the required string is : {ptr}")


