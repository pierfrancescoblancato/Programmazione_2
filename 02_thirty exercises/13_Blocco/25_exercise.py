numbers = [12, -5, 18, 7, 25, -2, 45, 11,0]

print("Filtering results:")

for num in numbers:
    if num == 0:
        break
    
    if num < 0:
        continue
    
    if num > 10:
        print(num)