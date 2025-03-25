import random

words = ["apple", "grape", "lemon", "mango", "peach", "pear", "cake", "fish", "bread", "grape", "melon"]

chosen_word = random.choice(words)
print(chosen_word)

display = []

lives = 6
stages = ['''
    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
        |
===========
''','''
    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
        |
===========
''','''
    +---+
    |   |
    O   |
   /|\  |
        |
        |
        |
===========
''','''
    +---+
    |   |
    O   |
   /|   |
        |
        |
        |
===========
''','''
    +---+
    |   |
    O   |
    |   |
        |
        |
        |
===========
''','''
    +---+
    |   |
    O   |
        |
        |
        |
        |
===========
''','''
    +---+
    |   |
        |
        |
        |
        |
        |
===========
''']

# for letter in chosen_word:
#     display += '_'

for i in range(len(chosen_word)):# apple _____
    display.append('_')
print(display)

game_over = False
while not game_over:
    guessed_letter = input("Guess a letter : ").lower()
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guessed_letter:
            display[position] = guessed_letter
    print(display)

    if guessed_letter not in chosen_word:
        lives -= 1
        if lives == 0:
            game_over = True
            print("You loss!!")

    if '_' not in display:
        game_over = True
        print(f"Congratulation! You win. The word is {chosen_word}.")

    print(stages[lives])