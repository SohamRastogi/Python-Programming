class Employee :
    language = "python"
    salary = "120000"

    def getinfo(self) :
        print(f"the language is {self.language} and the salary is {self.salary}")
    
    @staticmethod
    def greet() :
        print("good morning ")

harry = Employee()

print(harry.language , harry.salary)

harry.getinfo()

harry.greet()

