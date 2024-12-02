# Author: Jonathan Liu
# Date: 10/25/24
# Purpose: Generates a random password (25% uppercase letters, 25% lowercase letters, 25% numbers, 25% special characters) given the parameter of how long a user wants the password to be

from string import ascii_uppercase, ascii_lowercase, digits, punctuation
from random import choices, shuffle
from math import floor

def password_generator()->str:

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
        exclude = input("Enter characters, numbers, or symbols you would like to exlude ('quit' to quit): ")
        if exclude == 'quit':
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

#Generates uppercase letters as a list
def generate_uppercase(length, exclusions):
    uppercase_letters = choices(ascii_uppercase, k = floor(length/4))
    return omit(uppercase_letters, exclusions)

#Generates lowercase letters as a list
def generate_lowercase(length, exclusions):
    lowercase_letters = choices(ascii_lowercase, k = floor(length/4))
    return omit(lowercase_letters, exclusions)

#Generates numbers as a list
def generate_number(length, exclusions):
    numbers = choices(digits, k = floor(length/4))
    return omit(numbers, exclusions)

#Generates special characters as a list
def generate_special_chars(length, exclusions):
    special_chars = choices(punctuation, k = length - 3 * floor(length/4))
    return omit(special_chars, exclusions)
    

#Omits characters
def omit(pswd_segment, exclusions):
    while True:
        for char in exclusions:
            if char in pswd_segment:
                continue
        break
    return pswd_segment

#Test case
print(password_generator())