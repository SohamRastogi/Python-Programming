class coding :
    company = "ITC"

    def __init__(self , name , salary) :
        self.name = name
        self.salary = salary

    def show(self) :
        print(f"the name of the employee is {self.name} and the salary is {self.salary}")
    
a1 = coding("alpha" , 1)
# a1.show()

class programmer (coding) :
    comapy = "ITC infotech" 

    def __init__(self , name , salary , language) :
        self.name = name
        self.salary = salary
        self.language = language

    def show_language (self) :
        print(f"the name of the employee is {self.name} and he is good in {self.language} language")


p1 = programmer("beta" , 2 , "python")
p1.show()