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
