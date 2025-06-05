# adjacency matrix of the graph : 

list = []
list1 = []
list1.append(0)
list1.append(1)
list1.append(1)
list1.append(0)
list1.append(0)

list2 = []
list2.append(1)
list2.append(0)
list2.append(1)
list2.append(1)
list2.append(0)

list3 = []
list3.append(1)
list3.append(1)
list3.append(0)
list3.append(0)
list3.append(1)

list4 = []
list4.append(0)
list4.append(1)
list4.append(0)
list4.append(0)
list4.append(1)

list5 = []
list5.append(0)
list5.append(0)
list5.append(1)
list5.append(1)
list5.append(0)

list.append(list1)
list.append(list2)
list.append(list3)
list.append(list4)
list.append(list5)

dict = {}

l1 = []
for i in range(1,6) :
    if(list[0][i-1] == 1) :
        l1.append(i)
dict.update({1 : l1})

l2 = []
for i in range(1,6) :
    if(list[1][i-1] == 1) :
        l2.append(i)
dict.update({2 : l2})

l3 = []
for i in range(1,6) :
    if(list[2][i-1] == 1) :
        l3.append(i)
dict.update({3 : l3})

l4 = []
for i in range(1,6) :
    if(list[3][i-1] == 1) :
        l4.append(i)
dict.update({4 : l4})

l5 = []
for i in range(1,6) :
    if(list[4][i-1] == 1) :
        l5.append(i)
dict.update({5 : l5})

print(dict) 