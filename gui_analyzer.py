from tkinter import *
import re
import math

def analyze():

    password = entry.get()

    score = 0
    suggestions = []

    # Length checks
    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("Use at least 8 characters")

    if len(password) >= 12:
        score += 1

    # Uppercase
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        suggestions.append("Add uppercase letters")

    # Lowercase
    if re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append("Add lowercase letters")

    # Numbers
    if re.search(r"[0-9]", password):
        score += 1
    else:
        suggestions.append("Add numbers")

    # Special characters
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        suggestions.append("Add special characters")

    # Entropy
    entropy = len(password) * math.log2(94)

    # Strength
    if score <= 2:
        strength = "Weak Password"
    elif score <= 4:
        strength = "Medium Password"
    elif score == 5:
        strength = "Strong Password"
    else:
        strength = "Very Strong Password"

    # Display results
    strength_label.config(text=f"Strength: {strength}")
    score_label.config(text=f"Score: {score}/6")
    entropy_label.config(text=f"Entropy: {entropy:.2f} bits")

    if suggestions:
        suggestion_text = "\n".join(suggestions)
    else:
        suggestion_text = "No suggestions. Excellent password!"

    suggestion_label.config(text=suggestion_text)


# GUI Window
root = Tk()
root.title("Password Strength Analyzer")
root.geometry("500x450")

Label(root, text="Enter Password", font=("Arial", 12)).pack(pady=10)

entry = Entry(root, width=35, show="*")
entry.pack()

Button(root, text="Analyze", command=analyze).pack(pady=15)

strength_label = Label(root, text="", font=("Arial", 12, "bold"))
strength_label.pack(pady=5)

score_label = Label(root, text="", font=("Arial", 11))
score_label.pack()

entropy_label = Label(root, text="", font=("Arial", 11))
entropy_label.pack()

Label(root, text="Suggestions:", font=("Arial", 11, "bold")).pack(pady=10)

suggestion_label = Label(root, text="", justify=LEFT, wraplength=450)
suggestion_label.pack()

root.mainloop()