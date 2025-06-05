class Student  :

    def __init__ (self , __name , __roll , __age) :
        self.__name = __name
        self.__roll = __roll
        self.__age = __age
    
    def get_attribute(self) :
        print("the name of the student is : ", self.__name)
        print("the age of the student is : ", self.__age) 
        print("the roll number of the student is : ", self.__roll)
    
    def set_attribute (self , name_of_student , roll_of_student , age_of_student) :
        self.__name = name_of_student
        self.__roll = roll_of_student
        self.__age = age_of_student

        print("the final values of the attributes after modification are : ")
        print(f"name => {self.__name}")
        print(f"roll => {self.__roll}" )
        print(f"age => {self.__age}")



s1 = Student("soham" , 106 , 18)
s1.get_attribute()
s1.set_attribute("rastogi" , 1 , 10)

