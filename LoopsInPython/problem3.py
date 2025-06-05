n = int(input("enter a number : "))

flag = 0

if (n==1) :
    print("the number is neither prime nor composite")
else : 
    for i in range(2,n) : 
        if (n%i == 0) :
            flag =1
            break

    if flag == 1 :
        print("the number is not prime")
    else :
        print("the number is prime ")
