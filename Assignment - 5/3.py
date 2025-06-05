import numpy as np
import math

def factorial_array(arr):
    return np.array([math.factorial(int(i)) if i >= 0 else 1 for i in arr])

def pascal_triangle_matrix(n):
    rows = np.arange(n).reshape(-1, 1)  
    cols = np.arange(n).reshape(1, -1)  

    mask = cols <= rows
    row_vals = rows.flatten()
    col_vals = cols.flatten()
    diff_vals = (rows - cols).flatten()

   
    f_rows = factorial_array(row_vals)
    f_cols = factorial_array(col_vals)
    f_diff = factorial_array(diff_vals)

   
    f_rows = f_rows.reshape(n, 1)
    f_cols = f_cols.reshape(1, n)
    f_diff = f_diff.reshape(n, n)

    triangle = f_rows / (f_cols * f_diff)
    triangle = np.where(mask, triangle, 0)

    return triangle.astype(int)

# let :
n = 6
pascal = pascal_triangle_matrix(n)
print(pascal)
