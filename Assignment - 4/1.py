class Student :
    def __init__(self , name , roll , age) :
        self.name = name
        self.roll = roll
        self.age = age
    
s1 = Student ("abcd" , 32 , 18)

print("the name of the student s1 is : ", s1.name)
print("the roll number of the student s1 is : ",s1.roll)
print("the age of the student s1 is : ", s1.age)
