class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age  # attributo privato (con doppio underscore)
        
    def getAge(self):
        return self.__age  # metodo getter per accedere all'attributo privato
    
    def setAge(self, newAge):
        self.__age = newAge  # metodo setter per modificare l'attributo privato

p1 = Person("marta", 20)

# Accesso corretto tramite metodo getter
print(p1.getAge())  # Output: 20

# name mangling: Python rinomina internamente __age in _Person__age
# object._classname__privateattribute = name mangling
print(p1._Person__age)  # Output: 20 (accesso diretto non raccomandato, viola l'incapsulamento)