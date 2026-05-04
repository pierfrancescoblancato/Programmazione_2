#ricorsive function
def factorial(n):
    #caso base o condizione di uscita
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
       
    
factorial(3)