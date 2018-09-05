print("Jake Taylor's MiniRPG (C) 2018\n\n")

while True:
    try:
        userInput = int(input("1. New Game\n2. Quit\n\n"))
    except ValueError:
        print("\nSorry, that wasn't an option! ")
        continue
    else:
        break

def newGame():
    print("\nYou have begun an incredible journey...")

if userInput == 1:
    newGame()
else:
    quit()

def quit():
    quit()
