a = int(input("enter a number : "))
b = int(input("enter a number : "))
c = int(input("enter a number : "))
d = int(input("enter a number : "))

if ( a>=b and a>=c and a>=d) :
    print("the greatest number is : ",a)
elif ( b>=a and b>=c and b>=d) :
    print("the greatest number is : ",b)
elif (c>=a and c>=b and c>=d) :
    print("the greatest number is : ",c)
else :
    print("the greatest number is : ",d)