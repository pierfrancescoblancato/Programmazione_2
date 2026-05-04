class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

s = Student("Giulia", 22)

# 1. Simuliamo di ricevere il nome dell'attributo come stringa (es. da un input dell'utente)
attributo_richiesto = "age"

# 2. Leggiamo il valore usando getattr
# getattr vuole due cose: l'oggetto da ispezionare e il nome dell'attributo (come stringa)
valore = getattr(s, attributo_richiesto)

print("--- Accesso Dinamico ---")
print(f"Hai richiesto l'attributo: '{attributo_richiesto}'")
print(f"Il valore trovato è: {valore}")


# --- BONUS: Gestire gli errori con getattr ---
print("\n--- Bonus: Attributo inesistente ---")
attributo_falso = "city"

# Se chiedi a getattr un attributo che non esiste, il programma andrebbe in errore (AttributeError).
# Per evitarlo, puoi passare un "valore di default" come terzo argomento:
valore_sicuro = getattr(s, attributo_falso, "Valore non specificato (default)")

print(f"Hai richiesto l'attributo: '{attributo_falso}'")
print(f"Il valore trovato è: {valore_sicuro}")