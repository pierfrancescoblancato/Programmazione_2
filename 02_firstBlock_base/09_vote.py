vote = int(input("enter a vote between 1 and 100: "))


if vote < 60:
    print("Fail")
elif vote >= 60 and vote <= 79:
    print("Pass")
elif vote >= 80 and vote <= 100:
    print("Excellent")
else:
    print("ERROR: try again")