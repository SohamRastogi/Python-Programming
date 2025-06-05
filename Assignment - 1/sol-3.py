list = []

for i in range(10 , 1001) :
    sum_digit = 0
    alpha = i
    while ( alpha != 0) :
        sum_digit = sum_digit  + int(alpha % 10)
        alpha = alpha / 10
    num_final = sum_digit
    for j in range(1 , num_final + 1) :
        if(j**2 == num_final) :
            list.append(i)


print(list)
