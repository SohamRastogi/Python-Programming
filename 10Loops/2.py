# sum even numbers 

n = int(input("enter a number : "))

sum = 0

for i in range(0,n+1):
    if(i%2==0) :
        sum = sum + i
    elif(i%2==1) :
        continue

print(sum)