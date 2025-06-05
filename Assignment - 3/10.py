list = []

while True :
    try :
        print("enter the data in matrix row - wise")
        list = []
        for i in range(0 , 9) :
            n = input("enter a number : ")
            if('.' in n or '-' in n) :
                raise ValueError
            n = int(n)
            list.append(n)
        break
    
    except ValueError : 
        print("invalid input, try again") 

try : 
    determinant = list[0] * (list[4]*list[8] - list[7]*list[5]) + list[1] * (list[5]*list[6] - list[3]*list[8]) + list[2] * (list[3]*list[7] - list[4]*list[6])
    if(determinant == 0) :
        raise Exception 
except Exception :
    print("singular matrix error occured")


print(determinant)


