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
