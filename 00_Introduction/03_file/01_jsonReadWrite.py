import json 
# JSON, acronimo di JavaScript Object Notation, è un formato testuale leggero, standard e indipendente dal linguaggio,
# utilizzato per memorizzare e scambiare dati strutturati. I dati sono salvati in formato chiave:valore

filePath = "00_Introduction/03_file/assets/data1.json"
data = 5

# --- SCRITTURA (dump) ---
# json.dump() = scrive/converte i dati Python in formato JSON e li salva su file
with open(filePath, 'w') as f:
    json.dump(data, f)  # scrive il dato (int, list, dict, ecc.) nel file in formato JSON

# --- LETTURA (load) ---
# json.load() = legge un file JSON e lo converte in tipo Python (int, list, dict, ecc.)
with open(filePath, 'r') as f:
    value = json.load(f)  # carica e converte il contenuto JSON in un tipo Python

print(value)  # Output: 5