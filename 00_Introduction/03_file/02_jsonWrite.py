import json 

filePath = "00_Introduction/03_file/assets/data2.json"

class Vehicle:
    def __init__(self, wheals, stearing):  # NOTA: errori di battitura (wheals/wheels, stearing/steering)
        self.wheals = wheals
        self.stearing = stearing
        
v = Vehicle(4, 'volante')  # Crea un'istanza di Vehicle con 4 ruote e volante

# v.__dict__ è un dizionario che contiene tutti gli attributi dell'istanza
# Esempio: {"wheals": 4, "stearing": "volante"}
# json.dump() converte questo dizionario in formato JSON e lo salva nel file
with open(filePath, 'w') as f:
    json.dump(v.__dict__, f)