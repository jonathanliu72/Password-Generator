# Author: Jonathan Liu
# Date: 10/25/24
# Purpose: Generates a random password (25% uppercase letters, 25% lowercase letters, 25% numbers, 25% special characters) given the parameter of how long a user wants the password to be

from string import ascii_uppercase, ascii_lowercase, digits, punctuation
from random import choices, shuffle
from math import floor

def password_generator(length:int)->str:

    password_list = []
    password_list.extend(generate_uppercase(length))
    password_list.extend(generate_lowercase(length))
    password_list.extend(generate_number(length))
    password_list.extend(generate_special_chars(length))
    shuffle(password_list)
    password = ''.join(password_list)

    return password

#Generates uppercase letters as a list
def generate_uppercase(length):
    uppercase_letters = choices(ascii_uppercase, k = floor(length/4))
    return uppercase_letters

#Generates lowercase letters as a list
def generate_lowercase(length):
    lowercase_letters = choices(ascii_lowercase, k = floor(length/4))
    return lowercase_letters

#Generates numbers as a list
def generate_number(length):
    numbers = choices(digits, k = floor(length/4))
    return numbers

#Generates special characters as a list
def generate_special_chars(length):
    special_chars = choices(punctuation, k= length - 3 * floor(length/4))
    return special_chars

#Test case
print(password_generator(10))
print("Password generation complete!")