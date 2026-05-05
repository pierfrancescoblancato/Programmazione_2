#try catch
#funzionamento: runna il programma tranquillamente se non trova problemi, senno va in eccezione senza bloccare il programma
try:
    a = int(input("number: "))
    b = 5/a
    print(b)
    
    #tutto ok
except ZeroDivisionError:
    print("ZeroDivisionError: non e' possibile dividere per 0") # prima si prova a catturare gli errori specifici 
except ArithmeticError:
    print("ArithmeticError: errore generico") # poi si prova a catturare gli errori genericic 
except ValueError:
    print("ValueError: non e' possibile inserire un carattere")
else:
    print("andato a buon fine") #si attiva solo se il try va tutto a buon fine senza catturare eccezioni
finally:
    print("si attiva in ogni caso")#si attiva quando va tutto bene e anche quando va male (in ogni caso)