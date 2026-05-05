age = int(input("eta: "))

if age > 120 or age < 0:
    raise ValueError("Eta non vero simile")
else:
    print(f"Eta valida: {age}")