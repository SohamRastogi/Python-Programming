class Student :
    def __init__(self , name , roll) :
        self.name = name
        self.roll = roll

s1 = Student("12" , "alpha")

# let roll condition : must contain only numbers
# let name condition : must contain only alphabets

list = []

try :
    if any(char.isdigit() for char in s1.name):
        raise ValueError 
    # if any(char.isalpha() for char in repr(s1.roll)):
    #     raise ValueError
    
except ValueError :
    str1 = "Error : digit present in name"
    list.append(str1)
    
try :
    if any(char.isalpha() for char in repr(s1.roll)):
        raise ValueError
except ValueError :
    str2 = "Error : alphabet present in roll number"
    list.append(str2)

f = open("ans8.txt" , "w")
f.write(repr(list))
f.close()






