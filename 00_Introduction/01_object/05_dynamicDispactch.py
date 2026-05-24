'''# DYNAMIC DISPATCH: ha senso ed è utile chiamare metodi di classi 
differenti con lo stesso nome perchè in caso di iterazioni ad esempio 
tra elementi differenti si potrà richiamare il metodo una volta sola (esempio alla riga 30)'''
class MotoCycle:
    def accelerate(self):
        print("la moto sta accelerando ")
    
class Car:  # class NomeClasse(NomeSuperClasse):
    def accelerate(self):
        print(f"la macchina sta accelerando ")

class Bici:
    def accelerate(self):
        print("la bici sta accelerando ")
        
lista = []  # rinominato da 'lists' per evitare conflitto con la funzione built-in

c1 = Car()
lista.append(c1)

m1 = MotoCycle()
lista.append(m1)

b1 = Bici()
lista.append(b1)

print(lista)  # stampa la lista di oggetti (indirizzi di memoria)

# Polimorfismo: ogni oggetto viene trattato in modo uniforme
# Python utilizza il duck typing: "se cammina come un'anatra e starnazza come un'anatra, allora è un'anatra"
for el in lista:
    el.accelerate()  # ogni oggetto esegue il proprio metodo accelerate