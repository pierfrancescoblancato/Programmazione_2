#try catch
#funzionamento: runna il programma tranquillamente se non trova problemi, senno va in eccezione senza bloccare il programma
try:
    a = int(input("number: "))
    b = 5/a
    print(b)
    
    #tutto ok
except (ZeroDivisionError, ValueError) as e: #prima si prova a catturare gli errori specifici 
    print(f"Error {e}: errore di input, {type(e)}")  #l'errore si puo conservare in una variabile poiche e' un' oggetto
    print(f"Error {str(e)}: errore di input, {repr(e)}")
    raise ZeroDivisionError("non si puo dividere per 0")
except ArithmeticError:
    print("ArithmeticError: errore generico") # poi si prova a catturare gli errori genericic 
except ValueError:
    print("ValueError: non e' possibile inserire un carattere")
else:
    print("andato a buon fine") #si attiva solo se il try va tutto a buon fine senza catturare eccezioni
finally:
    print("si attiva in ogni caso")#si attiva quando va tutto bene e anche quando va male (in ogni caso)


class ErrorVehicle(Exception): #errori custom
    def __init__(self,message = "vehicle is broken"):
        super().__init__(*message)
        
a = input()
if Vehicle.doors > 9:
    raise ErrorVehicle()