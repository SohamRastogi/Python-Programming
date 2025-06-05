# can keep a counter variable in the constructor, when the constructor is called, count++. at the count, count gives us the number of instances.

def instance_tracker(cls):
    cls._instance_count = 0 

    original_init = cls.__init__  

   
    def new_init(self, param1, param2):  
        cls._instance_count += 1 
        original_init(self, param1, param2) 

    cls.__init__ = new_init  

   
    @classmethod
    def get_instance_count(cls):
        return cls._instance_count

    cls.get_instance_count = get_instance_count 
    return cls


@instance_tracker
class MyClass:
    def __init__(self, x, y): 
        self.x = x
        self.y = y


obj1 = MyClass(1, 2)
obj2 = MyClass(3, 4)

print(MyClass.get_instance_count())
