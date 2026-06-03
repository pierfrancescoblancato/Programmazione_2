lists = input("inserisci una frase: ").strip().split()

for l in lists:
    if l.isalpha():
        print(len(l))
    