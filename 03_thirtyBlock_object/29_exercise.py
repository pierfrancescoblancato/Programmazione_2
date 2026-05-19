#Procedurale
numbers = [5, 12, 8, 21, 7, 10, 15]

def filterProcedural(data):
    results1 = []
    for n in data:
        if n > 10:
            results1.append(n)
    return results1

print(f"Procedurale: {filterProcedural(numbers)}")

#OOP
class NumberFilter:
    results2 =[]
    def __init__(self, data):
        self.data = data
    
    def Filter(self, threshold):
        for n in self.data:
            if n > threshold:
                self.results2.append(n)
        return self.results2

# Utilizzo
numberGreater = NumberFilter([5, 12, 8, 21, 7, 10, 15])
print(f"OOP: {numberGreater.Filter(10)}")


#Funzionale
numbers = [5, 12, 8, 21, 7, 10, 15]

# Usiamo la funzione 'filter' con una 'lambda' (funzione anonima veloce)
result_functional = list(filter(lambda n: n > 10, numbers))

print(f"Funzionale: {result_functional}")