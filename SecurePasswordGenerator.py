# Author: Jonathan Liu
# Date: 10/25/24
# Purpose: Generates a random password (25% uppercase letters, 25% lowercase letters, 25% numbers, 25% special characters) given the parameter of how long a user wants the password to be and which characters to exclude
import os
import hashlib
import base64
from cryptography.fernet import Fernet
from string import ascii_uppercase, ascii_lowercase, digits, punctuation
from random import choices, shuffle
from math import floor

class SecurePasswordGenerator:
    def __init__(self):
        self.encryption_key = Fernet.generate_key()  # Key for AES encryption
        self.cipher = Fernet(self.encryption_key)

    def generate_password(self, length=16, exclusions=None):
        if exclusions is None:
            exclusions = []
        
        password_list = []
        password_list.extend(self.generate_uppercase(length, exclusions))
        password_list.extend(self.generate_lowercase(length, exclusions))
        password_list.extend(self.generate_number(length, exclusions))
        password_list.extend(self.generate_special_chars(length, exclusions))
        shuffle(password_list)
        password = ''.join(password_list)
        
        hashed_password, salt = self.hash_password(password)
        encrypted_password = self.encrypt_password(password)
        
        return {
            "plaintext": password,
            "hashed": hashed_password,
            "salt": salt,
            "encrypted": encrypted_password.decode(),
            "encryption_key": self.encryption_key.decode()
        }
    
    def generate_uppercase(self, length, exclusions):
        return self.get_valid_chars(ascii_uppercase, length // 4, exclusions)
    
    def generate_lowercase(self, length, exclusions):
        return self.get_valid_chars(ascii_lowercase, length // 4, exclusions)
    
    def generate_number(self, length, exclusions):
        return self.get_valid_chars(digits, length // 4, exclusions)
    
    def generate_special_chars(self, length, exclusions):
        return self.get_valid_chars(punctuation, length - 3 * (length // 4), exclusions)
    
    def get_valid_chars(self, character_set, count, exclusions):
        valid_chars = [char for char in character_set if char not in exclusions]
        return choices(valid_chars, k=count) if valid_chars else []
    
    def hash_password(self, password):
        salt = os.urandom(16)  # Generate a random 16-byte salt
        hashed_pw = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)
        return base64.b64encode(hashed_pw).decode(), base64.b64encode(salt).decode()
    
    def encrypt_password(self, password):
        return self.cipher.encrypt(password.encode())
    
    def decrypt_password(self, encrypted_password, key):
        cipher = Fernet(key)
        return cipher.decrypt(encrypted_password).decode()

# Test Case
generator = SecurePasswordGenerator()
password_data = generator.generate_password(16)

print("Generated Password:", password_data["plaintext"])
print("Hashed Password:", password_data["hashed"])
print("Salt:", password_data["salt"])
print("Encrypted Password:", password_data["encrypted"])
print("Encryption Key:", password_data["encryption_key"])  # Store this safely!
