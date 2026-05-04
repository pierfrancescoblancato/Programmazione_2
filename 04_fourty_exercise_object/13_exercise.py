class Student:
    def __init__(self,name):
        self.name = name

s = Student('giulia')
setattr(s,'age', 25)

print(s.__dict__)