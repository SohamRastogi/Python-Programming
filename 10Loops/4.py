# reverse a string using loops.

str = input("enter a string : ")
x = len(str)
l = []
for i in range(0,x) :
    l.append(str[x-i-1])

print("".join(l))