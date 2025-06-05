str = "sohamrastogi"
a = set()

for i in range(0 , len(str)) :
    for j in range(0 , len(str)) :
        if(str[i] == str[j] and i != j) :
            a.add(str[i : j+1])


print(a)
