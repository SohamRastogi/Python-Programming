m1 = int(input("enter marks of subject 1 : "))
m2 = int(input("enter marks of subject 2 : "))
m3 = int(input("enter marks of subject 3 : "))

sum = m1 + m2 + m3

if(sum / 3 < 40) :
    print("you have failed the exam")
elif (sum / 3 >= 40) :
    if(m1 < 33) :
        print("you have failed the exam")
    if(m2 < 33) :
        print("you have failed the exam")
    if(m3 < 33) :
        print("you have failed the exam")
    elif(m1 >= 33 and m2 >= 33 and m3 >= 33) :
        print("you have passed the exam")
