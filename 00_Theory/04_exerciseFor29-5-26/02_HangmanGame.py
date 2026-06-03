guessWord =""
found = []
attemps = 3
display = ""

def gethiddenWords():
    for w in range(attemps):
        word = input("Enter word do you want guess: ").upper().strip()
        if word.isalpha() and len(word) > 1:
            return word
        print(f"word not valid: '{word}'. try.")
    print("Too many failed attempts. Program terminated.")
    exit()
    
def printAsterisks(inputLetter: str, hiddenWord: str):
    global display
    
    if not (inputLetter.isalpha() and len(inputLetter) == 1):
        print(f"Input not valid: '{inputLetter}'. Enter a single Letter.")
        return None
    
    if inputLetter in found:
        print(f"You already searched the letter '{inputLetter}'")
    else:
        found.append(inputLetter)
    
    display = ""
    for letter in hiddenWord:
        if letter in found:
            display += letter
        else:
            display += "*"
    
    print(f"the word to guess is: {display}")
    
    return inputLetter in hiddenWord

guessWord = gethiddenWords()
print(f"The word to guess is: {'*' * len(guessWord)}")

while True:
    letter = input("Enter a letter: ").upper().strip()
    
    result = printAsterisks(letter, guessWord)
    if result == True:
        print(f"The letter found: {found}")
    elif result == False:
        attemps -= 1
    else:  
        continue
    
    if attemps == 0:
        print(f"you have wrong three time, the game is finish")
        break
    if guessWord == display:
        print(f"You have win, the words is: {display}")
        break
    
    
    
Zoom automatico
●  stats (text)  
⚠ types e stats possono essere salvati come JSON serializzato in stringa 
 
🧱 Creature (Python) 
La classe Creature deve: 
●  accettare i dati nel costruttore tramite **dict  
●  poter essere inizializzata sia:  
○  dai dati scaricati dalla API  
○  dai dati letti dal database  
Esempio concettuale: 
creature = Creature(**data_dict) 
 
 
🔹 Reader HTTP 
Riutilizzare la logica del Creature Loader precedente: 
●  richiesta HTTP alla PokeAPI  
●  normalizzazione dei dati  
●  gestione degli errori con try / except  
Il Reader non deve: 
●  scrivere direttamente nel database  
●  restituire HTML  
 
🖥 Template richiesti 
1 ⃣ index.html 
Pagina principale dell’applicazione. 
Deve mostrare: 
●  elenco di tutti i Pokémon presenti nel database  
●  Una scheda (riquadro) per ciascun Pokémon con:  
○  nome e stats principali 
○  link per la modifica  
Inoltre deve contenere: 
●  un pulsante o link “Aggiungi Pokémon”  
 
2 ⃣ add.html 
Pagina con un form contenente: 
●  un solo campo input: nome_pokemon  
●  un pulsante di invio  
Comportamento: 
●  alla sottomissione del form:  
1.  viene fatta la richiesta HTTP alla API  
2.  i dati vengono salvati nel database  
3.  si viene reindirizzati alla pagina index  
 
3 ⃣ edit.html 
Pagina per modificare un Pokémon già presente. 
Deve permettere: 
●  visualizzazione dei dati attuali  
●  modifica di uno o più campi (es. peso, altezza)  
Alla conferma: 
●  i dati vengono aggiornati nel database  
●  redirect alla pagina index  
 
🔹 Route Flask richieste 
Almeno le seguenti: 
●  / 
 → mostra l’elenco dei Pokémon (index)  
●  /add 
 → GET: mostra il form  → POST: scarica i dati e salva nel DB  
●  /edit/<id> 
 → GET: mostra il form di modifica  → POST: aggiorna il record nel DB  
 
🧪 Gestione delle eccezioni (obbligatoria) 
Devono essere gestiti: 
●  Pokémon non trovato nella API  
●  errori di rete  
L’app non deve crashare:  mostrare un messaggio di errore o tornare alla pagina precedente. 
 
📦 Consegna richiesta 
●  progetto Flask funzionante  
●  file .py principali  
●  cartella templates/ con i file HTML  
●  file SQLite con almeno 3 Pokémon salvati  
 
📊 Criteri di valutazione 
Aspetto  Valutazione 
Architettura MVT   
Uso corretto di Flask   
Integrazione API esterna   
Persistenza su SQLite   
Uso corretto di template HTML   
Gestione degli errori   
 
Note finali 
●  L’obiettivo non è l’estetica, ma la logica  
●  Il progetto deve dimostrare la continuità con il Creature Loader precedente  
●  Codice chiaro > codice complesso  
 