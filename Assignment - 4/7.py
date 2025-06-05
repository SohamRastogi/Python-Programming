class Student :
    def __init__(self , name , roll) :
        self.name = name
        self.roll = roll

s1 = Student("alpha" , 12)

# let roll condition : must contain only numbers
# let name condition : must contain only alphabets

try :
    if any(char.isdigit() for char in s1.name):
        raise ValueError 
    if any(char.isalpha() for char in repr(s1.roll)):
        raise ValueError
    
except ValueError :
    print("valueError occured")

print(s1.name)
print(s1.roll)



