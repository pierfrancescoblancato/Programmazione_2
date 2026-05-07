class Student:
    def __init__(self,nome,voto):
        self.nome = nome
        self.voto = voto
        
students = [
    Student("Giulia",45),
    Student("Mirko",60),
    Student("Alessio",70)
]

for stud in students:
    if stud.voto >= 60:
        print(f"Studente: {stud.nome} promosso con voto: {stud.voto}")