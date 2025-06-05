while True :
    try : 
        n = input("enter a number : ")
        if('.' in n or '-' in n) :
            raise ValueError 
        n = int(n)
        if(n <=1) :
            raise ValueError
        break
    except ValueError :
        print("invalid input, please try again..")

while True : 
    try : 
        k = input("enter a number : ")
        if('.' in k or '-' in k) :
            raise ValueError
        k = int(k)
        break
    except ValueError :
        print("invalid input, please try again")


def is_prime(nums) :
    for i in range(2 , nums ):
        if(nums % i == 0) :
            return False
    return True

count = 0

for i in range(2,  n+1) :
    list = [] 
    for j in range(2 , i+1) :
        if(is_prime(j) and i % j ==0 ) :
            list.append(j)
    if(len(list) == k) :
        count = count + 1

        
print(count)




