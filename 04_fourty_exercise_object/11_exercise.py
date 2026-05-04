class Student:
    def __init__(self,name):
        self.name = name
    
s = Student("Fabio")

if hasattr(s, 'age'):
        print(f"has attribute {'name'}")
else:
    print(f"missing attribute {'age'}")