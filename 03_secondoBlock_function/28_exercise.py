def avg(lista_voti):
    if not lista_voti: 
        return 0
    return sum(lista_voti) / len(lista_voti)

votes = [45, 65, 80, 30, 95, 58, 60, 72, 100, 42]

sufficient_votes = [vote for vote in votes if vote >= 60]

averange = avg(sufficient_votes)

print(f"Voti iniziali: {votes}")
print(f"Voti filtrati (>= 60): {sufficient_votes}")
print(f"La media dei voti filtrati è: {averange:.2f}")