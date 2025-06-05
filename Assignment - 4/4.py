class FixedInstanceSingleton:
    _instances = []  
    _max_instances = 3 # means max of three instances can be created for this class.

    def __new__(cls, *args, **kwargs):
        if len(cls._instances) < cls._max_instances:
            instance = super().__new__(cls)
            cls._instances.append(instance)
        return cls._instances[len(cls._instances) - 1]  

obj1 = FixedInstanceSingleton()
obj2 = FixedInstanceSingleton()
obj3 = FixedInstanceSingleton()
obj4 = FixedInstanceSingleton()  

print(obj1 is obj2)  
print(obj2 is obj3)  
print(obj3 is obj4) 