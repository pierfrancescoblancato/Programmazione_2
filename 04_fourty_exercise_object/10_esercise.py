class Vehicle:
    pass

class Car(Vehicle):
    pass

c = Car()

print(isinstance(c, Vehicle))