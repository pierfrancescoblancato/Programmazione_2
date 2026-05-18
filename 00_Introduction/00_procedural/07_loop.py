a = 0

# Un ciclo while che continua finché 'a' è minore o uguale a 10
while a <= 10:
    a += 1  # Incrementa 'a' di 1 a ogni iterazione
    
    # Verifica se 'a' è dispari usando l'operatore modulo (%)
    if a % 2 != 0:
        continue  # Salta il resto del ciclo e passa all'iterazione successiva
    
    # Questa riga viene eseguita solo se 'a' è pari
    print(a)
else:
    # Il blocco 'else' in un ciclo viene eseguito quando la condizione diventa falsa
    print("ciclo finito")
    
fruits = ["fragola","banana","cocco"]

# Metodo 1: Iterare direttamente sugli elementi (il più "Pythonico")
for fruit in fruits:
    print(fruit)
    
# Metodo 2: Iterare usando un indice e range()
# len(fruits) restituisce 3, quindi range(3) genera 0, 1, 2
for i in range(len(fruits)):
    print(f"elemento {i+1}: {fruits[i]}")

# Metodo 3: Usare enumerate()
# Questa è la pratica migliore quando servono sia l'indice che il valore
for i, el in enumerate(fruits):
    print(f"elemento {i+1}: {el}")