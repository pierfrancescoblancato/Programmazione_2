# Lista di esempio (non utilizzata nel codice, ma lasciata come riferimento)
lista = ["GM", 25, "M"]

# Dizionario iniziale con coppie chiave-valore
dizionario = {"key": "value", "name": "gm", "age": 25, "gender": "m"}

# Stampa il dizionario completo
print("Dizionario completo:", dizionario)

# Stampa il tipo di dato di dizionario
print("Tipo di dato:", type(dizionario))

# Accesso diretto a una chiave (se non esiste, genera KeyError)
print("Valore di 'name':", dizionario["name"])

# Metodo get(): restituisce il valore se la chiave esiste, altrimenti restituisce "NAN"
# Più sicuro dell'accesso diretto perché non genera errori
print("Get 'name' con default 'NAN':", dizionario.get("name", "NAN"))

# Chiede all'utente quale informazione vuole conoscere
chiave = input("Cosa vuoi sapere (es. name, age, key, gender): ")
print("Risultato:", dizionario.get(chiave, "NAN"))

# Aggiunge una nuova chiave "citta" se non esiste già nel dizionario
if "citta" not in dizionario:  # Sintassi più Pythonica di "not ... in"
    dizionario["citta"] = "catania"

print("Dizionario dopo aggiunta 'citta':", dizionario)

# pop(): rimuove la chiave specificata e restituisce il valore associato
# Se la chiave non esiste, genera KeyError (si può usare pop("key", default) per evitarlo)
genere = dizionario.pop("gender")
print("Valore rimosso con pop('gender'):", genere)
print("Dizionario dopo pop:", dizionario)

# Il metodo .clear() rimuove tutti gli elementi da un dizionario, lasciandolo vuoto
# dizionario.clear()

# len(): restituisce il numero di coppie chiave-valore nel dizionario
print("Numero di elementi nel dizionario:", len(dizionario))

# sorted(): restituisce una lista ordinata alfabeticamente delle chiavi del dizionario
print("Chiavi ordinate:", sorted(dizionario))

# METODO 1: Itera sulle chiavi del dizionario usando .keys()
print("\n--- Iterazione sulle chiavi ---")
for chiave in dizionario.keys():
    print(f"Chiave: {chiave} → Valore: {dizionario[chiave]}")

# METODO 2: Itera direttamente sul dizionario (di default itera sulle chiavi)
print("\n--- Iterazione diretta (sulle chiavi) ---")
for chiave in dizionario:
    print(f"{chiave}: {dizionario[chiave]}")

# METODO 3: Itera solo sui valori usando .values()
print("\n--- Iterazione solo sui valori ---")
for valore in dizionario.values():
    print(f"Valore: {valore}")

# METODO 4 (MIGLIORE): Itera su chiave e valore contemporaneamente usando .items()
print("\n--- Iterazione su chiave e valore con .items() ---")
for chiave, valore in dizionario.items():
    print(f"{chiave} = {valore}")