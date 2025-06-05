def ipv4_generator():
    return (
        f"{a}.{b}.{c}.{d}"
        for a in range(256)
        for b in range(256)
        for c in range(256)
        for d in range(256)
    )

gen = ipv4_generator()
for _ in range(10): # first 10 ipv4 addresses.
    print(next(gen))
