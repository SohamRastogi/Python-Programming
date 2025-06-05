# sol -1
from collections import defaultdict

def prime_factors(n):
    factors = defaultdict(int)
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors[d] += 1
            n //= d
        d = d + 1
    if n > 1:
        factors[n] += 1
    return dict(factors)

N = int(input("Enter N: "))
prime_factor_dict = {i: prime_factors(i) for i in range(1, N + 1)}

print(prime_factor_dict)

# sol -2
list = [[1,2,3] , [2,4,6]]

empty_list = []

for i in list :
    for j in i :
        empty_list.append(j) 

# print(empty_list)

for k in empty_list :
    if (k % 2 == 1) :
        empty_list.remove(k)

# print(empty_list)  
# till now we have obtained all the even numbers in the list.

# exit()

# NOTE :
# for i in range (0 , len(empty_list)) :
#     for j in range (0 , len(empty_list)) :
#         if(empty_list[i] == empty_list[j] and i != j) :
#             empty_list.remove(empty_list[i])

# exit()

final_list = []

for i in empty_list :
    if(i not in final_list) :
        final_list.append(i)

# print(final_list)

sum = 0

for i in final_list :
    sum = sum + i ** 2

print(f"The final answer is : {sum}")


# sol -3
list = []

for i in range(10 , 1001) :
    sum_digit = 0
    alpha = i
    while ( alpha != 0) :
        sum_digit = sum_digit  + int(alpha % 10)
        alpha = alpha / 10
    num_final = sum_digit
    for j in range(1 , num_final + 1) :
        if(j**2 == num_final) :
            list.append(i)


print(list)

# sol -4
str = "sohamrastogi"
a = set()

for i in range(0 , len(str)) :
    for j in range(0 , len(str)) :
        if(str[i] == str[j] and i != j) :
            a.add(str[i : j+1])


print(a)

# sol -5
para = "python is a high level, interpreted programming language known for its simplicity and readability. it supports multiple programming paradigms, including procedural, object-oriented, and functional programming. With a vast ecosystem of libraries"
dict = {'a' : 0 , 'b' : 0 , 'c' : 0 , 'd' : 0 , 'e' : 0 , 'f' : 0 , 'g' : 0 , 'h' : 0 , 'i' : 0 , 'j' : 0 , 'k' : 0 , 'l' : 0 , 'm' : 0 , 'n' : 0 , 'o' : 0 , 'p' : 0 , 'q' : 0 , 'r' : 0 , 's' : 0 , 't' : 0 , 'u' : 0 , 'v' : 0 , 'w' : 0 , 'x' : 0 , 'y' : 0 , 'z' : 0 }

count = 0
for i in range(0 , len(para)) :
    if(para[i] == 'a') :
        count = count + 1
dict.update({'a' : count})

count = 0
for i in range(0 , len(para)) :
    if(para[i] == 'b') :
        count = count + 1
dict.update({'b' : count})

count = 0
for i in range(0 , len(para)) :
    if(para[i] == 'c') :
        count = count + 1
dict.update({'c' : count})

count = 0
for i in range(0 , len(para)) :
    if(para[i] == 'd') :
        count = count + 1
dict.update({'d' : count})

count = 0
for i in range(0 , len(para)) :
    if(para[i] == 'e') :
        count = count + 1
dict.update({'e' : count})

count = 0
for i in range(0 , len(para)) :
    if(para[i] == 'f') :
        count = count + 1
dict.update({'f' : count})

count = 0
for i in range(0 , len(para)) :
    if(para[i] == 'g') :
        count = count + 1
dict.update({'g' : count})

count = 0
for i in range(0 , len(para)) :
    if(para[i] == 'h') :
        count = count + 1
dict.update({'h' : count})

count = 0
for i in range(0 , len(para)) :
    if(para[i] == 'i') :
        count = count + 1
dict.update({'i' : count})

count = 0
for i in range(0 , len(para)) :
    if(para[i] == 'j') :
        count = count + 1
dict.update({'j' : count})

count = 0
for i in range(0 , len(para)) :
    if(para[i] == 'k') :
        count = count + 1
dict.update({'k' : count})

count = 0
for i in range(0 , len(para)) :
    if(para[i] == 'l') :
        count = count + 1
dict.update({'l' : count})

