# Chiede all'utente un input, converte la stringa in intero e la memorizza in 'a'
a = int(input("Enter a value: ")) 

# Chiede all'utente un input, converte la stringa in intero e la memorizza in 'b'
b = int(input("Enter a value: ")) 

# Definisce una funzione di nome 'sum' che accetta due argomenti
def sum(a, b):
    return a + b  # Restituisce la somma matematica dei due input

# Stampa i valori usando le virgole (Python aggiunge automaticamente spazi tra gli elementi)
print("the value of a is:", a, "and, of b is:", b, "and the sum of a and b is", sum(a, b))

# Converte un float in intero (tronca la parte decimale, stampando 8)
print(int(8.9))

# Stampa usando una f-string per una formattazione più pulita e un'iniezione diretta delle variabili
print(f"the value of a is: {a} and of b is: {b} and the sum of a and b is {sum(a, b)}")