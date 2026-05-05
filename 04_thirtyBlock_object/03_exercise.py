class Student:
    def __init__(self,name,grade):
        self.name = name
        self.grade = grade
        print(f"oggetto creato con successo: {name} {grade}")
        
s1 = Student("ciccio",20)
s2 = Student("Marco",30)