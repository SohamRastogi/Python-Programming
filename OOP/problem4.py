import math

class Calculator :

    num = 0

    def __init__(self , number) :
        self.num = number 

    @staticmethod
    def greet() :
        print("hello user")

    def square(self) :
        print("the square of the number is : ", self.num ** 2)
    def cube(self) :
        print("the square of the number is : ",self.num ** 3)
    def square_root(self) :
        print("the square root of the number is : ",math.sqrt(self.num))


 

number = Calculator(10)
number.square()
number.cube()
number.square_root()
number.greet()

# print(number.num)