while True :
    try : 
        x = int(input("enter a number : "))
        break
    except ValueError:
        print("invalid input, please try again")

list = []
list.append(x)

if x == 1 or x == 0 :
    print("cycle has been detected")


while (x != 1 or x != 0) :
    alpha = 0

    while(x != 0) :
        alpha = alpha + (x%10) ** 2
        x = x // 10
    
    x = alpha
    list.append(x)

    if (x == 1 or x == 0) : 
        break

delta = len(list)

try :
    f = open("ans2.txt" ,"w")
    f.write(repr(delta))
except OSError as err :
    print("OSError : ",err)