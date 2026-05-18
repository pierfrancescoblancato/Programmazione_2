age = int(input("eta: "))

# Controllo dei limiti per l'età umana
if age > 120 or age < 0:
    # raise solleva un'eccezione personalizzata se l'età non è valida
    raise ValueError("Eta non vera simile")  # ValueError: Eta non vera simile
else:
    print(f"Eta valida: {age}")