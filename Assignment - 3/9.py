def collatz_length(n, memo):
   
    if n in memo:
        return memo[n] 

    original_n = n
    count = 0

    sequence = []  

    while n != 1:
        if n in memo: 
            count += memo[n]
            break
        
        sequence.append(n)  
        count += 1

        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1

   
    for idx, num in enumerate(sequence):
        memo[num] = count - idx

    return count

def longest_collatz_sequence(limit):
   
    try:
        if not isinstance(limit, int) or limit <= 0:
            raise ValueError("Input must be a positive integer.")

        memo = {1: 1} 
        max_length = 0
        best_number = 1

        for num in range(1, limit + 1):
            length = collatz_length(num, memo)
            if length > max_length:
                max_length = length
                best_number = num

        return best_number, max_length

    except ValueError as ve:
        print(f"Error: {ve}")
    except MemoryError:
        print("Error: Excessive memory usage detected.")
    except Exception as e:
        print(f"Unexpected error: {e}")


N = 100000  
result = longest_collatz_sequence(N)
print("Number with longest Collatz sequence:", result[0])
print("Length of sequence:", result[1])
