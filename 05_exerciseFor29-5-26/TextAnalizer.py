# stringa in input
string = input("Enter a string: ")

# 1. conta le parole serparate da spazi
def countWordsSeparatedSpaces(string: str):
    count = len(string.split())
    return count

# 2. conta le vocali
def countVowels(string: str):
    count = 0
    vowels ="aeiou"
    
    lwr = string.lower()
    for v in lwr:
        if v in vowels:
            count += 1
    return count

# 3. conta le consonanti
def countConsonants(string: str):
    count = 0
    consonants ="bcdfghjklmnpqrstvwxyz"
    
    lwr = string.lower()
    for c in lwr:
        if c in consonants:
            count += 1
    return count

# 4. conta le lettere che sono maiuscole
def countUppercase(string: str):
    count = 0
    for u in string:
        if u.isupper():
            count += 1
    return count

# 5. conte gli spazi
def countSpace(string: str):
    lwr = string.lower()
    return lwr.count(' ')

# 6.quanti caratteri che non sono ne' lettere, ne' numeri , ne' spazi
def countCharter(string: str):
    count = 0
    for c in string:
        if not c.isalnum() and not c.isspace():
            count += 1
        else:
            continue
    return count
            
print(f"Il numero di parole separate da spazi: {countWordsSeparatedSpaces(string)}")
print(f"Il numero di vocali: {countVowels(string)}")
print(f"Il numero di consonanti: {countConsonants(string)}")
print(f"Il numero di lettere maiuscole: {countUppercase(string)}")
print(f"Il numero di spazi: {countSpace(string)}")
print(f"Il numero di caratteri che non sono ne' lettere, ne' numeri , ne' spazi :{countCharter(string)}")