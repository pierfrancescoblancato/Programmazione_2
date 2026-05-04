class Playlist:
    def __init__(self, name, pl_descr, songs = []):
        self.name =name
        self.pl_descr = pl_descr
        self.songs  = songs
    
    def __add__(self, other):
        if isinstance(other,Playlist):
            new_name= self.name + "+" + other.name
            new_pldescr = "unione delle 2 playlist"
            new_songs = self.songs + other.songs
        return(new_name, new_pldescr, new_songs )
    
    def __str__(self):
        a = f'''Titolo della playlist: {self.name}\n
        {self.pl_descr} \n
        questa playlist contiene esattamente {len(self.song)} canzoni \n
        '''
        return a
        
pl1 = Playlist("estate 25","boh",['volare','maracaibo','danza kudouro'])
pl2 = Playlist("estate 26","boh2",['macarena','maracaibo','buoni o cattivi'])

pl3 = pl1 + pl2
print(pl3)

print(type(pl3))

#introspection serve per dialogare dinamicamente con il codice
print(isinstance(pl1,Playlist))
print(isinstance(pl3,int))

print("has title?", hasattr(pl1, "name"))
print("has promotion?", hasattr(pl1, "promotion"))


print(pl1.name)
a = input("get attribute: ")
if hasattr(pl1, a):
    print(getattr(pl1, a, "attributo non trovato"))
else:
    b = input("attribute not found, try: ")
    setattr(pl1, a, b)
print(getattr(pl1,a))