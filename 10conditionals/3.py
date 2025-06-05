marks = int(input("Enter your marks : "))

if(marks > 100) :
    print("verify your marks again")
    exit()

if(marks >= 90) :
    print("A grade")
elif(marks >=80 and marks < 90) :
    print("B grade")
elif(marks >= 70 and marks < 80) :
    print("C grade")
elif(marks >=60 and marks < 70) :
    print("D grade")
else  :
    print("F grade")