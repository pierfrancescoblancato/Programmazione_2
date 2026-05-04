# Initialize a list with one element
lista_spesa = ["banane"]

# Truthiness check: an empty list [] is False, a list with items is True
if lista_spesa:
    print(f"you have to buy {lista_spesa}")
else:
    # This runs only if the list is empty
    print("you havent to buy")
    
# Get user input and convert it to an integer
a = int(input("inserire l eta: "))

# Standard if-else block to determine adulthood
if(a < 18):
    is_adult = False
else:
    is_adult = True
    
# Ternary Operator: a compact, one-line version of the if-else above
# Syntax: [value_if_true] if [condition] else [value_if_false]
is_ad = False if a < 18 else True

# Print both results to verify they are identical
print(is_adult, is_ad)