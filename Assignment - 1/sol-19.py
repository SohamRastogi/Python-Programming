def fibonacci(n):
    a, b = 0, 1
    return tuple((a := b, b := a + b)[0] for _ in range(n))  # Comprehension-like

n = int(input("enter a number : "))
print(fibonacci(n))
