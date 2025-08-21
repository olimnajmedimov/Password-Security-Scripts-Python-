import hashlib

def check_password_strength(pwd):
    if len(pwd) < 8:
        return "Weak"
    if any(c.isdigit() for c in pwd) and any(c.isupper() for c in pwd):
        return "Strong"
    return "Medium"

password = input("Enter password: ")
print(f"Password strength: {check_password_strength(password)}")

# Example hash comparison
hashed = hashlib.sha256(password.encode()).hexdigest()
print(f"SHA256 Hash: {hashed}")
