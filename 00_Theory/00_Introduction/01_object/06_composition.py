'''
La Composition è una tecnica di progettazione in cui una classe 
contiene al suo interno istanze di altre classi come attributi,
invece di ereditare da esse. Si basa sulla relazione "HA UN" (has-a)
'''
class Engine:
    """Componente motore - può essere usato in auto, moto, barche, ecc."""
    def __init__(self, horsepower, fuel_type):
        self.horsepower = horsepower
        self.fuel_type = fuel_type
    
    def start(self):
        print(f"Motore da {self.horsepower} CV avviato")
    
    def stop(self):
        print("Motore spento")

class Wheels:
    """Componente ruote - riutilizzabile in qualsiasi veicolo"""
    def __init__(self, count=4):
        self.count = count
    
    def rotate(self):
        print(f"Ruote {self.count} in movimento")

class Radio:
    """Componente radio - potrebbe essere in auto, casa, ufficio"""
    def __init__(self, brand="Sony"):
        self.brand = brand
        self.is_on = False
    
    def turn_on(self):
        self.is_on = True
        print(f"Radio {self.brand} accesa")

# ============================================================================
# COMPOSITION: la classe Car COMPONE il suo comportamento usando altre classi
# ============================================================================
class Car:
    """
    Car NON eredita da Engine/Wheels/Radio (non è un "is-a")
    Car CONTIENE Engine/Wheels/Radio (relazione "has-a")
    """
    def __init__(self, model, horsepower):
        self.model = model
        # Composition: istanzia i componenti all'interno del costruttore
        self.engine = Engine(horsepower, "benzina")  # Car HA UN motore
        self.wheels = Wheels()                       # Car HA DELLE ruote
        self.radio = Radio()                         # Car HA UNA radio
    
    def start_car(self):
        """Delega il comportamento ai componenti"""
        print(f"Avvio {self.model}...")
        self.engine.start()    # delega al motore
        self.wheels.rotate()   # delega alle ruote
        self.radio.turn_on()   # delega alla radio
    
    def stop_car(self):
        self.engine.stop()

my_car = Car("Fiat 500", 85)
my_car.start_car()
my_car.stop_car()