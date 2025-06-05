while True :
    try :
        l = input("enter a number (start) : ")
        if('.' in l or '-' in l) :
            raise ValueError 
        l = int(l)
        break
    except ValueError:
        print("invalid input, please try again .....")

while True :
    try :
        r = input("enter a number (end) : ")
        if('.' in r or '-' in r) :
            raise ValueError
        r = int(r)
        break
    except ValueError :
        print("invalid input, please try again......")

list_final = []

for i in range(l + 1, r) :
    alpha = 0
    beta = i
    while(beta != 0) :
        alpha = alpha + (beta % 10) ** 3
        beta = beta // 10
    if(alpha == i) :
        list_final.append(i)

print(list_final)

