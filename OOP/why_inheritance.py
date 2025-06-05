class coding :
    company = "ITC"

    def __init__(self , name , salary) :
        self.name = name
        self.salary = salary

    def show(self) :
        print(f"the name of the employee is {self.name} and the salary is {self.salary}")

class Programmer :
    company = "ITC Infotech"

    def __init__(self , name , salary , language) :
        self.name = name
        self.salary = salary
        self.language = language

    def show(self) :
        print(f"the name of the employee is {self.name} and the salary is {self.salary}")
    def showLanguage(self) :
        print(f"the name of the employee is {self.name} and he is good with {self.language} language")


a1 = coding("alpha" , 1)
a1.show()

a2 = Programmer("beta" , 2 , "javascript")
a2.show()
a2.showLanguage()



