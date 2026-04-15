class Person:
    def __init__(self, name):
        self.name = name  
        
    def voyage(self,departure,arrive):
        print(f"viaggio da {departure} a {arrive} .")


p1 = Person("Giulia")
p1.voyage("catania", "palermo")