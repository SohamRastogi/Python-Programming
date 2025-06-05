# celcius to fahrenheit :

n = int(input("enter the temperature in degree celcius scale : "))

def convert(n) :
    alpha = 9*n/5
    return alpha + 32



a = convert(n)
print("the converted temperature to fahrenheit is : ",a)