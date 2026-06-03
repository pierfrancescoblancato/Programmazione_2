b = 5

def saluto(nome: str):
    global b  # Dichiara che stiamo usando la variabile globale 'b'
    print(f"Ciao, {nome}!")
    b = 45   # Modifica la variabile globale 'b' (non ne crea una locale)
    print(b)  # Stampa 45 (il nuovo valore globale all'interno della funzione)
    
saluto("Giovanni")
print(b)  # Stampa 45 (la variabile globale è stata modificata dalla funzione)