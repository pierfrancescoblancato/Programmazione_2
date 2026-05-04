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

print("Condizione (a=3):", moltiplicazione(3, 4)) 

print("Base con default:", moltiplicazione(4, 5)) 

print("Posizionali:", moltiplicazione(4, 2, 6))

print("Keyword:", moltiplicazione(a=7, b=4, c=5))

print("Misti:", moltiplicazione(7, c=2, b=3))

