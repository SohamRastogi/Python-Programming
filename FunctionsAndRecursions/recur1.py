nums = int(input("enter a number : "))
ans = 1

def factorial (n) :
    if(n==1 or n==0) :
        return 1
    return n*factorial(n-1)

answer=factorial(nums)
print("the factorial of the entered number is : ",answer)