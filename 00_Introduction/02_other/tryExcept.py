# try catch
# funzionamento: esegue il programma tranquillamente se non trova problemi, altrimenti va in eccezione senza bloccare il programma
try:
    a = int(input("number: "))
    b = 5 / a
    print(b)
    
    # tutto ok
except (ZeroDivisionError, ValueError) as e:  # prima si prova a catturare gli errori specifici
    print(f"Error {e}: errore di input, {type(e)}")  # l'errore si può conservare in una variabile poiché è un oggetto
    print(f"Error {str(e)}: errore di input, {repr(e)}")
    raise ZeroDivisionError("non si può dividere per 0")
except ArithmeticError:
    print("ArithmeticError: errore generico")  # poi si prova a catturare gli errori generici
except ValueError:
    print("ValueError: non è possibile inserire un carattere")
else:
    print("andato a buon fine")  # si attiva solo se il try va tutto a buon fine senza catturare eccezioni
finally:
    print("si attiva in ogni caso")  # si attiva quando va tutto bene e anche quando va male (in ogni caso)


class ErrorVehicle(Exception):  # errori custom
    def __init__(self, message="vehicle is broken"):
        super().__init__(*message)  # NOTA: *message è probabilmente un errore; dovrebbe essere message senza *
        
a = input()
# NOTA: Vehicle non è definita nell'esempio; questo codice presuppone un attributo di classe 'doors'
if Vehicle.doors > 9:
    raise ErrorVehicle()