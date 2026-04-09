a = 0

# A while loop that continues as long as 'a' is less than or equal to 10
while a <= 10:
    a += 1  # Increment 'a' by 1 at each iteration
    
    # Check if 'a' is odd using the modulo operator (%)
    if a % 2 != 0:
        continue  # Skip the rest of the loop and start the next iteration
    
    # This line only runs if 'a' is even
    print(a)
else:
    # The 'else' block in a loop executes when the condition becomes false
    print("ciclo finito")
    
fruits = ["fragola","banana","cocco"]

# Method 1: Iterating directly over the elements (most "Pythonic")
for fruit in fruits:
    print(fruit)
    
# Method 2: Iterating using an index and range()
# len(fruits) returns 3, so range(3) generates 0, 1, 2
for i in range(len(fruits)):
    print(f"element {i+1}: {fruits[i]}")

# Method 3: Using enumerate()
# This is the best practice when you need both the index and the value
for i, el in enumerate(fruits):
    print(f"element {i+1}: {el}")