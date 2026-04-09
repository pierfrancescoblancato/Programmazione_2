lista_spesa = ["banane"]

if lista_spesa:
    print(f"you have to buy {lista_spesa}")
else:
    print("you havent to buy")
    
    
a = int(input("inserire l eta: "))

if(a < 18):
    is_adult = False
else:
    is_adult = True
    
is_ad = False if a < 18 else True
print(is_adult,is_ad)

