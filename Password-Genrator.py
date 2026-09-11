import random
import string

def generate_password(length):
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    all_characters = letters + digits + symbols

    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password

print("Welcome to the password genarated by KAJU!!")
try:
    length = int(input("Enter the length of your password: "))
    if length < 4:
        print("The length of your password should be greater than 4.")
    else:
        generated = generate_password(length)
        print(f"Your secure password is {generated}. ")
except ValueError:
    print("Please enter a valid number !!!")
