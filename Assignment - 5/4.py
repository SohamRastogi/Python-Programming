import numpy as np
from scipy import sparse

def create_sparse_matrix(rows, cols, density):
   
    total_elements = rows * cols

    non_zero_count = int(total_elements * density)
 
    row_indices = np.random.randint(0, rows, size=non_zero_count)
    col_indices = np.random.randint(0, cols, size=non_zero_count)
    data = np.random.rand(non_zero_count)  

    
    sparse_matrix = sparse.coo_matrix((data, (row_indices, col_indices)), shape=(rows, cols))
    
    return sparse_matrix


rows, cols = 5, 5
density = 0.3 

sparse_mat = create_sparse_matrix(rows, cols, density)
dense_mat = sparse_mat.toarray()  

print("Sparse matrix \n", sparse_mat)
print("\nDense matrix:\n", dense_mat)
