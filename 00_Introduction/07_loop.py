a = 0

while a <= 10:
    a += 1
    if a % 2 != 0:
        continue
    print(a)
else:
    print("ciclo finito")
    
fruits = ["fragola","banana","cocco"]

for fruit in fruits:
    print(fruit)
    
for i in range(len(fruits)):
    print(f"element {i+1}: {fruits[i]}")

for i, el in enumerate(fruits):
    print(f"element {i+1}: {el}")
