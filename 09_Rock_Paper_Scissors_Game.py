import random

user_choice = int(input("\nEnter your choice, \nType 0 for Rock, 1 for Paper, 2 for Scissor : "))

if user_choice >= 3 or user_choice < 0:
    print("Choice invalid number. You loss!")
else:
    computer_choice = random.randint(0,2)
    print(f"Computer choice {computer_choice}")

    if computer_choice == user_choice:
        print("It's Draw!")
    elif computer_choice == 2 and user_choice == 0:
        print("You win!")
    elif computer_choice == 0 and user_choice == 1:
        print("You loss!")
    elif user_choice > computer_choice:
        print("You win!")
    elif computer_choice > user_choice:
        print("You loss!")