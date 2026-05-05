class Flyer:
    def fly(self):
        print("Flyer: Sto volando")

class Swimmer:
    def fly(self):
        print("Swimmer: Sto nuotando")


class Duck(Swimmer,Flyer):
    pass 


p = Duck()

p.fly()

#(Method Resolution Order)
print(Duck.mro()) #[<class '__main__.Duck'>, <class '__main__.Swimmer'>, <class '__main__.Flyer'>, <class 'object'>]