class NoSubclassingMeta(type):  # metaclass -> NoSubclassingMeta
    def __new__(cls, name, bases, class_dict):
        for base in bases:
            if isinstance(base, NoSubclassingMeta): 
                raise TypeError(f"Cannot subclass {base.__name__}")
        return super().__new__(cls, name, bases, class_dict)


class FinalClass(metaclass=NoSubclassingMeta):
    pass


try:
    class SubClass(FinalClass):  
        pass
except TypeError as e:
    print(f"Error: {e}")  
