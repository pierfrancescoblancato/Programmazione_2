file = "00_Introduction/03_file/assets/text.txt"

# --- LETTURA ---
# apertura di un file
file_stream = open(file, 'r')  # read: r (default), write: w, append: a
content = file_stream.readline()  # legge la prima riga
print(content)

file_stream.close()  # è importante chiudere il file!

# with gestisce automaticamente la chiusura del file
with open(file, 'r') as f:  # read = intero testo, readline = riga per riga, readlines = lista di righe
    content1 = f.read()      # tutto il contenuto come stringa
    content2 = f.readline()  # prima riga (vuota perché read() ha già letto tutto)
    content3 = f.readlines() # lista di righe (vuota perché già letto)

print(content1, content2, content3)

# --- SCRITTURA (sovrascrive) ---
with open(file, 'w') as f:  # 'w' = write - attenzione: SOVRASCRIVE il file
    newText = '''1) questo è un nuovo testo 
    che andrà a sovrascriversi
    '''
    f.write(newText)  # write = sovrascrive il file, writelines = scrive una lista

# --- SCRITTURA (append - aggiunge) ---
with open(file, 'a') as f:  # 'a' = append - AGGIUNGE alla fine del file
    newText = '''
    2) questo è un nuovo testo 
    che andrà alla fine ad appendesi
    '''
    f.write(newText)

lista = ['questa ', 'è', ' una lista ']
with open(file, 'a') as f:
    f.writelines(lista)  # writelines = scrive ogni elemento della lista

# --- Modalità di apertura ---
# t = text (testo - default)
# b = binary (binario)

'''
Modalità complete:
r   = lettura (text)
rt  = lettura (text - esplicito)
rb  = lettura (binary)
w   = scrittura (sovrascrive, text)
wt  = scrittura (sovrascrive, text)
wb  = scrittura (sovrascrive, binary)
a   = append (aggiunge, text)
at  = append (aggiunge, text)
ab  = append (aggiunge, binary)
'''