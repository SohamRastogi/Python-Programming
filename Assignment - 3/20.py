try :
    f = open("ans20.txt" , "r")
except OSError as err :
    print("OS Error : ", err)

list = []

data = f.readline()

flag = 1

if('.' in repr(data) or '-' in repr(data)) :
    flag = 0

if(flag == 1) :
    list.append(data)

data = f.readline()

while(data != "") :
    flag = 1
    if('.' in repr(data) or '-' in repr(data)) :
        flag = 0
    if(flag == 1) :
        list.append(data)
    data = f.readline()


count_list = len(list)

list_final = []

for i in range(0 , count_list) : 
    beta = int(list[i]) 

    sum = 0

    while(beta != 0) :
        sum = sum + beta % 10
        beta = beta // 10
    
    if(i % sum == 0) :
        list_final.append(i) 

print(list_final)
        

