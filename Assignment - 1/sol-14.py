m = int(input("enter a number(divisor) : "))
n = int(input("enter a number(key's upperbound) : "))

dict = {}

for i in range(1,n+1) :
    for j in range(1,100) :
        if((i*j) % m == 1) :
            dict.update({f"{i}" : f"{j}"})
            break
        dict.update({f"{i}" : -1})

print(dict)