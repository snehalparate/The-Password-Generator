import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''
    for i in range(length):
        password += random.choice(characters)
    return password

def main():
    print("=== Password Generator ===")
    
    user_input = input("Enter the desired password length: ")

    if not user_input.isdigit():
        print("Invalid input. Please enter a number.")
        return

    length = int(user_input)

    if length <= 0:
        print("Password length must be greater than zero.")
        return

    password = generate_password(length)
    print("Your generated password is:", password)

main()

