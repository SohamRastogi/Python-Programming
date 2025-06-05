class Animals :
    def __init__(self) :
        super().__init__()
        print("we are animal's constructors")

class Pets (Animals):

    def __init__(self) :
        super().__init__()
        print("we are the Pet's constructors")

class Dog (Pets) :

    def __init__(self) :
        super().__init__()
        print("we are the dog's class constructors")
    
    def bark(self) :
        print("lets bark common, that's what all we can do ")


D1 = Dog()

D1.bark()
