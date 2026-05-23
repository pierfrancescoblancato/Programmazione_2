class Vehicle:
    def __init__(self, model, year):
        self.model = model
        self.year = year
    
    def accelerate(self):
        print(f"{self.model} sta accelerando ed è un veicolo generico")
        
    def sterzo(self, angle):
        print(f"{self.model} sta sterzando di {angle} gradi")
    
class Car(Vehicle):  # class NomeClasse(NomeSuperClasse):
    def __init__(self, model, year, doors=5):
        super().__init__(model, year)  # chiama il costruttore della classe padre
        self.doors = doors
        
    def accelerate(self):  # override del metodo accelerate della classe padre
        print(f"{self.model} sta accelerando ma è una macchina")
        
class MotorCycle(Vehicle):
    def __init__(self, model, year, isAutomatic=False):
        super().__init__(model, year)
        self.isAutomatic = isAutomatic
    def accelerate(self):  # override del metodo accelerate della classe padre
        print(f"{self.model} sta accelerando ma è una moto")  
              
class SuperCar(Car, Vehicle):  # ereditarietà multipla
    def __init__(self, model, year, doors=5, color = 'yallow' ):
        super().__init__(model, year, doors)
        self.color = color
        
    def accelerate(self):  # override del metodo accelerate della classe padre
        print(f"{self.model} sta accelerando ma è una super macchina")
        
c1 = Car("fiat", 2022, 5)
c2 = Car("BMW", 2023, 3)

v1 = Vehicle("Carro", 2023)

s1 = SuperCar("bugatti",2022,3,"red")

v1.accelerate()  # chiama il metodo della classe Vehicle
c1.accelerate()   # chiama il metodo sovrascritto della classe Car
s1.accelerate()