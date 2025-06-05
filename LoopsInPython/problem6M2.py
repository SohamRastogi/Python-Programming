# method 2 :

n = int(input("enter a number : "))

for i in range(1,n+1) : 
    for j in range(0,n-i+1) :
        print(" ",end="")
    for k in range(0,2*i-1) :
        print("*",end="")
    print("\n")
