def class_factory(class_name, base_classes=(), attributes=None):
    attributes = attributes or {}  
    return type(class_name, base_classes, attributes)  


Person = class_factory("Person", (), {"greet": lambda self: "Hello!"})

p = Person()
print(p.greet())  

Employee = class_factory("Employee", (), {"role": "Software Engineer"})

e = Employee()
print(e.role)  

class Animal:
    def sound(self):
        return "Some generic sound"

Dog = class_factory("Dog", (Animal,), {"bark": lambda self: "Woof!"})

d = Dog()
print(d.sound()) 
print(d.bark())  
