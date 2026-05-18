# --- Operazioni sulle Liste ---
a = [1, 2, 3, 4, 5]
b = [6, 7]

# Concatena le liste 'a' e 'b' in una nuova lista 'c'
c = a + b
print(c)

d = ["fragola","banana","ananas"]
# Ordina la lista 'd' direttamente (modifica la lista originale)
d.sort()
print(d)

e = ["fragola","banana","ananas"]
# sorted() restituisce una NUOVA lista ordinata; la lista originale 'e' rimane INVARIATA
print(sorted(e)) 

x = [1, 2, 3, 4, 5]
# Rimuove la prima occorrenza del VALORE 2 dalla lista
x.remove(2)
print(x)

# --- Operazioni sulle Stringhe ---
y = "Forza Catania" 
# Slicing: stampa i caratteri dall'indice 1 al 4 (5 è escluso) -> "orza"
print(y[1:5])

# Operatore di appartenenza: verifica se "Catania" è una sottostringa di 'y' (restituisce True)
z = "Catania" in y
print(z)

s = "heLLo wORDl"
# Rende maiuscola solo la prima lettera e minuscole le restanti
print(s.capitalize())
# Converte l'intera stringa in maiuscolo
print(s.upper())
# Converte l'intera stringa in minuscolo
print(s.lower())
# La stringa originale 's' rimane invariata (le stringhe sono immutabili)
print(s)

# --- Pulizia e Incatenamento di Metodi sulle Stringhe ---
s2 = "      python              "
# Rimuove tutti gli spazi bianchi all'inizio e alla fine
print(s2.strip())
# Incatenamento di metodi: rimuove spazi, sostituisce "th" con "or", poi rende maiuscola la prima lettera -> "Pyron"
print(s2.strip().replace("th","or").capitalize())
# La stringa originale 's2' rimane invariata con tutti i suoi spazi
print(s2)