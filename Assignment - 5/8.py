import numpy as np

def cyclic_permutation_matrix(base_row):
    n = len(base_row)
    matrix = np.zeros((n, n), dtype=int)
    
    for i in range(n):
        matrix[i] = np.roll(base_row, -i) 

    return matrix


base = np.array([1, 2, 3, 4])
result = cyclic_permutation_matrix(base)
print(result)
