while True :
    try :
        n = input("enter a number : ")
        if('.' in n or '-' in n) :
            raise ValueError 
        n = int(n)
        break
    except ValueError :
        print("invalid input, please try again")

try :
    f = open("ans6.txt" , "r")
except OSError as err :
    print("OS Error : " , err)

data = f.read()

f.close()

counter = len(data)

list_final = []

for i in range(0 , counter - 5) :
    l = []
    for j in range(0 , 6) :
        l.append(data[i+j])
    list_final.append(l)

try : 
    f = open("ans6_ouput.txt" , "w") 
except OSError as err :
    print("Os error : ",err)

f.write(repr(list_final))
f.close()  






