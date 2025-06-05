input_str = "teeter"

count = len(input_str)

for i in range (0 , count) :
    flag = 0
    for j in range(0 , count) :
        if(input_str[i] == input_str[j] and i != j) :
            flag = 1
    if(flag == 0) :
        print(input_str[i])

