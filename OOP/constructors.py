class Employee :
    language = "python"
    salary = 120000

    def __init__(self) :
        print("i am creating an object")

    def getinfo(self) :
        print(f"the language is {self.language} and the salary is {self.salary}")

    @staticmethod
    def greet() :
        print("good morning sir")

harry = Employee()

harry.getinfo()  
harry.greet()


