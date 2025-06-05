n = int(input("enter a number : "))


print("*" * n)
for j in  range(1,n-1) :
    print("*",end="")
    print(" " * (n-2) , end="")  # bracket over (n-2) is compulsory ....
    print("*",) 
print("*" * n)
    
# print(" " * 4)
# print("hello ")