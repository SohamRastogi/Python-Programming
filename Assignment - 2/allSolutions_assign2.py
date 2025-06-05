# sol - 1

def unique_char_count(paragraph):
    word_map = {}
    words = paragraph.lower().split()
    
    for word in words:
        word_map[word] = len(set(word)) 
    
    return word_map

paragraph = "This is a simple test Testing unique character count"
print(unique_char_count(paragraph))

# sol - 2

# let N = 5

dict = {}

# value for key = 1 :
dict1 = {}
for m in range (2,6) :
    for n in range(1,10) :
        if((1*n) % m == 1) :
            dict1.update({m : n})
            break

dict.update({1 : dict1})

# value for key = 2 :
dict2 = {}
for m in range(2,6) :
    for n in range(1,10) :
        if((2*n) % m == 1):
            dict2.update({m : n})
            break
dict.update({2 : dict2})

# value for key = 3 :
dict3 = {}
for m in range(2,6) :
    for n in range(1,10) :
        if((3*n) % m == 1):
            dict3.update({m : n})
            break
dict.update({3 : dict3})

# value for key = 4 :
dict4 = {}
for m in range(2,6) :
    for n in range(1,10) :
        if((4*n) % m == 1):
            dict4.update({m : n})
            break
dict.update({4 : dict4})

# value for key = 5 :
dict5 = {}
for m in range(2,6) :
    for n in range(1,10) :
        if((5*n) % m == 1):
            dict5.update({m : n})
            break
dict.update({5 : dict5})


print(dict)

# sol - 3

# adjacency matrix of the graph : 

list = []
list1 = []
list1.append(0)
list1.append(1)
list1.append(1)
list1.append(0)
list1.append(0)

list2 = []
list2.append(1)
list2.append(0)
list2.append(1)
list2.append(1)
list2.append(0)

list3 = []
list3.append(1)
list3.append(1)
list3.append(0)
list3.append(0)
list3.append(1)

list4 = []
list4.append(0)
list4.append(1)
list4.append(0)
list4.append(0)
list4.append(1)

list5 = []
list5.append(0)
list5.append(0)
list5.append(1)
list5.append(1)
list5.append(0)

list.append(list1)
list.append(list2)
list.append(list3)
list.append(list4)
list.append(list5)

dict = {}

l1 = []
for i in range(1,6) :
    if(list[0][i-1] == 1) :
        l1.append(i)
dict.update({1 : l1})

l2 = []
for i in range(1,6) :
    if(list[1][i-1] == 1) :
        l2.append(i)
dict.update({2 : l2})

l3 = []
for i in range(1,6) :
    if(list[2][i-1] == 1) :
        l3.append(i)
dict.update({3 : l3})

l4 = []
for i in range(1,6) :
    if(list[3][i-1] == 1) :
        l4.append(i)
dict.update({4 : l4})

l5 = []
for i in range(1,6) :
    if(list[4][i-1] == 1) :
        l5.append(i)
dict.update({5 : l5})

print(dict) 

# sol - 4

s1 = {1 , 5 , 3}
s2 = {4 , 2}

list1 = []
list2 = []

x = len(s1)
y = len(s2)

for i in range(1 , x+1) :
    list1.append(s1.pop())

for i in range(1 , y+1) :
    list2.append(s2.pop())

list_final = []

for i in range (0 , x) :
    list_ele = []
    for j in range (0 , y) :
        dict = {}
        dict.update({list1[i] : list2[j]})
        list_ele.append(dict)
    list_final.append(list_ele)

print(list_final)


# sol - 5

def ipv4_generator():
    return (
        f"{a}.{b}.{c}.{d}"
        for a in range(256)
        for b in range(256)
        for c in range(256)
        for d in range(256)
    )

gen = ipv4_generator()
for _ in range(10): # first 10 ipv4 addresses.
    print(next(gen))

# sol - 6

