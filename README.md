# 🔐 Password Generator & Strength Checker
A Python-based terminal application that generates secure passwords based on user preferences and evaluates their strength. It can also verify whether the generated or entered passwords are commonly used and thus insecure.

🚀 Features
  🔢 Custom Password Generation
    Generate multiple passwords at once by specifying:
    Length
    Number of passwords
    Inclusion of uppercase, lowercase, digits, and special characters

  📂 Automatic File Saving
    All generated passwords are saved to password.txt for future reference.

  🛡️ Password Strength Checker
    Check the strength of:
    A custom password
    All passwords in the password.txt file

  🧠 Dictionary Attack Protection:
    Compares against a list of common passwords (if common_password.txt exists) to flag insecure choices.

📁 Files
  main.py – The core script for password generation and strength checking
  password.txt – Stores generated passwords (created at runtime)
  common_password.txt (optional) – List of weak/common passwords for comparison

🛠️ Requirements
  Python 3.x (standard library only, no external packages)
