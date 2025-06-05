class Student :
    def __init__(self , __name , __age , __roll) : # made all the variable private to this class.
        self.__name = __name
        self.__age = __age
        self.__roll = __roll

s1 = Student("ABC" , 18 , 20)

print(s1.__name)
print(s1.__age)
print(s1.__roll) 
