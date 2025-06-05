m = int(input("enter your marks so that i can determine your grade : "))

if ( m >=90 and m<=100) :
    print("excellent grade")
elif (m>=80 and m<90) :
    print("A grade ")
elif (m >= 70 and m < 80) :
    print("B grade")
elif (m >=60 and m < 70) :
    print("C grade ")
elif (m>= 50 and  m< 60) :
    print("D grade")
elif ( m < 50) :
    print("sorry, you have failed the exam and you will have to repeat the year")