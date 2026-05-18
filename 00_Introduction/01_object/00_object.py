# la classe è uno stampino a cui all'interno definiamo uno schema, non rigido
class Student: 
    # attributi di classe, quindi si riferiscono all'intera classe
    name_pl = ""
    role_pl = "Student"
    description = "questa classe dovrebbe essere usata ogni volta che creerai un nuovo studente"
        
    # metodi speciali, definiscono come si comportano gli oggetti della classe quando viene istanziato in situazioni particolari
    # non esiste overloading dei costruttori, quindi non esistono più costruttori con solo parametri differenti
    def __init__(self, name, surname, age = 1, course= "NULL"):
        self.name = name.strip().capitalize()
        self.surname = surname.strip().capitalize()
        self.age = age
        self.course = course
        self.fullname = self.name + self.surname
        
    # self va inserito sempre, richiama se stesso
    def saluta(self):
        print(f"ciao a tutti, mi chiamo {self.name} e ho {self.age} anni e sono {self.role_pl}!")

    
# sono attributi riferiti all'istanza
s1 = Student("tommaso", "pappalardo", 32, "developer")
s1.saluta()
s2 = Student("riccardo", "fuffolo")
s2.saluta()


print(s1.name, s1.surname, s1.age)
print(s1)  # stampa la rappresentazione di default dell'oggetto (indirizzo di memoria)

print(Student.description)  # accesso all'attributo di classe
print(s1.description)       # l'istanza eredita anche l'attributo di classe