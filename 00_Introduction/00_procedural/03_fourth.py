s = "123abc"
s2 = "123abc-?"
s3 = "132"
s4 = "CIAO A TUTTI"

# isalnum(): Returns True if all characters are alphanumeric (letters or numbers)
# s is True, s2 is False because of symbols "-?"
print(s.isalnum(), s2.isalnum())

# isalpha(): Returns True if all characters are letters (a-z)
# s3 is False because "132" contains only numbers
print(s3.isalpha())

# isascii(): Returns True if the string contains only ASCII characters (standard symbols/letters)
print(s.isascii())

# isdecimal(): Returns True if all characters are decimals (0-9)
# s is False (has letters), s3 would be True
print(s.isdecimal())

# isdigit(): Returns True if all characters are digits (includes subscripts like ²)
print(s3.isdigit())

# isupper(): Returns True if all cased characters are uppercase
print(s4.isupper())

# islower(): Returns True if all cased characters are lowercase
print(s4.islower())