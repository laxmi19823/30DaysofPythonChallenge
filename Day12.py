import re

def validate_gmail(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@gmail\.com$'
    return bool(re.match(pattern, email))

email = input("Enter your Gmail address: ")

if validate_gmail(email):
    print("Valid Gmail address!✅")
else:
    print("Invalid Gmail address❌. Please enter a valid Gmail ID.")
