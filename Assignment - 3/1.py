import sys

l = []

try :
    f = open("ans1.txt" , "r")
    line = f.readline()
    line = int(line.strip())


except OSError as err :
    print("OSError : ", err)
except ValueError :
    print("issue converting it to int ")

line =  f.readline()

while(line != "") :
    try :
        line = int(line.strip())
        l.append(line)
    except ValueError :
        print("issue converting it to int")
    line = f.readline()

def prime_factors(n):
    factors = []
    i = 2  
    while i * i <= n:  
        while n % i == 0:  
            factors.append(i)
            n //= i  
        i += 1 
    if n > 1:  
        factors.append(n)
    return factors

prime_factor_dict = {num: prime_factors(num) for num in l}

print(prime_factor_dict)



