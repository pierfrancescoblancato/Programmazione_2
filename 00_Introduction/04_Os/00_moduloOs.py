import os 

a = os.getcwd()#cartella di lavoro attuale

print("cartella corrente ",a )

print("cartelle e file: ", os.listdir()) # list di cartelle nel ambiente di lavoro

#if 'requirements.txt' in os.listdir():
    
#os.mkdir('andrea') creare una cartella

#os.rmdir('andrea')#eliminare una cartella, elimina solo se la cartella e' vuota


os.chdir('andrea')
