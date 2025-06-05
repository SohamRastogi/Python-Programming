class Employee :
    name = "abcd"
    language = "python"
    salary = 120000

    def __init__(self , name , language  , salary) :
        self.name = name
        self.language = language
        self.salary = salary

harry = Employee("harry" , "javascript" , 140000)

print(harry.name , harry.language , harry.salary)




