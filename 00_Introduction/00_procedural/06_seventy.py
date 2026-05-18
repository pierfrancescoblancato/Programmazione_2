# Inizializza una lista con un elemento
lista_spesa = ["banane"]

# Controllo di truthiness: una lista vuota [] è False, una lista con elementi è True
if lista_spesa:
    print(f"devi comprare {lista_spesa}")
else:
    # Questo viene eseguito solo se la lista è vuota
    print("non devi comprare nulla")
    
# Richiede un input all'utente e lo converte in un intero
a = int(input("inserire l eta: "))

# Blocco if-else standard per determinare la maggiore età
if(a < 18):
    is_adult = False
else:
    is_adult = True
    
# Operatore ternario: una versione compatta in una riga dell'if-else sopra
# Sintassi: [valore_se_vero] if [condizione] else [valore_se_falso]
is_ad = False if a < 18 else True

# Stampa entrambi i risultati per verificare che siano identici
print(is_adult, is_ad)