import random

diceRolling = True

while diceRolling:
    print(random.randint(1,6))
    playAgain = input("Do you play again? say [yes/no] : ")
    if playAgain == "yes":
        continue
    else:
        print("Game over!")
        break