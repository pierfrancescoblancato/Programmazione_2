import json

filePath = "00_Introduction/03_file/assets/data2.json"

class Vehicle:
    def __init__(self, wheals, stearing):  # NOTA: probabilmente "wheels" e "steering" (errori di battitura)
        self.wheals = wheals
        self.stearing = stearing
        
# Legge il file JSON e lo converte in un dizionario Python
with open(filePath, 'r') as f:
    value = json.load(f)  # value sarà un dizionario es: {"wheals": 4, "stearing": "wheel"}

# **value (unpacking operator) disimballa il dizionario in argomenti keyword
# Equivalente a: Vehicle(wheals=value["wheals"], stearing=value["stearing"])
v1 = Vehicle(**value)

print(type(v1))  # Output: <class '__main__.Vehicle'>
print(v1.stearing, v1.wheals)  # Stampa i valori letti dal JSON