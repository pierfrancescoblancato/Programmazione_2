class Student:
    def __init__(self,name,grade):
        self.name = name
        self.grade = grade
        print(f"oggetto creato con successo: {name} {grade}")
    def __str__(self):
        return f"Student: {self.name} (grade: {self.grade})"
        
s1 = Student("Alice",28)
print(s1)