count = 0
for i in range(0 , len(para)) :
    if(para[i] == 'm') :
        count = count + 1
dict.update({'m' : count})

count = 0
for i in range(0 , len(para)) :
    if(para[i] == 'n') :
        count = count + 1
dict.update({'n' : count})

count = 0
for i in range(0 , len(para)) :
    if(para[i] == 'o') :
        count = count + 1
dict.update({'o' : count})

count = 0
for i in range(0 , len(para)) :
    if(para[i] == 'p') :
        count = count + 1
dict.update({'p' : count})

count = 0
for i in range(0 , len(para)) :
    if(para[i] == 'q') :
        count = count + 1
dict.update({'q' : count})

count = 0
for i in range(0 , len(para)) :
    if(para[i] == 'r') :
        count = count + 1
dict.update({'r' : count})

count = 0
for i in range(0 , len(para)) :
    if(para[i] == 's') :
        count = count + 1
dict.update({'s' : count})

count = 0
for i in range(0 , len(para)) :
    if(para[i] == 't') :
        count = count + 1
dict.update({'t' : count})

count = 0
for i in range(0 , len(para)) :
    if(para[i] == 'u') :
        count = count + 1
dict.update({'u' : count})

count = 0
for i in range(0 , len(para)) :
    if(para[i] == 'v') :
        count = count + 1
dict.update({'v' : count})

count = 0
for i in range(0 , len(para)) :
    if(para[i] == 'w') :
        count = count + 1
dict.update({'w' : count})

count = 0
for i in range(0 , len(para)) :
    if(para[i] == 'x') :
        count = count + 1
dict.update({'x' : count})

count = 0
for i in range(0 , len(para)) :
    if(para[i] == 'y') :
        count = count + 1
dict.update({'y' : count})

count = 0
for i in range(0 , len(para)) :
    if(para[i] == 'z') :
        count = count + 1
dict.update({'z' : count})

print(dict)

# sol -6
import itertools

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_generator(N):
    primes = [num for num in range(2, N + 1) if is_prime(num)]
    return itertools.cycle(primes)  

# example :
N = 10
cyclic_primes = prime_generator(N)


for _ in range(20):
    print(next(cyclic_primes), end = " ")

# sol -7
import itertools

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_generator(N):
    primes = [num for num in range(2, N + 1) if is_prime(num)]
    return itertools.cycle(primes)  

# example :
N = 10
cyclic_primes = prime_generator(N)


for _ in range(20):
    print(next(cyclic_primes), end = " ")

# sol -8
# making a list uptill first 100 numbers !!

triangular_numbers = [] 
fibonacci_numbers = []

for i in range(0, 100) :
    number = int(i*(i+1)/2)
    if(number > 100) :
        break
    triangular_numbers.append(number)

a = 1
b = 1
sum = 0

for i in range(0,100) :
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

# sol -9
# str = "soham"

# reversed_helper_list = []

# for i in range (0 , len(str)) :
#     reversed_helper_list.append(str[len(str) - i -1])
# rev_str = "".join(reversed_helper_list)

# print(rev_str)

dict = {}

sentence = "python programming nohtyp code script file edoc elif"

list = sentence.split(" ") 

for i in list :
    reversed_helper_list = []
    for j in range(0 , len(i)) :
        reversed_helper_list.append(i[len(i) - j - 1])
    rev_str = "".join(reversed_helper_list)
    

    if(rev_str) in list :
        dict.update({f"{i}" : f"{rev_str}"})


    unique_dict = {}  
    seen = set()  

    for key, value in dict.items():
        if value not in seen:  
            unique_dict[key] = value
            seen.add(key)
            seen.add(value)  

 
print(unique_dict)

# sol -10
# str = "soham"

# reversed_helper_list = []

# for i in range (0 , len(str)) :
#     reversed_helper_list.append(str[len(str) - i -1])
# rev_str = "".join(reversed_helper_list)

# print(rev_str)

dict = {}

sentence = "python programming nohtyp code script file edoc elif"

list = sentence.split(" ") 

for i in list :
    reversed_helper_list = []
    for j in range(0 , len(i)) :
        reversed_helper_list.append(i[len(i) - j - 1])
    rev_str = "".join(reversed_helper_list)
    

    if(rev_str) in list :
        dict.update({f"{i}" : f"{rev_str}"})


    unique_dict = {}  
    seen = set()  

    for key, value in dict.items():
        if value not in seen:  
            unique_dict[key] = value
            seen.add(key)
            seen.add(value)  

 
