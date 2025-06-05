class Programmer :
    name = ""
    salary = 0
    experience = 0

    def __init__(self , name , salary , experience) :
        self.name = name
        self.salary = salary
        self.experience = experience

    def getinfo(self) :
        print(f"the name of the employee is {self.name}, his salary is {self.salary} and his experience is {self.experience}")


    
a1 = Programmer ("a1" , 500000 , 5)
a2 = Programmer ("a2" , 490000 , 4)
a3 = Programmer ("a3" , 600000 , 6)

a1.getinfo()
a2.getinfo()
a3.getinfo()





