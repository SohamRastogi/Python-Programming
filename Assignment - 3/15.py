while True : 
    try :
        r = input("enter a number : ")
        if('.' in r or '-' in r ) :
            raise ValueError
        r = int(r)
        break
    except ValueError :
        print("invalid input, please try again.... ")




# x^2 + y^2 + z^2 = R^2
list = []

for i in range (-r , r +1) :
    for j in range(-r , r+1) :
        for k in range(-r , r+1) :
            if(i**2 + j**2 + k**2 <= r**2) :
                list_initial = []
                list_initial.append(i)
                list_initial.append(j)
                list_initial.append(k)
                try  :
                    list.append(list_initial)
                except MemoryError :
                    print("Memory Error : Not enough memory available.")
                


alpha = tuple(list)
print(alpha)
