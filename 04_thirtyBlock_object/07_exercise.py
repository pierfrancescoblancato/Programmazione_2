class Course:
    def __init__(self, lista_studenti):
        self.students = lista_studenti

    def __len__(self):
        return len(self.students)


students = ["Alice", "Marco", "Sofia"]

c = Course(students)

print(len(c))  