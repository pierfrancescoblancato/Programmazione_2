class Playlist:
    def __init__(self, name, pl_descr, songs = []):
        self.name = name
        self.pl_descr = pl_descr
        self.songs = songs
    
    def __add__(self, other):
        if isinstance(other, Playlist):
            new_name = self.name + "+" + other.name
            new_pldescr = "unione delle 2 playlist"
            new_songs = self.songs + other.songs
            return (new_name, new_pldescr, new_songs)  # ATTENZIONE: restituisce una tupla, non una Playlist!
    
    def __str__(self):
        # CORREZIONE: era self.song, ma l'attributo si chiama self.songs
        a = f'''Titolo della playlist: {self.name}\n
        {self.pl_descr} \n
        questa playlist contiene esattamente {len(self.songs)} canzoni \n
        '''
        return a
        
pl1 = Playlist("estate 25", "boh", ['volare', 'maracaibo', 'danza kudouro'])
pl2 = Playlist("estate 26", "boh2", ['macarena', 'maracaibo', 'buoni o cattivi'])

pl3 = pl1 + pl2  # pl3 è una tupla, non un oggetto Playlist
print(pl3)

print(type(pl3))  # <class 'tuple'>

# introspection serve per dialogare dinamicamente con il codice
print(isinstance(pl1, Playlist))  # True
print(isinstance(pl3, int))       # False

print("has title?", hasattr(pl1, "name"))       # True
print("has promotion?", hasattr(pl1, "promotion"))  # False

print(pl1.name)
a = input("get attribute: ")
if hasattr(pl1, a):
    print(getattr(pl1, a, "attributo non trovato"))
else:
    b = input("attribute not found, try: ")
    setattr(pl1, a, b)
print(getattr(pl1, a))