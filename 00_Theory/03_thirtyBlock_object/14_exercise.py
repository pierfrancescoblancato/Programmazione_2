class Person:
    def saluta(self):
        print("ciao a tutti!")

p = Person()

value = input("digit (saluta): ")
method = getattr(p, value)

method()