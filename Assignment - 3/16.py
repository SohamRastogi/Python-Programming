try  :
    f = open("ans16.txt" , "r")
except OSError as err:
    print("OS error : ", err)

data = f.readline()

list = []

while (data != "") :
    try :
        if('.' in data or '-' in data) :
            raise ValueError
        data = int(data)
        list.append(data)
        data = f.readline()

    except ValueError :
        print("invalid input for computation")
        data = f.readline()


happy_list = []

counter = len(list)

for i in range(0 , counter) : 
    flag = 0
    x = list[i] 
    count = 0
    while (x != 1) :
        count = count + 1
        if(count > 100):
            flag = 1
            break
        beta = 0
        while(x != 0) :
            beta = beta + (x % 10) ** 2
            x = x // 10
        x = beta
    if(flag == 0) :
        happy_list.append(list[i]) 

print(happy_list)
        
        
