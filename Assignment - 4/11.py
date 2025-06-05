import abc

class grandparent (metaclass=abc.ABCMeta):
    
    @abc.abstractmethod
    def execute(self):
        pass

class parent (grandparent) :
    def execute(self) :
        print("Hello, this is HelloPlugin class")

class child (parent) :
    def execute(self) :
        print("Bye , this was GoodByePlugin class")

h1 = parent().execute()
h2 = child().execute()
