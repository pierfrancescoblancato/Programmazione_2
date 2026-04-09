username = "admin"
password = "123abc"
Attempts = 3
access = False

for i in range(Attempts):
    userIn = input("Enter the username: ")
    passIn = input("Enter the password: ")

    clearPassIn = passIn.strip().lower()
    if username == userIn and password == clearPassIn:
        access = True
        break
    else:
        print(f"LogIn: ERROR! Attempts remaining: {(Attempts-1) - i}")

if access:
    print("LogIn: Successful!")
else:
    print("LogIn: ERROR, you have made too many failed attempts!")