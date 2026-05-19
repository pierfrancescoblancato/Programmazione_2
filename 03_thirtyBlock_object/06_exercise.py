class Student:
    def __init__(self,name,grade):
        self.name = name
        self.grade = grade
        print(f"oggetto creato con successo: {name} {grade}")
        
    def __eq__(self,other):
        if isinstance(self, Student):
            if self.name == other.name and self.grade == other.grade:
                return True
            else:
                return False
        else:
            return False

            
s1 = Student("Alice",28)
s2 = Student("Alice",28)

print(s1 == s2)
