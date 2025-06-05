row_nums = int(input("enter the pascal triangle row number : "))

# that means we have to print the value of 2C0 , 2C1 , 2C2

def factorial (n) :
    product = 1
    for i in range(1, n+1) :
        product = product * i

    return product
def combination(i , j) :
    return factorial(i) // (factorial(j) * factorial(i-j))

list = [] 

for i in range(0,row_nums) :
    list.append( combination (row_nums - 1 , i))


print(list)



    

