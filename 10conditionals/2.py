age = int(input("enter your age : "))
day = input("enter the day of the week : ")
day_final = day.lower()

if (age >= 18 and day_final == 'wednesday') :
    print("the price of the ticket is dollar 12 - dollar 2 which is 10 dolllars only")
elif (age >= 18 and day_final != 'wednesday') :
    print("the price of the ticket is dollar 12 only")
elif (age < 18 and day_final == 'wednesday') :
    print("the price of the ticket is dollar 8 - dollar 2 which is 6 dollars only")
elif (age < 18 and day != 'wednesday') :
    print("the price of the ticket is 8 dollars only")

    
