while True :
    try :
        n = input("enter a number : ")

        if('.' in n or '-' in n) :
            raise ValueError
        n = int(n)
        if(n <=1) :
            raise ValueError
        break
    except ValueError :
        print("that's invalid input, please try again")
    except ZeroDivisionError as err:
        print("error occured : ",err)

# now i have an integer 'n' whose value is greater than 1.

dict_final= {}

dict1 = {}
dict1.update({1 : -1})

dict_final.update(dict1)

dict2 = {}
dict2.update({2 : -1})
dict_final.update(dict2)



for i in range(3 , n + 1) :
    
    dict = []

    for j in range(2 , i + 1) :
        flag = 0
        for k in range(1, 100) :
            if((i * k) % j == 1) :
                flag = 1
                dict.append({i : k})
                break
        if(flag == 0) :
            dict.append({i : -1})
    
    
    
    dict_final[i] = dict

print(dict_final)
                




