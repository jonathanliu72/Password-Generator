# Author: Jonathan Liu
# Date: 10/25/24
# Purpose: Generates a random password (25% uppercase letters, 25% lowercase letters, 25% numbers, 25% special characters) given the parameter of how long a user wants the password to be and which characters to exlude

from string import ascii_uppercase, ascii_lowercase, digits, punctuation
from random import choices, shuffle
from math import floor

def password_generator()->str:
    try:
        while True:
            length = input("Enter desired length of password: ")
            if length.isdigit():
                length = int(length)
                break
            else:
                print("Please input an integer.")
                continue
        
        exclusions = []
        while True:
            exclude = input("Enter characters, numbers, or symbols you would like to exlude ('continue' to continue): ")
            if exclude == 'continue':
                break
            else:
                if len(exclude) > 1:
                    print("Please enter one at a time.")
                    continue
                exclusions.append(exclude)
        

        password_list = []
        password_list.extend(generate_uppercase(length, exclusions))
        password_list.extend(generate_lowercase(length, exclusions))
        password_list.extend(generate_number(length, exclusions))
        password_list.extend(generate_special_chars(length, exclusions))
        shuffle(password_list)
        password = ''.join(password_list)

        return password
    except RecursionError:
        print("Too many characters were entered to produce a secure password. Please try again.")
        return password_generator()



#Generates uppercase letters as a list
def generate_uppercase(length, exclusions):
    uppercase_letters = choices(ascii_uppercase, k = floor(length/4))
    if contains(uppercase_letters, exclusions):
        return generate_uppercase(length, exclusions)
    else:
        return uppercase_letters

#Generates lowercase letters as a list
def generate_lowercase(length, exclusions):
    lowercase_letters = choices(ascii_lowercase, k = floor(length/4))
    if contains(lowercase_letters, exclusions):
        return generate_lowercase(length, exclusions)
    else:
        return lowercase_letters


#Generates numbers as a list
def generate_number(length, exclusions):
    numbers = choices(digits, k = floor(length/4))
    if contains(numbers, exclusions):
        return generate_number(length, exclusions)
    else:
        return numbers
   
#Generates special characters as a list
def generate_special_chars(length, exclusions):
    special_chars = choices(punctuation, k = length - 3 * floor(length/4))
    if contains(special_chars, exclusions):
        return generate_special_chars(length, exclusions)
    else:
        return special_chars
    

#Checks if password segment contains omitted characters
def contains(pswd_segment, exclusions):
    for char in pswd_segment:
        if char in exclusions:
            return True
    return False

#Test case
print(password_generator())