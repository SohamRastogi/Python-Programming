"""
    1 : snake
    -1 : water
    0 : gun
"""

import random

computer = random.choice([-1 , 0 , 1])

you_str = input("enter a string : ")

dict = {
    's' : 1 ,
    'w' : -1 ,
    'g' : 0
}

you = dict[you_str]

rev_dict = {
    1 : 'snake' ,
    -1 : 'water' ,
    0 : 'gun'
}

print(f"you have chosen : {rev_dict[you]}")
print(f"the computer has chosen : {rev_dict[computer]}")

if(you == computer) :
    print("its a draw")
else :
    if((computer - you) == -1 or (computer - you) == 2) :
        print("you lose")
    else :
        print("you win")
