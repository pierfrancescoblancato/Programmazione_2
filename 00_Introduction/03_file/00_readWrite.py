file="00_Introduction/03_file/assets/text.txt"

#lettura
# apertura di un file
file_stream = open(file,'r') # read: r default , write: w, append: w
content = file_stream.readline() 
print(content)

file_stream.close()
with open(file,'r') as f: # read = intero testo, readline = riga per riga, readlines = lista di righe
    content1 = f.read()
    content2 = f.readline()
    content3 = f.readlines()
    
print(content1,content2,content3)

#scrittura = write
with open(file,'w') as f:
    newText = '''1) questo e' un nuovo testo 
    che andra a sovrascriversi
    '''
    f.write(newText) # write = sovrascrive il file, writelines = scrive una lista

#scrittura = append
with open(file,'a') as f:
    newText = '''
    2) questo e' un nuovo testo 
    che andra alla fine ad appendersi
    '''
    f.write(newText)
    
lists = ['questa ','e`',' una lista ']
with open(file,'a') as f:
    f.writelines(lists)
   
   
# t = text; b = binary
'''
a at ab
r rt rb
w wt wb
'''
