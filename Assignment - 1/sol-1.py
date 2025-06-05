from collections import defaultdict

def prime_factors(n):
    factors = defaultdict(int)
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors[d] += 1
            n //= d
        d = d + 1
    if n > 1:
        factors[n] += 1
    return dict(factors)

N = int(input("Enter N: "))
prime_factor_dict = {i: prime_factors(i) for i in range(1, N + 1)}

print(prime_factor_dict)
