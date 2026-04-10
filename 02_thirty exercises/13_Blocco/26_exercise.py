user_in = input("Enter the username: ")
pass_in = input("Enter the password: ")

if user_in and len(pass_in) >= 6:
    print("LogIn: Valid!")
else:
    print("LogIn: Invalid. Ensure username is not empty and password is 6+ chars.")