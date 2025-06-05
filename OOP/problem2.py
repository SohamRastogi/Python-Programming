import math

class Calculator :
    number = 0

    def __init__(self,number) :
        self.number = number
    def square(self) :
        print("the square of the number is : ",self.number ** 2)
    def cube(self) :
        print("the cube of the number is : ",self.number ** 3)
    def square_root(self) :
        print("the square root of the number is : ", math.sqrt(self.number) )



n1 = Calculator(10)
n1.square()
n1.cube()
n1.square_root()
