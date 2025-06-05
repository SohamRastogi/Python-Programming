# chess-board pattern using nested list comprehension.

final_list = []

for i in range(1,9) :
    list_temp = []
    for j in range(1,9) :
        if( (i+j) % 2 == 0 ) :
            list_temp.append("1")
        elif ( (i+j) % 2 == 1) :
            list_temp.append("0")
    final_list.append(list_temp)
            
for i in final_list :
    print(i) 

