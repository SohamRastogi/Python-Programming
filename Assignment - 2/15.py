list_moves = [1 , -1 , 1 , 1 , -1]
list_random_walk = [0]

for i in range(0 , len(list_moves)) :
    list_random_walk.append(list_random_walk[i] + list_moves[i])

print(list_random_walk) 