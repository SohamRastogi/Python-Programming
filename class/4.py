try :
    raise NameError("HiThere")

    n = input("enter a string : ")

except NameError :
    print("an exception flew by!")

else :
    print(f"{n}")
finally  :
    print("execution complete")

