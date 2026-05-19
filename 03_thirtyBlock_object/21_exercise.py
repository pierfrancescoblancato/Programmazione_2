class Flyer:
    def fly(self):
        print("Flyer: Sto volando")

class Swimmer:
    def fly(self):
        print("Swimmer: Sto nuotando")


class Duck(Flyer, Swimmer):
    pass 


p = Duck()

p.fly()

# 3. Stampiamo l'MRO (Method Resolution Order)
print(Duck.mro())#[<class '__main__.Duck'>, <class '__main__.Flyer'>, <class '__main__.Swimmer'>, <class 'object'>]