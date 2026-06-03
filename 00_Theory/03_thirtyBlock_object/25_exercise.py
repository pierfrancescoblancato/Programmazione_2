class CarSteering:
    def steer(self):
        print("La macchina sta sterzando")
        
class BikeSteering:
    def steer(self):
        print("La bici sta sterzando")

class Vehicle:
    def __init__(self,steeringObject):
        self.steering = steeringObject
        
    def engage_steering(self):
        print("Il veicolo sta svolgendo la manovra...")
        self.steering.steer()
    
volante = CarSteering()
manubrio = BikeSteering()

auto = Vehicle(volante)
moto = Vehicle(manubrio)

auto.engage_steering()
moto.engage_steering()
