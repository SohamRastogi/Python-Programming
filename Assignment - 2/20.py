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
