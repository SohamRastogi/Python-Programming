class Employee :
    salary = 120000
    language = "Python"

    def getinfo(self):
        print(f"the language is {self.language} and the salary is {self.salary}")
    def greet(self) :
        print("good morning harry")
        


harry = Employee()
harry.language = "java script"
harry.getinfo()

harry.greet()


