class Person:
    def __init__(self,name,age):
        self.name = name
        self.__age = age
        
    def getAge(self):
        return self.__age

p1 = Person("marta", 20)

print(p1.getAge())

#object._classname__privateattribute = name mangling
print(p1._Person__age)
