# overflow of integer issues automatically handled in python as python has dynamic integer flow, it is a number powerful programming language

while True :
    try :
        n = input("Enter a number : ")
        if('.' in n or '-' in n) : 
            raise ValueError
        n = int(n)
        break
    except ValueError :
        print("invalid input, please try again.... ")

def function_listing() :
    list_final.append(list)

list_final = []

for i in range (1 , n+1) :
    
    for j in range(1 , n + 1) :
        for k in range(1 , n+1) :
            list = []
            flag = 0
            if(j**2 + k**2 == i**2) :
                list.append(i)
                list.append(k)
                list.append(j)
                flag = 1
                function_listing()
                break
                
        

print(list_final)
