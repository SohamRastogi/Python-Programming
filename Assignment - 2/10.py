def get_factors(n):
    return tuple(i for i in range(1, n + 1) if n % i == 0)

numbers = range(1, 11) # let n = 10

factors_dict = {num: get_factors(num) for num in numbers}


print(factors_dict)
