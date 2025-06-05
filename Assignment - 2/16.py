# let n = 10

n = 10

list_final = []

for i in range(1, 11) :
    for j in range(1, 11) :
        for k in range(1, 11) :
            if(i**2 + j**2 == k**2) :
                list_initial = []
                list_initial.append(i)
                list_initial.append(j)
                list_initial.append(k)
                list_final.append(list_initial)

print(list_final)
