# password_checker.py

import re
import tkinter as tk
from tkinter import messagebox

# === Password Strength Checker ===
def check_password_strength(password):
    score = 0
    # Length >= 8
    if len(password) >= 8:
        score += 1
    # Uppercase
    if re.search(r"[A-Z]", password):
        score += 1
    # Lowercase
    if re.search(r"[a-z]", password):
        score += 1
    # Digit
    if re.search(r"\d", password):
        score += 1
    # Special character
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1

    if score <= 2:
        return "Weak"
    elif score == 3 or score == 4:
        return "Moderate"
    else:
        return "Strong"

# === GUI App ===
def check_password():
    password = entry.get()
    if not password:
        messagebox.showwarning("Warning", "Please enter a password!")
        return
    strength = check_password_strength(password)
    result_label.config(text=f"Password Strength: {strength}")

# === GUI Setup ===
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x200")

tk.Label(root, text="Enter a Password:", font=("Arial", 12)).pack(pady=10)
entry = tk.Entry(root, show="*", width=30)
entry.pack()

tk.Button(root, text="Check Strength", command=check_password).pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12, "bold"))
result_label.pack()

root.mainloop()
