# name = input("Enter your name : ")
# fatherName = input("Enter your father name : ")
# motherName = input("Enter your mother name : ")
# address = input("Enter your address : ")
# study = input("Which class do you read in : ")
#
# story = f"{name}, you are a mad. Your father {fatherName} is a "
#
# print("/nHere is your mad libs story:")

print("Start Mad Libs!")

name = input("Enter your name: ")
father_name = input("Enter your father's name: ")
mother_name = input("Enter your mother's name: ")
address = input("Enter your address: ")
study = input("What are you studying?: ")

story = f"{name} is a very funny person. \nTheir father's name is {father_name} and \ntheir mother's name is {mother_name}. They live in {address}. {name} is currently studying {study}. \nOne day, while walking down the street, a cat suddenly sat next to them and said, 'Why so serious?' Everyone started laughing!"

print("\nYour funny story:")
print(story)
