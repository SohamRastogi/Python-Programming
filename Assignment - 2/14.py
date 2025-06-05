# let the radius be 3
r = 3

# x^2 + y^2 + z^2 = R^2
list = []

for i in range (-r , r +1) :
    for j in range(-r , r+1) :
        for k in range(-r , r+1) :
            if(i**2 + j**2 + k**2 <= r**2) :
                list_initial = []
                list_initial.append(i)
                list_initial.append(j)
                list_initial.append(k)
                list.append(list_initial)

alpha = tuple(list)
print(alpha)
