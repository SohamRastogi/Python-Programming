import math

radius = int(input("enter the radius of the circle : "))

def circle(radius) :
    area = math.pi * radius * radius 
    perimeter = math.pi * 2 * radius
    return area, perimeter

a , p = circle(radius)

print(a, p)