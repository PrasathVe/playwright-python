import random
import string
from string import digits

def generate_password(min_length, numbers=True, special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    character = letters
    if numbers:
        character += digits
    if special_characters:
        character += special
    pwd = ""
    meet_criteria = False
    has_numbers = False
    has_special = False

    while not meet_criteria or len(pwd) < min_length:
        new_char = random.choice(character)
        pwd += new_char

        if new_char in digits:
            has_numbers=True
        elif new_char in special:
            has_special = True

        meet_criteria = True
        if numbers:
            meet_criteria = has_numbers
        if special_characters:
            meet_criteria = meet_criteria and has_special
    return pwd
pwd = generate_password(10)
print(pwd)