import numpy as np

def spiral_matrix(n):
    matrix = np.zeros((n, n), dtype=int)
    top, bottom = 0, n - 1
    left, right = 0, n - 1
    num = 1

    while num <= n * n:

        for i in range(left, right + 1):
            matrix[top][i] = num
            num += 1
        top += 1

        for i in range(top, bottom + 1):
            matrix[i][right] = num
            num += 1
        right -= 1

        if top <= bottom:
            for i in range(right, left - 1, -1):
                matrix[bottom][i] = num
                num += 1
            bottom -= 1

       
        if left <= right:
            for i in range(bottom, top - 1, -1):
                matrix[i][left] = num
                num += 1
            left += 1

    return matrix


spiral = spiral_matrix(10)
print("\n")
print("the spiral matrix is : ")
print(spiral)
