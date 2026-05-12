import json 
#JSON, acronimo di JavaScript Object Notation, è un formato testuale leggero, standard e indipendente dal linguaggio, utilizzato per memorizzare e scambiare dati strutturati, i dati sono in formato salvati chiave:valore

filePath = "00_Introduction/03_file/assets/data1.json"
data = 5

#write
with open(filePath, 'w') as f:
    json.dump(data, f)

#read
with open(filePath, 'r') as f:
    value = json.load(f)

print(value)