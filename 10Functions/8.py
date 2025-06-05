n = int(input("enter a number : "))

def factorial(n) :
    if(n==1 or n==0) :
        return 1
    return factorial(n-1) * n

answer = factorial(n)

print(f"the factorial of {n} is {answer}")