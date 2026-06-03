class Vehicle: 
    def __init__(self,model,year):
        self.model = model
        self.year = year
    
    def describe(self):
        print(f"Modello: {self.model}, \nYear: {self.year}")
    
class Car(Vehicle):
    def __init__(self,model,year,doors):
        super().__init__(model,year)
        self.doors = doors
        
    def describe(self):
        print(f"Modello: {self.model} \nYear: {self.year} \nDoors: {self.doors}")
        
c1 = Car("Corsa", 2022, 2)

print(c1.describe())