class Course:
    def __init__(self, name, lista_studenti):
        self.name = name
        self.students = lista_studenti

    def __add__(self, other):
        new_name = self.name + " + " + other.name
        new_list = self.students + other.students
        return Course(new_name, new_list)

    def __str__(self):
        return f"Corso {self.name} con studenti: {self.students}"


c1 = Course("front end", ["Alice", "Marco", "Sofia"])
c2 = Course("back end", ["Mirko", "Pier", "Matteo"])

c3 = c1 + c2

print(c3)