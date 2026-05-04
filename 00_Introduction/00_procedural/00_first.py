# Prompt user for input, convert the string to an integer, and store it in 'a'
a = int(input("Enter a value: ")) 

# Prompt user for input, convert the string to an integer, and store it in 'b'
b = int(input("Enter a value: ")) 

# Define a function named 'sum' that takes two arguments
def sum(a, b):
    return a + b  # Return the mathematical sum of the two inputs

# Print values using commas (Python automatically adds spaces between items)
print("the value of a is:", a,"and, of b is:", b, "and the sum of a and b is", sum(a,b))

# Convert a float to an integer (this truncates the decimal, printing 8)
print(int(8.9))

# Print using an f-string for cleaner formatting and direct variable injection
print(f"the value of a is: {a} and of b is: {b} and the sum of a and b is {sum(a,b)}")

