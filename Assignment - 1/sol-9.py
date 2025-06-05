# str = "soham"

# reversed_helper_list = []

# for i in range (0 , len(str)) :
#     reversed_helper_list.append(str[len(str) - i -1])
# rev_str = "".join(reversed_helper_list)

# print(rev_str)

dict = {}

sentence = "python programming nohtyp code script file edoc elif"

list = sentence.split(" ") 

for i in list :
    reversed_helper_list = []
    for j in range(0 , len(i)) :
        reversed_helper_list.append(i[len(i) - j - 1])
    rev_str = "".join(reversed_helper_list)
    

    if(rev_str) in list :
        dict.update({f"{i}" : f"{rev_str}"})


    unique_dict = {}  
    seen = set()  

    for key, value in dict.items():
        if value not in seen:  
            unique_dict[key] = value
            seen.add(key)
            seen.add(value)  

 
print(unique_dict)