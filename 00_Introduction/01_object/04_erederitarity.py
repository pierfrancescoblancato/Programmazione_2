class Vehicle:
    def __init__(self,model,year):
        self.model = model
        self.year = year
    
    def accelerate(self):
        print(f"{self.model} sta accelerando ed e' un veicolo generico")
        
    def sterzo(self,angle):
        print(f"{self.model} sta sterzando di {angle} grandi")
    
class Car(Vehicle): #class className(superClass Name):
    def __init__(self,model,year,doors = 5):
        super().__init__(model,year)
        self.doors = doors
        
    def accelerate(self):
        print(f"{self.model} sta accelerando ma e' una macchina")
        
class MotorCycle(Vehicle):
    def __init__(self,model, year, isAutomatic = False):
        super().__init__(model,year)
        self.isAutomatic = isAutomatic
        
class SuperCar(Car, Vehicle):
    color = red

c1 = Car("fiat", 2022,5)
c2 = Car("BMW", 2023,3)

v1 = Vehicle("Carro", 2023)

v1.accelerate()

c1.accelerate()