import re

def check_password_strength(password):
    strength = 0
    feedback = []

    # Length check
    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("🔴 Password should be at least 8 characters long.")

    # Uppercase check
    if re.search(r'[A-Z]', password):
        strength += 1
    else:
        feedback.append("🔴 Add at least one uppercase letter.")

    # Lowercase check
    if re.search(r'[a-z]', password):
        strength += 1
    else:
        feedback.append("🔴 Add at least one lowercase letter.")

    # Number check
    if re.search(r'[0-9]', password):
        strength += 1
    else:
        feedback.append("🔴 Add at least one number.")

    # Special character check
    if re.search(r'[^A-Za-z0-9]', password):
        strength += 1
    else:
        feedback.append("🔴 Add at least one special character (e.g. !, @, #, $).")

    # Strength rating
    if strength == 5:
        rating = "🟢 Strong Password"
    elif strength >= 3:
        rating = "🟡 Moderate Password"
    else:
        rating = "🔴 Weak Password"

    return rating, feedback

def main():
    print("🔐 Password Strength Checker")
    password = input("Enter your password: ")

    rating, feedback = check_password_strength(password)

    print(f"\nPassword Strength: {rating}")
    if feedback:
        print("Suggestions to improve:")
        for tip in feedback:
            print(tip)

if __name__ == "__main__":
    main()
