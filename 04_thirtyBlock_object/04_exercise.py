class Student:
    def __init__(self,name,grade):
        self.name = name
        self.grade = grade
        print(f"oggetto creato con successo: {name} {grade}")
        
s1 = Student("ciccio",20)
s2 = Student("Marco",30)

s1.age = 21
print(f"Eta di {s1.name} (s1): {s1.age}")

print(s2.age)