class PasswordChecker:
    def __init__(self):
        self.common_passwords = ["password", "123456", "123456789", "qwerty", "12345678", "111111", "1234567890", "1234567", "password1", "12345", "1234", "password123", "qwertyuiop", "1q2w3e4r", "admin", "qwerty123", "123123", "11111111", "welcome", "login"]
        self.password_history = {}

    def check_strength(self, password):
        strength = "very weak"
        if password.lower() in self.common_passwords:
            return strength
        if len(password) < 6:
            return strength

        has_uppercase = any(char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" for char in password)
        has_lowercase = any(char in "abcdefghijklmnopqrstuvwxyz" for char in password)
        has_digit = any(char in "0123456789" for char in password)
        has_special_char = any(char in "!@#$%^&*()-_=+[{]}|;:',<.>/?`~" for char in password)

        if len(password) >= 8 and has_uppercase and has_lowercase and has_digit and has_special_char:
            strength = "very strong"
        elif len(password) >= 8 and (has_uppercase or has_lowercase) and has_digit and has_special_char:
            strength = "strong"
        elif len(password) >= 8 and (has_uppercase or has_lowercase) and has_digit:
            strength = "moderate"
        elif len(password) >= 6:
            strength = "weak"

        return strength

    def update_history(self, password, strength):
        self.password_history[password] = strength


checker = PasswordChecker()

while True:
    user_input = input("Enter a password (or 'quit' to exit): ")
    if user_input.lower() == "quit":
        break

    strength = checker.check_strength(user_input)
    print("Password strength:", strength)

    checker.update_history(user_input, strength)

print("Password history:")
for password, strength in checker.password_history.items():
    print(f"Password: {password}, Strength: {strength}")
