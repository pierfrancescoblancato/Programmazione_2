age = int(input("Eta: "))

if(age < 18):
    print("arricogghiti")
else:
    if(age < 35):
        print("membro junior")
    elif(age >= 35 and age <= 50):
        print("membro mid")
    else:
        print("membro senior")