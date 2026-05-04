import os

for i in range(12, 30):
    filename = f"{i}_exercise.py"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"# Esercizio {i}\n\nif __name__ == '__main__':\n    pass\n")
    print(f"Creato: {filename}")