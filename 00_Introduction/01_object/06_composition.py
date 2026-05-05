class Avviamento:
    def start(self):
        print("il motore si e' avviato")

class AvviamentoElettronico(Avviamento):
    def start(self):
        print("avviamento eletronico")

class AvviamentoPedale(Avviamento):
    def start(self):
        print("il pedale funziona")

class Vehicle:
    def __init__(self,model,avviamento):
        self.model = model
        self.avviamento = avviamento
        
    def partenza(self):
        self.avviamento.start()

m1 = Vehicle('ktm',AvviamentoPedale())
m2 = Vehicle('Panda',AvviamentoElettronico())

m1.partenza()
m2.partenza()

m1.avviamento.start()