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
        
c1 = Car("Corsa", 2022, 5)

print(c1.describe())