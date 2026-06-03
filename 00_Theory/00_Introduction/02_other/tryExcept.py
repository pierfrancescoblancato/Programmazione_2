# TRY/EXCEPT - Gestione delle eccezioni
# funzionamento: esegue il programma tranquillamente se non trova problemi,
# altrimenti va in eccezione senza bloccare il programma
try:
    a = int(input("Inserisci un numero: "))
    b = 5 / a
    print(f"Risultato: {b}")
    
    # tutto ok

# Cattura errori SPECIFICI (ordine IMPORTANTE: prima i più specifici)
except (ZeroDivisionError, ValueError) as e:
    print(f"Error {e}: errore di input, {type(e)}")
    print(f"Error {str(e)}: errore di input, {repr(e)}")
    # raise ZeroDivisionError("non si può dividere per 0")  # ATTENZIONE: raise dentro except è spesso indesiderato

# Cattura errori GENERICI (dopo quelli specifici)
except ArithmeticError:
    print("ArithmeticError: errore generico")  # Copre ZeroDivisionError, OverflowError, FloatingPointError
except ValueError:
    print("ValueError: non è possibile inserire un carattere")  # MAI RAGGIUNTO (già catturato sopra)

else:
    print("andato a buon fine")  # Si attiva SOLO se il try va a buon fine (nessuna eccezione)

finally:
    print("si attiva in ogni caso")  # Sempre eseguito (successo o errore)


# ECCEZIONI PERSONALIZZATE (Custom Exceptions)

class ErrorVehicle(Exception):
    """Eccezione personalizzata per veicoli"""
    def __init__(self, message="vehicle is broken"):
        super().__init__(message)  # self.message è disponibile automaticamente

# ESEMPIO DI UTILIZZO

# Definizione della classe Vehicle (mancava nell'esempio originale)
class Vehicle:
    doors = 4  # Attributo di classe (esempio)

# Esempio corretto di lancio dell'eccezione personalizzata
try:
    a = int(input("Inserisci un numero di porte: "))
    # Vehicle.doors esiste ora come attributo di classe
    if a > 9:
        #raise serve a lanciare (generare) un'eccezione in modo esplicito
        raise ErrorVehicle("Troppe porte per un veicolo normale!")
    else:
        print(f"Numero di porte accettabile: {a}")
        
except ErrorVehicle as e:
    print(f"Errore personalizzato catturato: {e}")
    
except ValueError:
    print("Devi inserire un numero valido!")