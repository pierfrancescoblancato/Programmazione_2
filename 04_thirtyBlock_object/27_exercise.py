lists = [1,2,3,4,5,6,7,8,9,10] 
def printEvenNumber(lists):
    for el in lists:
        if el % 2 == 0:
            print(f"Numero pari trovato: {el}")
            
printEvenNumber(lists)