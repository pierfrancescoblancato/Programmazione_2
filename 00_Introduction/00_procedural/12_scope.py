b = 5

def saluto(nome: str):
    global b
    print(f"Ciao, {nome}!")
    b = 45
    print(b)
    
saluto("Giovanni")
print(b)
