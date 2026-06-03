import os

a = os.getcwd()  # cartella di lavoro attuale
print("cartella corrente:", a)
print("cartelle e file:", os.listdir())

# os.mkdir() - crea UNA cartella
os.mkdir('andrea')

# os.makedirs() - crea TUTTE le cartelle intermedie
os.makedirs('andrea/documenti/foto/2024', exist_ok=True)

# os.chdir() - cambia directory
os.chdir('andrea')
print("Ora in:", os.getcwd())

# os.rmdir() - elimina solo se vuota
os.rmdir('andrea/backup')  # se esiste ed è vuota