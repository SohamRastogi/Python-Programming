pass_word = input("enter the password : ")
x = len(pass_word)

if(x < 6):
    print("weak password")
elif(x >= 6 and x <= 10):
    print("medium password")
else :
    print("strong password")
    



