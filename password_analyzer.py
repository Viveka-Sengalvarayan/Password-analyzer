import re
import math

password = input("Enter Password: ")

common_passwords = [
    "123456",
    "password",
    "admin",
    "qwerty",
    "welcome"
]

if password.lower() in common_passwords:
    print("\nWARNING: Common password detected!")

score = 0
suggestions = []

if len(password) >= 8:
    score += 1
else:
    suggestions.append("Use at least 8 characters")

if len(password) >= 12:
    score += 1

if re.search(r"[A-Z]", password):
    score += 1
else:
    suggestions.append("Add uppercase letters")

if re.search(r"[a-z]", password):
    score += 1
else:
    suggestions.append("Add lowercase letters")

if re.search(r"[0-9]", password):
    score += 1
else:
    suggestions.append("Add numbers")

if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
    score += 1
else:
    suggestions.append("Add special characters")

entropy = len(password) * math.log2(94)

print("\nScore:", score)
print("Entropy:", round(entropy, 2), "bits")

if score <= 2:
    print("Weak Password")
elif score <= 4:
    print("Medium Password")
elif score == 5:
    print("Strong Password")
else:
    print("Very Strong Password")

if suggestions:
    print("\nSuggestions:")
    for item in suggestions:
        print("-", item)