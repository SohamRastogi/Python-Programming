# let N = 5

dict = {}

# value for key = 1 :
dict1 = {}
for m in range (2,6) :
    for n in range(1,10) :
        if((1*n) % m == 1) :
            dict1.update({m : n})
            break

dict.update({1 : dict1})

# value for key = 2 :
dict2 = {}
for m in range(2,6) :
    for n in range(1,10) :
        if((2*n) % m == 1):
            dict2.update({m : n})
            break
dict.update({2 : dict2})

# value for key = 3 :
dict3 = {}
for m in range(2,6) :
    for n in range(1,10) :
        if((3*n) % m == 1):
            dict3.update({m : n})
            break
dict.update({3 : dict3})

# value for key = 4 :
dict4 = {}
for m in range(2,6) :
    for n in range(1,10) :
        if((4*n) % m == 1):
            dict4.update({m : n})
            break
dict.update({4 : dict4})

# value for key = 5 :
dict5 = {}
for m in range(2,6) :
    for n in range(1,10) :
        if((5*n) % m == 1):
            dict5.update({m : n})
            break
dict.update({5 : dict5})


print(dict)