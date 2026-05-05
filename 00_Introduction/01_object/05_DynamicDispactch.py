class MotoCycle:
    def accelerate(self):
        print("la moto sta accelerando ")
    
class Car: #class className(superClass Name):   
    def accelerate(self):
        print(f"la macchina sta accelerando ")

class Bici:
    def accelerate(self):
        print("la bici sta accelerando ")
        
lists =[]

c1 = Car()
lists.append(c1)

m1 = MotoCycle()
lists.append(m1)

b1 = Bici()
lists.append(b1)

print(lists)

for el in lists:
    el.accelerate()