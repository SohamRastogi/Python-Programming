class Employee :

    company = "ITC"
    def show(self) :
        print(f"the name of the employee is {self.name}, the salary of the employee is {self.salary}")

class Coder :
    language = "python" 

    def printLanguage(self) :
        print("out of all the languages, your language is here : {self.language}")


class Programmer(Employee , Coder):
    
    company = "ITC infotech" 
    
    def showLanguage(self) :
        print(f"the name is {self.name} ans the employee is good at {self.language}")

a = Employee()
b = Programmer()


