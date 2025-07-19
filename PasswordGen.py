import random

# Get user input
length = int(input("Enter the length of the password: "))
amount = int(input("Enter the number of passwords to generate: "))
upper = int(input("Include uppercase letters? (1 for yes, 0 for no): "))
lower = int(input("Include lowercase letters? (1 for yes, 0 for no): "))
num = int(input("Include numbers? (1 for yes, 0 for no): "))
special = int(input("Include special characters? (1 for yes, 0 for no): "))

def generate_passwords(length, amount, upper, lower, num, special):
    # Define character sets
    uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowercase_letters = uppercase_letters.lower()
    numbers = "0123456789"
    special_characters = "!@#$%^&*}()-+[]|;:,.<}>?/~\\{"

    all_chars = ""
    passwords = []

    # Build character pool
    if upper:
        all_chars += uppercase_letters
    if lower:
        all_chars += lowercase_letters
    if num:
        all_chars += numbers
    if special:
        all_chars += special_characters

    if not all_chars:
        print("Error: No character types selected. Cannot generate passwords.")
        return

    # Generate passwords
    for _ in range(amount):
        password = "".join(random.choices(all_chars, k=length))
        print(password)
        passwords.append(password)

    # Write to file
    with open("password.txt", "w") as file:
        for pwd in passwords:
            file.write(pwd + "\n")

    print(f"{amount} passwords saved to password.txt")

def password_Strength():
    choice = input("Do you want to check the strength of a specific password? (yes/no): ")

    if choice.lower() == "yes":
        password = input("Enter the password to check its strength: ")
        strength = 0

        # Character type checks
        if any(c.isupper() for c in password):
            strength += 1
        if any(c.islower() for c in password):
            strength += 1
        if any(c.isdigit() for c in password):
            strength += 1
        if any(c in "!@#$%^&*}()-+[]|;:,.<}>?/~\\{" for c in password):
            strength += 1
        if len(password.strip()) >= 8:
            strength += 1

        # Check if password is common
        try:
            with open('common_password.txt', 'r', encoding='utf-8') as fp:
                if password.strip() in fp.read().split():
                    strength = 0
                    print("The password is too common")

        except FileNotFoundError:
            print("Note: 'common_password.txt' not found. Skipping dictionary check.")

        print("The strength of your password is:", strength)
        if strength == 5:
            print(f"{password.strip()} is a very strong & secure password.")
        elif 3 < strength < 5:
            print(f"{password.strip()} is a moderate password.")
        else:
            print(f"{password.strip()} is a weak & insecure password.")
    
    else:
        # Check strength for passwords in password.txt
        try:
            with open("password.txt", "r") as file:
                passwords = file.readlines()
        except FileNotFoundError:
            print("Error: 'password.txt' not found.")
            return

        for password in passwords:
            strength = 0
            if any(c.isupper() for c in password):
                strength += 1
            if any(c.islower() for c in password):
                strength += 1
            if any(c.isdigit() for c in password):
                strength += 1
            if any(c in "!@#$%^&*}()-+[]|;:,.<}>?/~\\{" for c in password):
                strength += 1
            if len(password.strip()) >= 8:
                strength += 1

            print("The strength of your password is:", strength)
            if strength == 5:
                print(f"{password.strip()} is a very strong & secure password.")
            elif 3 < strength < 5:
                print(f"{password.strip()} is a moderate password.")
            else:
                print(f"{password.strip()} is a weak & insecure password.")

# Run the program
generate_passwords(length, amount, upper, lower, num, special)
password_Strength()