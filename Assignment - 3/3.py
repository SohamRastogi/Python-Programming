while True :
    try :
        x = input("enter a number : ")
        if ('.' in x or '-' in x or x == "") : 
            raise ValueError 
        x = int(x)
        break
    except ValueError :
        print("that's an invalid input, please try again")

# i have x as an integer now.

def is_prime(n):
    for i in range(2 , n) :
        if(n % i == 0 ) :
            return False
    return True

def becomes_prime_after_removal(num):
    num_str = str(num)  
    for i in range(len(num_str)):  
        new_num = int(num_str[:i] + num_str[i+1:])  
        if new_num > 0 and is_prime(new_num):  
            return True 
    return False  

print(becomes_prime_after_removal(x))



