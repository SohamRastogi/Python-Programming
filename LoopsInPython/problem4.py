# sum of n natural numbers using while loop

n = int(input("enter a number : "))

sum = 0

while ( n >= 0) :
    sum = sum + n
    n = n-1

print("the answer of the problem is : ",sum)