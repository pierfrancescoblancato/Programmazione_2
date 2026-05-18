lista = ["GM", 25, "M"]

dizionario = {"key": "value", "name": "gm", "age": 25, "gender": "m"}

print(dizionario)
print(type(dizionario))
print(dizionario["name"])

# Metodo get(): restituisce il valore se la chiave esiste, altrimenti restituisce "NAN"
print(dizionario.get("name", "NAN"))

chiave = input("cosa vuoi sapere: ")
print(dizionario.get(chiave, "NAN"))

# Aggiunge una nuova chiave "citta" se non esiste già nel dizionario
if not "citta" in dizionario:
    dizionario["citta"] = "catania"

print(dizionario)

# pop() rimuove la chiave specificata e restituisce il valore associato
genere = dizionario.pop("gender")
print(genere)
print(dizionario)

# clear() è un metodo, ma mancano le parentesi () per chiamarlo correttamente
# Così stampa solo il riferimento al metodo, non lo esegue
print(dizionario.clear)

print(len(dizionario))
# sorted() restituisce una lista ordinata delle chiavi del dizionario
print(sorted(dizionario))

# Itera sulle chiavi del dizionario
for chiave in dizionario.keys():
    print(dizionario[chiave])

# NOTA: L'ultimo ciclo ha un problema: usa 'key' che non è definita in questo scope
# Inoltre stampa la stessa coppia per ogni valore
for valore in dizionario.values():
    print(chiave, dizionario[chiave])  # Errore: 'chiave' non è definita qui