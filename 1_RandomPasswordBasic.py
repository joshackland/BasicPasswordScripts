import random, string

characters = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
password = ""
PASSWORD_LENGTH = 16

for i in range(PASSWORD_LENGTH):
    password += characters[random.randint(0, len(characters)-1)]

print(password)