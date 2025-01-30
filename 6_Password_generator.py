import random
import string

def generate_password(min_length, numbers=True, special_characters=True):   # numbers and special_characters are optional
    letters = string.ascii_letters     # all letters
    digits = string.digits             # 0 - 9 digits
    special = string.punctuation       # all special characters

    characters = letters        # your password will compulsorily contain letters

    if numbers:         # if your password contains numbers
        characters += digits
    if special_characters:      # if your password contains special characters
        characters += special   

    password = ""
    meets_criteria = False
    has_number = False
    has_special = False

    while not meets_criteria or len(password) < min_length:
        new_char = random.choice(characters)
        password += new_char

        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True

        meets_criteria = True

        if numbers:
            meets_criteria = has_number
        if special_characters:
            meets_criteria = meets_criteria and has_special

    return password

min_length = int(input("Enter the minimum length: "))
has_number = input("Do you want to have numbers (y/n): ").lower() == "y"
has_special = input("Do you want to have special characters (y/n): ").lower() == "y"
password = generate_password(min_length, has_number, has_special)
print(f"The generated password is: {password}")
            