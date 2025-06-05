while True :
    try :
        n = input("enter a number : ")
        if('.' in n or '-' in n) :
            raise ValueError
        n = int(n)
        break
    except ValueError :
        print("invalid input, please try again")

triangular_numbers = [] 
fibonacci_numbers = []

for i in range(0, n+1) :
    number = int(i*(i+1)/2)
    if(number > 100) :
        break
    triangular_numbers.append(number)

a = 1
b = 1
sum = 0

for i in range(0,n+1) :
    fibonacci_numbers.append(sum)
    a = b
    b = sum
    sum = a + b

    if(sum > 100) :
        break

final_common_list = []

for i in triangular_numbers :
    if(i in fibonacci_numbers) :
        final_common_list.append(i) 

print(final_common_list)



