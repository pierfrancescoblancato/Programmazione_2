class Vehicle:
    type = "Car"

    def __init__(self, model):
        self.model = model

v1 = Vehicle("escort")
v2 = Vehicle("panda")

print(f"v1.type: {v1.type}")
print(f"v2.type: {v2.type}")

Vehicle.type = "Truck"

print(f"v1.type: {v1.type}")
print(f"v2.type: {v2.type}")

print(f"Vehicle.type: {Vehicle.type}")