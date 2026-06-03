# funzione ricorsiva
def factorial(n):
    # caso base o condizione di uscita
    if n == 0:
        return 1
    else:
        # passo ricorsivo: n * fattoriale di (n-1)
        return n * factorial(n-1)
    
print(factorial(998))
# Calcolo passo passo:
# factorial(3) = 3 * factorial(2)
# factorial(2) = 2 * factorial(1)
# factorial(1) = 1 * factorial(0)
# factorial(0) = 1
# Risultato: 3 * 2 * 1 * 1 = 6