def isPrime(k) :
    flag = 0
    for i in range(2 , k) :
        if(k % i == 0) :
            flag = 1

    if(flag == 0) :
        return True
    elif (flag == 1) :
        return False 



list_initial = [[1,2,3,4] , [1,2,3,4] , [1,2,3,4] , [1,2,3,4]]

final_list = []
count = 0

for i in list_initial :
    count = count + 1
    for j in range(1 , len(i) + 1) :
        # calculating prime factors for i + j
        sum = j + count
        list = []
        for k in range(2 , sum + 1) :
            if(isPrime(k)) :
                list.append(k)
        sum = 0
        for a in list :
            sum = sum + a
        final_list.append(sum)


print(final_list)
        
        
            





    
