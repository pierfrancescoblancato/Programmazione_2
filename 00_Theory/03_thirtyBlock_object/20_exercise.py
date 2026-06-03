class Vehicle: 
    def __init__(self,model,year):
        self.model = model
        self.year = year
    
    def describe(self):
        print(f"Generic Vehicle\nModello: {self.model}, \nYear: {self.year}")
    
class Car(Vehicle):
    def __init__(self,model,year,doors):
        super().__init__(model,year)
        self.doors = doors
        
    def describe(self):
        print(f"Car\nModello: {self.model} \nYear: {self.year} \nDoors: {self.doors}")
        
class ElectricCar(Car):
    def __init__(self,model,year,doors,watt):
        super().__init__(model,year,doors)
        self.watt = watt
    
    def describe(self):
        print(f"ElectricCar\nModello: {self.model} \nYear: {self.year} \nDoors: {self.doors}\nWatt: {self.watt}w")
        
    
c1 = ElectricCar("Corsa", 2026, 5,500)

print(c1.describe())