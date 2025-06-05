def sieve_of_eratosthenes(n):
    primes = {x for x in range(2, n+1)}
    for i in range(2, int(n**0.5) + 1):
        if i in primes:
            primes -= {i * j for j in range(i, (n // i) + 1)}
    return primes

# let value of N = 100
N = 100
print(sieve_of_eratosthenes(N))
