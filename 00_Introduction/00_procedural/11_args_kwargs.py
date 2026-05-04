# *ARGS: Argomenti Posizionali Variabili

# L'asterisco singolo (*) davanti a 'names' è la vera magia.
# Dice a Python: "Prendi tutti i valori sciolti che l'utente inserisce e 
# impacchettali insieme dentro una Tupla chiamata 'names'".
def roll_call(*names):
    
    # Se stampiamo 'names' nudo e crudo, vedremo le parentesi tonde tipiche delle Tuple.
    # Ad esempio: ("Gianmaria", "Franco")
    print("Raw values received:", names)
    print("Here is who is present today:")
    
    # Essendo una Tupla, si comporta come una lista. Quindi possiamo 
    # usare un ciclo for per estrarre e stampare un nome alla volta.
    for name in names:
        print("-", name)

print("--- First day ---")
# Qui passiamo un solo elemento. 'names' diventerà la tupla ("Gianmaria",)
roll_call("Gianmaria")

print("\n--- Second day ---")
# Qui passiamo due elementi. La funzione non va in errore perché *names è flessibile!
roll_call("Gianmaria", "Franco")

print("\n--- Third day ---")
# Possiamo passarne quanti ne vogliamo, la funzione li impacchetterà tutti.
roll_call("Gianmaria", "Franco", "Anna", "Mirko")


# **KWARGS: Keyword Arguments

# I due asterischi (**) davanti a 'amesquastra' dicono a Python: 
# "Prendi tutti gli argomenti passati con un nome (chiave=valore) e 
# impacchettali insieme dentro un Dizionario".
def team(**amesquastra):
    
    # 'amesquastra' ora è un vero e proprio dizionario. 
    # Il metodo .keys() ci permette di estrarre solo la prima parte (le chiavi/i ruoli).
    print("ruoli previsti:", amesquastra.keys())
    print("ve la presento meglio: ")
    
    # Il metodo .items() estrae la coppia completa, così nel ciclo for 
    # 'role' prende la chiave (es. 'founder') e 'name' prende il valore (es. 'gianmarco').
    for role, name in amesquastra.items():
        print(role,":",name)

print("\n--- Team 1 ---")
# Creerà il dizionario: {'founder': 'gianmarco'}
team(founder="gianmarco")

print("\n--- Team 2 ---")
# Creerà il dizionario: {'founder': 'gianmarco', 'cofounder': 'ciccio'}
team(founder="gianmarco", cofounder = "ciccio")

print("\n--- Team 3 ---")
# Puoi aggiungere tutti i ruoli che vuoi inventandoti il nome al momento!
team(founder="gianmarco", cofounder = "ciccio", ambassador="mirko")