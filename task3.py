import re

def check_password_strength(password):
    # Initialize strength variables
    strength_score = 0
    feedback = []

    # Check length of the password
    if len(password) >= 8:
        strength_score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Check for uppercase letters
    if re.search(r'[A-Z]', password):
        strength_score += 1
    else:
        feedback.append("Password should include at least one uppercase letter (A-Z).")

    # Check for lowercase letters
    if re.search(r'[a-z]', password):
        strength_score += 1
    else:
        feedback.append("Password should include at least one lowercase letter (a-z).")

    # Check for digits
    if re.search(r'[0-9]', password):
        strength_score += 1
    else:
        feedback.append("Password should include at least one number (0-9).")

    # Check for special characters
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        strength_score += 1
    else:
        feedback.append("Password should include at least one special character (!@#$%^&*(), etc.).")

    # Provide overall strength feedback
    if strength_score == 5:
        feedback.append("Strong password!")
    elif strength_score >= 3:
        feedback.append("Moderate password. Consider adding more variety of characters.")
    else:
        feedback.append("Weak password. Consider adding more length, mixed cases, digits, and special characters.")

    return strength_score, feedback

def main():
    print("Password Strength Checker")
    password = input("Enter a password to assess: ")

    # Get the strength score and feedback
    score, feedback = check_password_strength(password)

    # Print the results
    print(f"\nPassword strength score: {score}/5")
    print("Feedback:")
    for suggestion in feedback:
        print(f"- {suggestion}")

if __name__ == "__main__":
    main()
