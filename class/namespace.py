# Built-in Scope Example
from math import factorial  # Built-in function

# Global Scope
x = "Global Variable"

def outer_function():
    x = "Enclosing Variable"  # Enclosing scope

    count = 0  # Another enclosing variable

    def middle_function():
        x = "Middle Enclosing Variable"  # Another level of enclosing scope

        def inner_function():
            # Local Scope
            x = "Local Variable"

            print(f"1️⃣ Built-in Scope: Factorial of 5 → {factorial(5)}")

            print(f"2️⃣ Local Scope: {x}")  # Uses the local 'x'

            # Demonstrating nonlocal on multiple levels
            nonlocal x  # Modifies 'Middle Enclosing Variable'
            x = "Modified by Inner (nonlocal)"

            print(f"3️⃣ After nonlocal change, Middle Enclosing Scope: {x}")

            # Changing count using nonlocal (Enclosing Variable)
            nonlocal count
            count += 1  # Modify enclosing variable

        inner_function()

        print(f"4️⃣ After inner_function call, Middle Enclosing Scope: {x}")  # Should reflect change

    middle_function()

    print(f"5️⃣ Outer Function Scope: {x}")  # Should remain unchanged

# Global function that modifies global x
def modify_global():
    global x  # Explicitly modifies the global x
    x = "Modified Global Variable"

print(f"🌍 Initial Global Scope: {x}")  # Original global value

# Call outer function to see nonlocal vs local in action
outer_function()

# Modify the global variable
modify_global()
print(f"🌍 After modify_global call, Global Scope: {x}")  # Should reflect change