counter = 0
while True:
    n = int(input("Enter a number (0: exit): "))
    if n == 0:
        print(f"Exit: Positive number entered: {counter}")
        break
    else:
        if n >= 0:
            counter += 1
