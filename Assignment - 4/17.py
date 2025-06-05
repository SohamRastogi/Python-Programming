class LimitedInstances:
    _instance_count = 0  
    _max_instances = 3   

    def __new__(cls, *args, **kwargs):
        if cls._instance_count >= cls._max_instances:
            raise Exception(f"Cannot create more than {cls._max_instances} instances of {cls.__name__}")
        
        instance = super().__new__(cls)  
        cls._instance_count += 1  
        return instance 

    def __del__(self):
        type(self)._instance_count -= 1

obj1 = LimitedInstances()
obj2 = LimitedInstances()
obj3 = LimitedInstances()

try:
    obj4 = LimitedInstances()  
except Exception as e:
    print(f"Error: {e}")
