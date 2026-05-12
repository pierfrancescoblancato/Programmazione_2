import json 

filePath = "00_Introduction/03_file/assets/data2.json"

class Vehicle:
    def __init__(self,wheals,stearing):
        self.wheals = wheals
        self.stearing = stearing
        
v =  Vehicle(4,'volante')

with open(filePath, 'w') as f:
    json.dump(v.__dict__, f)
