import itertools

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_generator(N):
    primes = [num for num in range(2, N + 1) if is_prime(num)]
    return itertools.cycle(primes)  

# example :
N = 10
cyclic_primes = prime_generator(N)


for _ in range(20):
    print(next(cyclic_primes), end = " ")
