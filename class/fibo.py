def fib(n) :
    a = 0
    b = 0
    sum = 1
    while(sum<n) :
        print(sum , end=" ")
        a = b
        b = sum;
        sum = a + b

def fib2(n) :
    result = []
    a = 0
    b = 0
    sum = 1
    while (sum < n) :
        result.append(sum)
        a = b
        b = a+ b
        sum = a+ b
    return result

