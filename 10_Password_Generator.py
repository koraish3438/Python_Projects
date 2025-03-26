import random

character_list = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
    'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W',
    'X', 'Y', 'Z',
]

number_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbol_list = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']

print("\nWelcome to password generator!\n")
user_char = int(input("How many letter you want in your password : "))
user_number = int(input("How many number you want in your password : "))
user_symbol = int(input("How many symbol you want in your password : "))

password_list = []

for i in range(1, user_char+1):
    char = random.choice(character_list)
    password_list += char
for j in range(1, user_number+1):
    num = random.choice(number_list)
    password_list += num
for k in range(1, user_symbol+1):
    sym = random.choice(symbol_list)
    password_list += sym

random.shuffle(password_list)

password_string = ""
for l in password_list:
    password_string += l

print(f"\nYour password is = {password_string}")