import numpy as np

def toeplitz_matrix_from_vector(v):
    n = len(v)
    toeplitz = np.empty((n, n), dtype=v.dtype)
    
    for i in range(n):
        toeplitz[i, :i+1] = v[i::-1]          
        toeplitz[i, i+1:] = v[1:n-i]        

    return toeplitz

# let : 
n = 5
v = np.random.randint(1, 10, size=n)
print("Input vector:", v)

T = toeplitz_matrix_from_vector(v)
print("\nToeplitz Matrix:\n", T)
