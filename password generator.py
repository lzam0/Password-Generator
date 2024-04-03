import random as r
import string
import re

def GeneratePassword():
    password_array = []

    # Iterate twice to make a password length of 8
    for i in range(r.randint(1,3)):

        # Generate lower case letters
        letters = string.ascii_lowercase
        lower_case_letters = ''.join(r.choice(letters) for i in range(1))

        # Generate upper case letters
        letters = string.ascii_uppercase
        upper_case_letters = ''.join(r.choice(letters) for i in range(1))

        # Generate numbers
        letters = string.digits
        num = ''.join(r.choice(letters) for i in range(1))

        # Generate punctuation
        letters = string.punctuation
        punc = ''.join(r.choice(letters) for i in range(1))

        # Append to password array
        password_array.extend([lower_case_letters, upper_case_letters, num, punc])

    r.shuffle(password_array)

    password = ''.join(password_array)
    return password


def CheckPassword(password):

    # Check if length is long enough
    length_enough = len(password) >= 8
    # Check if there are any lowercase letters in the string
    has_lower = any(char.islower() for char in password)
    
    # Check if there are any uppercase letters in the string
    has_upper = any(char.isupper() for char in password)

    # Check if any character in the string is a punctuation character
    has_num = any(char.isdigit() for char in password)

    # Check if any character in the string is a punctuation character
    has_punc =  any(char in string.punctuation for char in password)

    # I want this to basically check if the password is actually secure
    if(length_enough and has_lower and has_upper and has_punc and has_num):
        print("Passowrd is Secure")
    else:
        print("Passowrd is not Secure")

my_password = GeneratePassword()
print(my_password)
CheckPassword(my_password)