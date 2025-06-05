items = ['apple' , 'banana' , 'orange' , 'apple' , 'mango']

count = len(items)

for i in range(0,count) :
    for j in range(0,count) :
        if(items[i] == items[j] and i != j) :
            print(items[i])
            exit()