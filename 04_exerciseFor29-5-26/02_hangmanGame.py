guessWord =""
found = []
attemps = 3
display = ""

def gethiddenWords():
    for w in range(3):
        word = input("Enter word do you want guess: ").upper().strip()
        if word.isalpha() and len(word) > 1:
            return word
        print(f"word not valid: '{word}'. try.")
    print("Too many failed attempts. Program terminated.")
    exit()
    
def printAsterisks(inputLetter: str, hiddenWord: str):
    global display
    
    if not (inputLetter.isalpha() and len(inputLetter) == 1):
        print(f"Input not valid: '{inputLetter}'. Enter a single Letter.")
        return None
    
    if inputLetter in found:
        print(f"You already searched the letter '{inputLetter}'")
    else:
        found.append(inputLetter)
    
    display = ""
    for letter in hiddenWord:
        if letter in found:
            display += letter
        else:
            display += "*"
    
    print(f"the word to guess is: {display}")
    
    return inputLetter in hiddenWord

guessWord = gethiddenWords()
print(f"The word to guess is: {'*' * len(guessWord)}")

while True:
    letter = input("Enter a letter: ").upper().strip()
    
    result = printAsterisks(letter, guessWord)
    if result == True:
        print(f"The letter found: {found}")
    elif result == False:
        attemps -= 1
    else:  # risultato è None
        continue
    
    if attemps == 0:
        print(f"you have wrong three time, the game is finish")
        break
    if guessWord == display:
        print(f"You have win, the words is: {display}")
        break