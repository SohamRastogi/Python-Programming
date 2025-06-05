s1 = {1 , 5 , 3}
s2 = {4 , 2}

list1 = []
list2 = []

x = len(s1)
y = len(s2)

for i in range(1 , x+1) :
    list1.append(s1.pop())

for i in range(1 , y+1) :
    list2.append(s2.pop())

list_final = []

for i in range (0 , x) :
    list_ele = []
    for j in range (0 , y) :
        dict = {}
        dict.update({list1[i] : list2[j]})
        list_ele.append(dict)
    list_final.append(list_ele)

print(list_final)


