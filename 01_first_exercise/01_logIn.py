username = "admin"
password = "123abc"

access = False

for i in range(3):
    userIn = input("Enter the username: ")
    passIn = input("Enter the password: ")

    clearPassIn = passIn.strip().lower()

    if username == userIn and password == clearPassIn:
        access = True
        break
    else:
        print(f"LogIn: ERROR! Attempts remaining: {2 - i}")

if access:
    print("LogIn: Successful!")
else:
    print("LogIn: ERROR, you have made too many failed attempts!")