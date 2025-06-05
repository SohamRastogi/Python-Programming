n = 100  

num_list = []  

for i in range(1, 100):
    if i % 7 == 1:
        num_list.append(i)

final_list = []


for i in num_list:
    if i < 10:  
        final_list.append(i)
    else:
        rev_num = 0
        alpha = i
        while alpha > 0:
            digit = alpha % 10
            rev_num = rev_num * 10 + digit
            alpha = alpha // 10  

        if rev_num == i:
            final_list.append(i)

print(final_list)
