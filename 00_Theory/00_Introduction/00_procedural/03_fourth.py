s = "123abc"
s2 = "123abc-?"
s3 = "132"
s4 = "CIAO A TUTTI"

# isalnum(): Restituisce True se tutti i caratteri sono alfanumerici (lettere o numeri)
# s è True, s2 è False a causa dei simboli "-?"
print(s.isalnum(), s2.isalnum())

# isalpha(): Restituisce True se tutti i caratteri sono lettere (a-z)
# s3 è False perché "132" contiene solo numeri
print(s3.isalpha())

# isascii(): Restituisce True se la stringa contiene solo caratteri ASCII (simboli/lettere standard)
print(s.isascii())

# isdecimal(): Restituisce True se tutti i caratteri sono decimali (0-9)
# s è False (ha lettere), s3 sarebbe True
print(s.isdecimal())

# isdigit(): Restituisce True se tutti i caratteri sono cifre (include pedici come ²)
print(s3.isdigit())

# isupper(): Restituisce True se tutti i caratteri con maiuscole/minuscole sono maiuscoli
print(s4.isupper())

# islower(): Restituisce True se tutti i caratteri con maiuscole/minuscole sono minuscoli
print(s4.islower())