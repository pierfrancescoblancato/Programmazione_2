class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

s = Student("Giulia", 22)

attribute = "age"


value = getattr(s, attribute)

print(f"Hai richiesto l'attributo: '{attribute}'")
print(f"Il valore trovato è: {value}")
