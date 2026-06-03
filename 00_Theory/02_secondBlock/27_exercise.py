class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def descrivi(self):
        descrizione = f"Ciao, mi chiamo {self.name} e ho {self.age} anni."
        return descrizione

persona = Person("Giulia", 28)


risultato_descrizione = persona.descrivi()

print(risultato_descrizione)