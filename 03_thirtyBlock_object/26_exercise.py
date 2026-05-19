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
        self.steering.steer()

auto = Vehicle(CarSteering())
auto.engage_steering()

auto.steering = BikeSteering()
auto.engage_steering()