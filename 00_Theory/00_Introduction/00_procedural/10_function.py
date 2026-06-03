def saluto(nome: str):
    print(f"Ciao, {nome}!")

def moltiplicazione(a, b, c=1):
    if a == 3:
        return 3
    else:
        return a * b * c

print("--- INIZIO PROGRAMMA ---")

saluto("Gianmaria")
saluto("Franco")

print("\n--- TEST MOLTIPLICAZIONI ---")

# Se a == 3, la funzione restituisce 3 senza moltiplicare
print("Condizione (a=3):", moltiplicazione(3, 4)) 

# Usa il valore di default per c (c=1)
print("Base con default:", moltiplicazione(4, 5)) 

# Argomenti posizionali: a=4, b=2, c=6
print("Posizionali:", moltiplicazione(4, 2, 6))

# Argomenti per keyword (parola chiave): l'ordine non conta
print("Keyword:", moltiplicazione(a=7, b=4, c=5))

# Argomenti misti: prima posizionali, poi keyword
# a=7 (posizionale), c=2 (keyword), b=3 (keyword)
print("Misti:", moltiplicazione(7, c=2, b=3))