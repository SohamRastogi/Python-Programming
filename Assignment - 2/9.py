def generate_bsp_fractal(start, end, depth):

    if depth == 0:
        return [(start, end)]  

  
    one_third = start + (end - start) / 3
    two_third = start + 2 * (end - start) / 3


    left_part = generate_bsp_fractal(start, one_third, depth - 1)
    right_part = generate_bsp_fractal(two_third, end, depth - 1)

    return left_part + right_part  


# let :
depth = 3  
bsp_sequence = generate_bsp_fractal(0, 1, depth)

print("Binary Space Partitioning Sequence (Fractal-Based):")
for segment in bsp_sequence:
    print(segment)
