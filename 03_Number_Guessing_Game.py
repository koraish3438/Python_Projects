# import random
#
# def number_guessing_game():
#     print("Welcome to the Number Guessing Game!")
#     secret_number = random.randint(1, 100)
#     attempts = 0
#     max_attempts = 7
#
#     while attempts < max_attempts:
#         try:
#             guess = int(input(f"Attempt {attempts + 1}/{max_attempts} - Guess a number between 1 and 100: "))
#             attempts += 1
#
#             if guess < secret_number:
#                 print("Too low! Try again.")
#             elif guess > secret_number:
#                 print("Too high! Try again.")
#             else:
#                 print(f"Congratulations! You guessed the number in {attempts} attempts.")
#                 break
#         except ValueError:
#             print("Please enter a valid number!")
#
#     if attempts == max_attempts and guess != secret_number:
#         print(f"Sorry, you've used all {max_attempts} attempts. The correct number was {secret_number}.")
#
#
# if __name__ == "__main__":
#     number_guessing_game()


import random

def Number_Guessing_Game():
    print("Let's go....!")

    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 7

    while attempts < max_attempts:
        try:
            guess_number = int(input(f"Attempts is {attempts + 1}/{max_attempts} - guess a number in 1 to 100 : "))
            attempts += 1

            if guess_number < secret_number:
                print("Too low! try again.")
            elif guess_number > secret_number:
                print("Too high! try again.")
            else:
                print("Congratulation! you win..")
                break
        except ValueError:
            print("Please input the valid number : ")

    if attempts == max_attempts and guess_number != secret_number:
        print(f"Sorry, you've used all {max_attempts} attempts. The correct number was {secret_number}.")

if __name__ == "__main__":
    Number_Guessing_Game()