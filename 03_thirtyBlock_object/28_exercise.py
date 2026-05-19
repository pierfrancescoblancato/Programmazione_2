lists = [1,2,3,4,5,6,7,8,9,10] 
evenLists = []
def printEvenNumber(lists):
    for el in lists:
        if el % 2 == 0:
            evenLists.append(el)
            print(f"Numero pari trovato: {el}")
    print(f"lista con solo numeri pari: {evenLists}")
           
printEvenNumber(lists)
