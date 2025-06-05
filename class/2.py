try :
    n = int(input("enter a number : "))
    x = 10 / n
except (ZeroDivisionError , ValueError) :
    print("an error occured")
else :
    print(f"the final answer is : {x}")
finally :
    print("execution complete")

