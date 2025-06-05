n = int(input("enter a number : "))

if(n == 1) :
    print("the entered number is neither prime nor composite ")
    exit()

if(n==2) :
    print("the entered number is prime")
    exit()

flag = 0

for i in range(2,n) :
    if(n % i == 0) :
        flag = 1
        break
    
if(flag == 0) :
    print("the entered number is prime")

elif(flag == 1) :
    print("the entered number is composite")

