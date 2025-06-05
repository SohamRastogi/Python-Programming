class Student :

    def __init__ (self , name , roll , age) :
        self.name = name
        self.roll = roll
        self.age = age

    def update_name (self , new_name):
        self.name = new_name
        try :
            f = open("ans19.txt" , "a") 
            f.write(f" name updated, now new name is {self.name}")
            f.close()
        except OSError as err :
            print("Error : ", err)
    
    def update_roll (self , new_roll) :
        self.roll = new_roll
        try :
            f = open("ans19.txt" , "a")
            f.write(f" roll number updated, now new roll number is {self.roll}")
            f.close()
        except OSError as err :
            print("Error : ", err)

    def update_age (self , new_age) :
        self.age = new_age
        try :
            f = open("ans19.txt" , "a")
            f.write(f" age updated, now new age is {self.age}")
            f.close()
        except OSError as err :
            print("Error : ", err)
        

s1 = Student("soham" , 1 , 16)
s1.update_name ("Rastogi")
s1.update_roll (106)
s1.update_age (18)

