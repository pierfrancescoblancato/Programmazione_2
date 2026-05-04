#la classe e' uno stampino a cui all'interno definiamo uno schema, non 'rigido
class Student: 
    #attributi di classe, quindi si riferiscono all intera classe

    description = "this class is supposed to be used anytime you will create a new student"
        
    #metodi speciali, definiscono come si comportano degli oggetti della classe quando viene istanziato in situazioni in particolare/specifici
    #non esiste overloading dei costruttori, quindi non esistono piu costruttori con solo parametri differenti
    def __init__(self, name, surname, age = 1, course= "NULL"):
        self.name= name.strip().capitalize()
        self.surname = surname.strip().capitalize()
        self.age = age
        self.course = course
        self.fullname = self.name + self.surname

    # viene richiamata automaticamente quando si fa == 
    def __eq__(self, other):
        if isinstance(other, Student):
            if(self.name == other.name and self.surname == other.surname and self.age == other.age):
                return True
            else:
                return False
        else:
            return False
            
s1 = Student("tommaso","pappalardo", 32, "developer")
s2 = Student("tommaso","pappalardo", 15, "developer")
s3 = Student("tommaso","pappalardo", 32, "cybersecurty")

print(s1 == s2)
print(s1 == s3)

