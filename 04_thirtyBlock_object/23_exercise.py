class Car:
    def steer(self):
        print("Auto: Sto girando il volante.")

class Motorcycle:
    def steer(self):
        print("Moto: Sto piegando e girando il manubrio.")

vehicles = [Car(), Motorcycle(), Car(), Motorcycle()]

print("--- Inizio dell'iterazione polimorfica ---")

for v in vehicles:
    v.steer()