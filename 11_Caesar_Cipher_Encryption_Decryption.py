character_list = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
    'x', 'y', 'z'
]

def encryption(plain_message, shift_key):
    cipher_message = ""
    for char in plain_message:
        if char in character_list:
            position = character_list.index(char)
            new_position = (position + shift_key) % 26
            cipher_message += character_list[new_position]
        else:
            cipher_message += char
    print(f"Here's is your encrypted message : {cipher_message}")

def decryption(cipher_message, shift_key):
    plain_message = ""
    for char in cipher_message:
        if char in character_list:
            position = character_list.index(char)
            new_position = (position - shift_key)  % 26
            plain_message += character_list[new_position]
        else:
            plain_message += char
    print(f"Here's is your encrypted message : {plain_message}")

wanna_end = False
while not wanna_end:
    what_you_want = input("\nWhat do you want? \nType 'encrypt' for encryption and 'decrypt' for decryption\nand 'stop' for Exit : ")
    if what_you_want == "encrypt":
        message = input("Enter your message : ").lower()
        shift = int(input("Enter shift number : "))
        encryption(plain_message=message, shift_key=shift)
    elif what_you_want == "decrypt":
        message = input("Enter your message : ").lower()
        shift = int(input("Enter shift number : "))
        decryption(cipher_message=message, shift_key=shift)
    elif what_you_want == 'stop':
        wanna_end = True
        print("Ok! See you later.. Good bey.. Have a nice day..")
    else:
        print("Please enter valid input for Caesar Cipher! Thank you..")
        play_again = input("Type 'yes' for Continue. and 'no' for Exit. : ")
        if play_again == 'no':
            wanna_end = True
            print("Ok! See you later.. Good bey.. Have a nice day..")
