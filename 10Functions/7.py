import random

n = int(input("enter a number : "))

def func(n) :
    while (True) :
        alpha = random.randint(0,n+1)
        if(alpha % 2 == 0):
            return alpha
        elif (alpha %2 == 1) :
            continue


ans = func(n)
print(ans)