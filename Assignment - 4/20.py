class LoggedInt:
    def __init__(self, value):
        if not isinstance(value, int):  
            raise TypeError("LoggedInt only supports integer values.")
        self.value = value  

    def __repr__(self):
        return f"LoggedInt({self.value})"  

    def log(self, operation, other, result):
        print(f"LOG: {self.value} {operation} {other} = {result}")

    def __add__(self, other):
        result = self.value + int(other)
        self.log("+", other, result)
        return LoggedInt(result)

    def __sub__(self, other):
        result = self.value - int(other)
        self.log("-", other, result)
        return LoggedInt(result)

    def __mul__(self, other):
        result = self.value * int(other)
        self.log("*", other, result)
        return LoggedInt(result)

    def __truediv__(self, other):
        if int(other) == 0:
            raise ZeroDivisionError("Division by zero is not allowed!")
        result = self.value / int(other)
        self.log("/", other, result)
        return LoggedInt(int(result))

    def __floordiv__(self, other):
        result = self.value // int(other)
        self.log("//", other, result)
        return LoggedInt(result)

    def __mod__(self, other):
        result = self.value % int(other)
        self.log("%", other, result)
        return LoggedInt(result)

    def __pow__(self, other):
        result = self.value ** int(other)
        self.log("**", other, result)
        return LoggedInt(result)

    def __int__(self):
        return self.value 

    def __eq__(self, other):
        return self.value == int(other)  

a = LoggedInt(10)
b = LoggedInt(3)

c = a + b 
d = a - b  
e = a * 2  
f = a / b  

print(c, d, e, f)  
