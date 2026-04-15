class Person:
    def __init__(self, name, age):
        self.name = name  
        self.age = age
        
    def greet(self):
        print(f"Ciao! Mi chiamo {self.name} e ho {self.age} anni.")


p1 = Person("Giulia", 22)
p2 = Person("Marco", 25)


p1.greet()
p2.greet()