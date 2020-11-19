from hashlib import sha256

#enter password and retrieve the SHA256 hash of it
user_password = input('Enter a password: ')
password_hash = sha256(user_password.encode('utf-8')).hexdigest()
print("The entered password has a SHA256 hash of: " + password_hash)


#enter password to compare with stored password hash
password_attempt = input("Enter your password: ")
password_attempt_hash = sha256(password_attempt.encode('utf-8')).hexdigest()

print(f"The password \"{password_attempt}\" has a SHA256 value of {password_attempt_hash}")

if (password_attempt_hash == password_hash):
    print("That was the correct password!")
else:
    print("Incorrect password!")