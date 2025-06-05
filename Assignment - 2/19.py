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


