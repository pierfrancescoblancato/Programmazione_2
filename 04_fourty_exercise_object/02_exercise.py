class Vehicle:
    type = "Car"

    def __init__(self, model):
        self.model = model

v1 = Vehicle("escort")
v2 = Vehicle("panda")

print(f"v1.type: {v1.type}")
print(f"v2.type: {v2.type}")

v1.type = "Truck"

print(f"v1.type: {v1.type}")
print(f"v2.type: {v2.type}")

print(f"Vehicle.type: {Vehicle.type}")

print(f"v1.__dict__: {v1.__dict__}")

print(f"v2.__dict__: {v2.__dict__}")