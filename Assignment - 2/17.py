from math import gcd

def coprime_dict(N):
    return {n: {m for m in range(1, N+1) if gcd(n, m) == 1} for n in range(1, N+1)}

# let N = 10
N = 10
result = coprime_dict(N)
print(result)
