import random, string

random_characters = ""
password_length = 0
password = ""

MINIMUM_PASSWORD_LENGTH = 8

#function to retrieve user's decision
def user_input_yes_no(message):
    option = input(message)
    while option not in "Yy " and option not in "nN":
        print("Invalid option.\nTo choose yes type either: 'y' 'Y' ' '\nTo choose no type either: 'n' 'N'.")
        option = input(message)
    return option

#user decides how complex the password will be
lowercase = user_input_yes_no("Do you want lowercase letters in the password? (Y/n): ")
uppercase = user_input_yes_no("Do you want uppercase letters in the password? (Y/n): ")
digits = user_input_yes_no("Do you want digits letters in the password? (Y/n): ")
punctuation = user_input_yes_no("Do you want punctuation letters in the password? (Y/n): ")

#user decides how long the password will be. must be greater than mimimum password length
while password_length <= MINIMUM_PASSWORD_LENGTH:
    password_length = int(input("Enter the length of the password (minimum 8): "))

#creating string of characters that may potentially be in the password
if lowercase in "yY ":
    characters += string.ascii_letters
if uppercase in "yY ":
    characters += string.ascii_uppercase
if digits in "yY ":
    characters += string.digits
if punctuation in "yY ":
    characters += string.punctuation

#randomly selects characters for password based on user requirements
for i in range(number):
    password += characters[random.randint(0, len(characters)-1)]

print(password)