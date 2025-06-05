a = 31
# print(type(a)) => also valid

a = 31
t = type(a)
print(t)

b = 32.2
t = type(b)
print(t)

c = "SohamRastogi"
t = type(c)
print(t)

d = "40.5"
t = type(d)
print(t)

# typecasting

a = "31.2"
b = float(a)
print(b)
t = type(b)
print(t)


# invlaid =>

# a = "31.2"
# b = int(a)
# t = type(b)
# print(b)
# print(t)


# valid =>
a = 31.2
print(type(int(a)))
print(int(a))

a = "31.2"
print(type(float(a)))
print(float(a))

# a = "20.5"
# b = int(a)
# t = type(b)
# print(t)

a = 20
b = float(a)
print(type(b))
print(a)
print(b)



