# snake water gun game : 

import random

"""
    1 : snake
    -1 : water
    0 : gun
"""

#computer = 1 : but we need to generate a random number for computer 
computer = random.choice([-1,0,1])
str_user = input("enter your preferred choice (s/w/g) : ")
dict = {
    's' : 1 ,
    'w' : -1 ,
    'g' : 0
}

you = dict[str_user]

reverse_dict = {
    1 : 'snake' ,
    -1 : 'water' ,
    0 : 'gun' 
}

# print(f"{you}")
# print(f"{computer}")
# print(reverse_dict[you])

print(f"you chose {reverse_dict[you]}")
print(f"the computer chose {reverse_dict[computer]}")

if (computer == you) :
    print("its a draw ")
else : 

    if(computer == -1 and you == 1) :
        print("you win")
    elif(computer == -1 and you == 0) :
         print("you lose")
    elif(computer == 1 and you == -1) :
        print("you lose")
    elif(computer == 1 and you == 0) :
        print("you win")
    elif(computer == 0 and you == 1) :
        print("you win")
    elif(computer == 0 and you == -1) :
        print("you lose")
    else :
        print("somethingwent wrong")

