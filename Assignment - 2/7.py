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
