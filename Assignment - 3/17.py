import sys

try :
    f = open("ans17.txt" , "r")
except OSError as err :
    print("OS Error : ", err)

list_final = [] 

data = f.readline()
# print(data)

alpha = len(data) - 1
# print(alpha) 

if('@' in data and data[alpha-1] == 'm' and data[alpha-2] == 'o' and data[alpha-3] == 'c' and data[alpha-4] == '.') :
    list_final.append(data)

while (data != "") :
    data = f.readline()
    alpha = len(data) - 1
    if('@' in data and data[alpha-1] == 'm' and data[alpha-2] == 'o' and data[alpha-3] == 'c' and data[alpha-4] == '.') :
        list_final.append(data)

print(list_final) # list of all valid email addresses.



    