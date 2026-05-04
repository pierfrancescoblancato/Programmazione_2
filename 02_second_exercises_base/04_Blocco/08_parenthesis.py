piove = True
ho_ombrello = False
ho_impermeabile = True

controllo_1 = piove or ho_ombrello and not ho_impermeabile


controllo_2 = (piove or ho_ombrello) and not ho_impermeabile

print(f"Risultato senza parentesi: {controllo_1}")
print(f"Risultato con parentesi:    {controllo_2}")