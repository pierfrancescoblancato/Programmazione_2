# --- List Operations ---
a = [1, 2, 3, 4, 5]
b = [6, 7]

# Concatenates lists 'a' and 'b' into a new list 'c'
c = a + b
print(c)

d = ["fragola","banana","ananas"]
# Sorts the list 'd' in-place (modifies the original list directly)
d.sort()
print(d)

e = ["fragola","banana","ananas"]
# sorted() returns a NEW sorted list; the original list 'e' remains UNCHANGED
print(sorted(e)) 

x = [1, 2, 3, 4, 5]
# Removes the first occurrence of the VALUE 2 from the list
x.remove(2)
print(x)

# --- String Operations ---
y = "Forza Catania" 
# Slicing: prints characters from index 1 to 4 (5 is excluded) -> "orza"
print(y[1:5])

# Membership operator: checks if "Catania" is a substring of 'y' (returns True)
z = "Catania" in y
print(z)

s = "heLLo wORDl"
# Capitalizes only the first letter and lowers the rest
print(s.capitalize())
# Converts the entire string to uppercase
print(s.upper())
# Converts the entire string to lowercase
print(s.lower())
# The original string 's' remains unchanged (strings are immutable)
print(s)

# --- String Cleaning & Chaining ---
s2 = "      python              "
# Removes all leading and trailing whitespace
print(s2.strip())
# Method Chaining: strips spaces, replaces "th" with "or", then capitalizes -> "Pyron"
print(s2.strip().replace("th","or").capitalize())
# The original string 's2' remains unchanged with all its spaces
print(s2)