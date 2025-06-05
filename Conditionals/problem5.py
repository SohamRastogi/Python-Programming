list = []
name = input("enter your name : ")
list.append(name)

name = input("enter your name : ")
list.append(name)

name = input("enter your name : ")
list.append(name)

name = input("enter your name : ")
list.append(name)

target = input("enter name to be searched in a list : ")

# flag  = 0
# if(list[0] == target) :
#     flag = 1

# if(list[1] == target) :
#     flag = 2

# if(list[2] == target) :
#     flag = 3

# if(list[3] == target) :
#     flag = 4

# if (flag != 0) :
#     print("name is found in the list")
# else :
#     print("name is not found in the list")

if (target in list) :
    print("name is present in the list")
else :
    print("name is not present in the list")