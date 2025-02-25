import re
import SecurePasswordGenerator

class PasswordStrengthChecker:
    @staticmethod
    def check_strength(password):
        strength_criteria = {
            "length": len(password) >= 8,
            "uppercase": bool(re.search(r"[A-Z]", password)),
            "lowercase": bool(re.search(r"[a-z]", password)),
            "digit": bool(re.search(r"\d", password)),
            "special": bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))
        }
        
        score = sum(strength_criteria.values())
        
        if score == 5:
            return "Strong"
        elif score >= 3:
            return "Medium"
        else:
            return "Weak"

# Test Case
generator = SecurePasswordGenerator.SecurePasswordGenerator()
password_data = generator.generate_password(16)

print("Generated Password:", password_data["plaintext"])
print("Hashed Password:", password_data["hashed"])
print("Salt:", password_data["salt"])
print("Encrypted Password:", password_data["encrypted"])
print("Encryption Key:", password_data["encryption_key"])  # Store this safely!

checker = PasswordStrengthChecker()
strength = checker.check_strength(password_data["plaintext"])
print("Password Strength:", strength)