print(unique_dict)

# sol -11
sentence = "hello world welcome to python programming"

list = sentence.split(" ")
final_list = []

for i in list :
    flag = 0
    for j in range(0 , len(i)) :
        for k in range(0 , len(i)) :
            if(i[j] == i[k] and j != k) :
                flag = 1
    
    if(flag == 0) :
        final_list.append(i)

max = -1


for str in final_list :
    if(max < len(str)) :
        max = len(str)
        ptr = str


print(f"the required string is : {ptr}")

# sol -12
n = 100  

num_list = []  

for i in range(1, 100):
    if i % 7 == 1:
        num_list.append(i)

final_list = []


for i in num_list:
    if i < 10:  
        final_list.append(i)
    else:
        rev_num = 0
        alpha = i
        while alpha > 0:
            digit = alpha % 10
            rev_num = rev_num * 10 + digit
            alpha = alpha // 10  

        if rev_num == i:
            final_list.append(i)

print(final_list)

# sol -13
def magic_square(n):
    
    square = [[0] * n for _ in range(n)]

    
    i, j = 0, n // 2  

    for num in range(1, n * n + 1):
        square[i][j] = num  
        
        
        new_i, new_j = (i - 1) % n, (j + 1) % n
        

        if square[new_i][new_j]:
            i = (i + 1) % n
        else:
            i, j = new_i, new_j

    return square


N = 3  
magic = magic_square(N)

for row in magic:
    print(row)

# sol -14
m = int(input("enter a number(divisor) : "))
n = int(input("enter a number(key's upperbound) : "))

dict = {}

for i in range(1,n+1) :
    for j in range(1,100) :
        if((i*j) % m == 1) :
            dict.update({f"{i}" : f"{j}"})
            break
        dict.update({f"{i}" : -1})

print(dict)

# sol -15
def isPrime(k) :
    flag = 0
    for i in range(2 , k) :
        if(k % i == 0) :
            flag = 1

    if(flag == 0) :
        return True
    elif (flag == 1) :
        return False 



list_initial = [[1,2,3,4] , [1,2,3,4] , [1,2,3,4] , [1,2,3,4]]

final_list = []
count = 0

for i in list_initial :
    count = count + 1
    for j in range(1 , len(i) + 1) :
        # calculating prime factors for i + j
        sum = j + count
        list = []
        for k in range(2 , sum + 1) :
            if(isPrime(k)) :
                list.append(k)
        sum = 0
        for a in list :
            sum = sum + a
        final_list.append(sum)


print(final_list)
        
# sol -16
n = int(input("enter a number : "))  

num_dict = {i: {"binary": bin(i), "hexadecimal": hex(i)} for i in range(n+1)}


for key, value in num_dict.items():
    print(f"{key}: Binary = {value['binary']}, HexaDecimal = {value['hexadecimal']}")

# sol -17
row_nums = int(input("enter the pascal triangle row number : "))

# that means we have to print the value of 2C0 , 2C1 , 2C2

def factorial (n) :
    product = 1
    for i in range(1, n+1) :
        product = product * i

    return product
def combination(i , j) :
    return factorial(i) // (factorial(j) * factorial(i-j))

list = [] 

for i in range(0,row_nums) :
    list.append( combination (row_nums - 1 , i))


print(list)

# sol -18
# chess-board pattern using nested list comprehension.

final_list = []

for i in range(1,9) :
    list_temp = []
    for j in range(1,9) :
        if( (i+j) % 2 == 0 ) :
            list_temp.append("1")
        elif ( (i+j) % 2 == 1) :
            list_temp.append("0")
    final_list.append(list_temp)
            
for i in final_list :
    print(i) 


# sol -19
def fibonacci(n):
    a, b = 0, 1
    return tuple((a := b, b := a + b)[0] for _ in range(n))  # Comprehension-like

n = int(input("enter a number : "))
print(fibonacci(n))

# sol -20

matrix = [ [1,2,3] , [4,5,6] , [7,8,9] ]

determinant = (matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1])) + (matrix[0][1] * (matrix[1][2] * matrix[2][0] - matrix[1][0] * matrix[2][2])) + (matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0]))

print(determinant)
            





    













