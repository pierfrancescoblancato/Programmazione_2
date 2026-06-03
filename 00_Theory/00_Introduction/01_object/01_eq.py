# Definizione della classe Student
class Student: 
    # Attributo di classe (condiviso da tutte le istanze)
    description = "questa classe dovrebbe essere usata ogni volta che creerai un nuovo studente"

    # Metodo costruttore: inizializza gli attributi dell'istanza
    def __init__(self, name, surname, age = 1, course= "NULL"):
        self.name = name.strip().capitalize()      # Rimuove spazi e capitalizza
        self.surname = surname.strip().capitalize() 
        self.age = age
        self.course = course
        self.fullname = self.name + self.surname   # Concatenazione (manca spazio)

    # Metodo speciale __eq__: ridefinisce l'operatore di uguaglianza (==)
    def __eq__(self, other):
        if isinstance(other, Student):             # Verifica che other sia uno Student
            if(self.name == other.name and self.surname == other.surname and self.age == other.age):
                return True
            else:
                return False
        else:
            return False
            
# Creazione di tre istanze Student
s1 = Student("tommaso", "pappalardo", 32, "developer")
s2 = Student("tommaso", "pappalardo", 15, "developer")
s3 = Student("tommaso", "pappalardo", 32, "cybersecurty")

print(s1 == s2)  # False: età diversa (32 vs 15)
print(s1 == s3)  # True: nome, cognome ed età uguali (course non viene confrontato)