n = int(input("enter a number : "))  

num_dict = {i: {"binary": bin(i), "hexadecimal": hex(i)} for i in range(n+1)}


for key, value in num_dict.items():
    print(f"{key}: Binary = {value['binary']}, HexaDecimal = {value['hexadecimal']}")
