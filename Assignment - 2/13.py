def fibo(n) :
   
    fib_list = []

    a = 1
    b = 1
    sum = 0
    for i in range(1,n+1) :
      a = b
      b = sum
      sum = a+b
      fib_list.append(sum)
    
    return tuple(fib_list)
    

alpha = fibo(10)
print (alpha)