def sieve_of_eratosthenes(n):
    primes = {x for x in range(2, n+1)}
    for i in range(2, int(n**0.5) + 1):
        if i in primes:
            primes -= {i * j for j in range(i, (n // i) + 1)}
    return primes

# let value of N = 100
N = 100
print(sieve_of_eratosthenes(N))


# sol - 7

import numpy as np

def construct_tensor(N):
    # Step 1: Initialize a random N x N x N tensor
    T = np.random.randint(1, 10, (N, N, N))  # Values between 1 and 9 for clarity
    
    # Step 2: Create an empty tensor to store determinants
    det_tensor = np.zeros((N-1, N-1, N))  # (N-1) x (N-1) x N because we need valid neighbors

    # Step 3: Compute determinants
    for i in range(N-1):  # Avoid last row
        for j in range(N-1):  # Avoid last column
            for k in range(N):  # Use all depths
                # Construct 2x2 matrix from neighboring indices
                M = np.array([
                    [T[i][j][k], T[i+1][j][k]], 
                    [T[i][j+1][k], T[i+1][j+1][k]]
                ])
                # Compute determinant
                det_tensor[i][j][k] = np.linalg.det(M)

    return T, det_tensor

# Example Usage
N = 4  # Set size of tensor
original_tensor, determinant_tensor = construct_tensor(N)

print("Original Tensor:")
print(original_tensor)

print("\nDeterminant Tensor:")
print(determinant_tensor)

# sol - 8

import hashlib 

sentence = "welcome to Python Programming it is a very easy to learn language"

list = sentence.split(" ")

list_encoded = []

for i in list :
    hash_value = hashlib.sha256(i.encode()).hexdigest()
    list_encoded.append(hash_value)

print(list_encoded)


# sol - 9

def generate_bsp_fractal(start, end, depth):

    if depth == 0:
        return [(start, end)]  

  
    one_third = start + (end - start) / 3
    two_third = start + 2 * (end - start) / 3


    left_part = generate_bsp_fractal(start, one_third, depth - 1)
    right_part = generate_bsp_fractal(two_third, end, depth - 1)

    return left_part + right_part  


# let :
depth = 3  
bsp_sequence = generate_bsp_fractal(0, 1, depth)

print("Binary Space Partitioning Sequence (Fractal-Based):")
for segment in bsp_sequence:
    print(segment)


# sol - 10

def get_factors(n):
    return tuple(i for i in range(1, n + 1) if n % i == 0)

numbers = range(1, 11) # let n = 10

factors_dict = {num: get_factors(num) for num in numbers}


print(factors_dict)

# sol - 11

def is_uniform(grid):
    first_value = grid[0][0]
    return all(cell == first_value for row in grid for cell in row)

def quadtree(grid):
    """Recursively constructs a quadtree representation of an image grid."""
    n = len(grid)  
    
   
    if is_uniform(grid):
        return grid[0][0]
    
    mid = n // 2  
    top_left = [row[:mid] for row in grid[:mid]]  
    top_right = [row[mid:] for row in grid[:mid]]  
    bottom_left = [row[:mid] for row in grid[mid:]]  
    bottom_right = [row[mid:] for row in grid[mid:]]  #

   
    return {
        "top_left": quadtree(top_left),
        "top_right": quadtree(top_right),
        "bottom_left": quadtree(bottom_left),
        "bottom_right": quadtree(bottom_right),
    }

# let 
image = [
    [1, 1, 2, 2],
    [1, 1, 2, 2],
    [3, 3, 4, 4],
    [3, 3, 4, 4]
]

quadtree_dict = quadtree(image)
print(quadtree_dict)

# sol - 12

from itertools import product

def check_winner(board, player):
    """Check if a given player ('O' or 'X') has won the board."""
    winning_positions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8), 
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  
        (0, 4, 8), (2, 4, 6) 
    ]
    return any(all(board[i] == player for i in line) for line in winning_positions)

def is_valid_board(board):
    """Check if the given board state is valid."""
    count_O = board.count('O')
    count_X = board.count('X')

    
    if not (count_O == count_X or count_O == count_X + 1):
        return False

   
    O_wins = check_winner(board, 'O')
    X_wins = check_winner(board, 'X')

    if O_wins and X_wins:
        return False

    if O_wins and count_O == count_X:  
        return False
    if X_wins and count_O > count_X:  
        return False

    return True

def rotate_90(board):
    """Rotate a Tic-Tac-Toe board 90 degrees clockwise."""
    return [
        board[6], board[3], board[0],
        board[7], board[4], board[1],
        board[8], board[5], board[2]
    ]

def get_canonical_form(board):
    
    board_variants = [board]
    
    for _ in range(3):
        board = rotate_90(board)
        board_variants.append(board)
    
    return min(board_variants)

def generate_valid_boards():
   
    valid_boards = set()
    
    for board_tuple in product(['O', 'X', '_'], repeat=9):
        board = list(board_tuple)

        if is_valid_board(board):
            canonical_board = tuple(get_canonical_form(board))
            valid_boards.add(canonical_board)

    return valid_boards

valid_board_states = generate_valid_boards()

print(f"Total valid unique Tic-Tac-Toe board states (ignoring rotations): {len(valid_board_states)}")



# sol - 13

def fibo(n) :
   
    fib_list = []

    a = 1
    b = 1
    sum = 0
    for i in range(1,n+1) :
      a = b
      b = sum
      sum = a+b
      fib_list.append(sum)
    
    return tuple(fib_list)
    

alpha = fibo(10)
print (alpha)

# sol - 14

# let the radius be 3
r = 3

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
                list.append(list_initial)

alpha = tuple(list)
print(alpha)


# sol - 15

list_moves = [1 , -1 , 1 , 1 , -1]
list_random_walk = [0]

for i in range(0 , len(list_moves)) :
    list_random_walk.append(list_random_walk[i] + list_moves[i])

print(list_random_walk) 

# sol - 16

# let n = 10

n = 10

list_final = []

for i in range(1, 11) :
    for j in range(1, 11) :
        for k in range(1, 11) :
            if(i**2 + j**2 == k**2) :
                list_initial = []
                list_initial.append(i)
                list_initial.append(j)
                list_initial.append(k)
                list_final.append(list_initial)

print(list_final)

# sol - 17

from math import gcd

def coprime_dict(N):
    return {n: {m for m in range(1, N+1) if gcd(n, m) == 1} for n in range(1, N+1)}

# let N = 10
N = 10
result = coprime_dict(N)
print(result)


# sol - 18

def latin_hypercube(N):
    return [
        [[(i + j + k) % N + 1 for k in range(N)] for j in range(N)]
        for i in range(N)
    ]

# let N = 3 
N = 3  
hypercube = latin_hypercube(N)


for layer in hypercube:
    for row in layer:
        print(row)
    print() 


# sol - 19

import numpy as np

def generate_semi_magic_square(N):
    while True:
        numbers = np.arange(1, N*N + 1)
        np.random.shuffle(numbers)
        square = numbers.reshape(N, N)
        
        
        row_sums = np.sum(square, axis=1)
        col_sums = np.sum(square, axis=0)
        
       
        if np.all(row_sums == row_sums[0]) and np.all(col_sums == col_sums[0]):
            return square

# let N = 3
N = 3  
semi_magic_square = generate_semi_magic_square(N)

print("Generated Semi-Magic Square:")
print(semi_magic_square)


# sol - 20

import numpy as np
from sympy import factorint

def sum_of_prime_factors(n):
    return sum(factorint(n).keys()) if n > 1 else 0  

def generate_4d_tensor(shape):
    tensor = np.zeros(shape, dtype=int)
    
    for i in range(shape[0]):
        for j in range(shape[1]):
            for k in range(shape[2]):
                for l in range(shape[3]):
                    tensor[i, j, k, l] = (sum_of_prime_factors(i) + 
                                          sum_of_prime_factors(j) + 
                                          sum_of_prime_factors(k) + 
                                          sum_of_prime_factors(l))
    return tensor

shape = (3, 3, 3, 3)  
tensor = generate_4d_tensor(shape)

print("Generated 4D Tensor:")
print(tensor)
