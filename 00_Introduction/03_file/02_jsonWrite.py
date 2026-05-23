import json 

filePath = "00_Introduction/03_file/assets/data2.json"

class Vehicle:
    def __init__(self, wheels, steering): 
        self.wheels = wheels
        self.steering = steering
        
v = Vehicle(4, 'volante')  # Crea un'istanza di Vehicle con 4 ruote e volante

# v.__dict__ è un dizionario che contiene tutti gli attributi dell'istanza
# Esempio: {"wheals": 4, "stearing": "volante"}
# json.dump() converte questo dizionario in formato JSON e lo salva nel file
with open(filePath, 'w') as f:
    json.dump(v.__dict__, f)