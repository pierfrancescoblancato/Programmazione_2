class Playlist:
    def __init__(self, name, pl_descr, songs=[]): 
        self.name = name
        self.pl_descr = pl_descr
        self.songs = songs
    
    def __add__(self, other):
        # Sovraccarica l'operatore + tra due Playlist
        if isinstance(other, Playlist):
            new_name = self.name + "+" + other.name
            new_pldescr = "unione delle 2 playlist"
            new_songs = self.songs + other.songs
            return (new_name, new_pldescr, new_songs)
    
    def __str__(self):
        # Stringa formattata per print() e str()
        a = f'''Titolo della playlist: {self.name}\n
        {self.pl_descr} \n
        questa playlist contiene esattamente {len(self.songs)} canzoni \n
        '''
        return a
        
pl1 = Playlist("estate 25", "boh", ['volare', 'maracaibo', 'danza kudouro'])
pl2 = Playlist("estate 26", "boh2", ['macarena', 'maracaibo', 'buoni o cattivi'])

pl3 = pl1 + pl2  
print(pl3)           # ('estate 25+estate 26', 'unione delle 2 playlist', ['volare', 'maracaibo', 'danza kudouro', 'macarena', ...])

print(type(pl3))     # <class 'tuple'>

# INTROSPECTION: capacità di esaminare oggetti a runtime
print(isinstance(pl1, Playlist))  # True (verifica il tipo)
print(isinstance(pl3, int))       # False

print(hasattr(pl1, "name"))        # True (verifica se esiste l'attributo)
print(hasattr(pl1, "promotion"))   # False

print(pl1.name)                     # Accesso diretto

# Introspection dinamica con input utente
a = input("get attribute: ")
if hasattr(pl1, a):
    print(getattr(pl1, a, "attributo non trovato"))  # Legge attributo dinamicamente
else:
    b = input("attribute not found, try: ")
    setattr(pl1, a, b)              # Crea/modifica attributo dinamicamente
print(getattr(pl1, a))