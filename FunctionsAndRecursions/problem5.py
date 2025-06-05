n = int(input("enter a number : "))

def pattern(number) :
    for i in range(1,n+1) :
        print("*" * (n-i+1))


pattern(n)