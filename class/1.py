try:
    n = int(input("enter a number : "))
    res = 100 / n
except ZeroDivisionError :
    print("you cant divide by zero")

except ValueError :
    print("Enter a valid number ")
else :
    print(f"result is : {res}")
finally :
    print("execution complete")