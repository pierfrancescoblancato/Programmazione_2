import os

start = 1
end = 2

for i in range(start, end + 1):
    filename = f"{i}_exercise.py"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"# Esercizio {i}\n")
    print(f"Creato: {filename}")