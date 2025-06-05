a = int(input("enter the first number : "))
b = int(input("enter the second number : "))
c = int(input("eneter the third number : "))

def max () :
    if(a>=b and a>=c) :
        return a
    elif(b>=c and b>=a) :
        return b
    else :
        return c
    
ans = max()
print("the maximum of the 3 entered numbers is : ",ans)