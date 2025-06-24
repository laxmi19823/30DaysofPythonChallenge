from pydantic import BaseModel, EmailStr, Field, root_validator
from typing import Optional

class UserProfile(BaseModel):
    name: str = Field(..., min_length=1)
    email: EmailStr
    age: int = Field(..., ge=18, le=100)

def get_valid_input(prompt: str, validation_func=None):
    while True:
        value = input(prompt + ": ").strip()
        try:
            if validation_func:
                return validation_func(value)
            return value
        except ValueError as e:
            print(f"Invalid input: {str(e)}")
            continue

def main():
    print("\nEnter your profile details:")
    
    # Get validated inputs
    name = get_valid_input("Enter your name")
    email = get_valid_input("Enter your email", lambda x: EmailStr.validate(x))
    
    # Special handling for age
    while True:
        try:
            age_str = input("Enter your age (18-100): ")
            age = int(age_str)
            if 18 <= age <= 100:
                break
            print("Age must be between 18 and 100")
        except ValueError:
            print("Please enter a valid number")

    # Create and validate the profile
    try:
        profile = UserProfile(name=name, email=email, age=age)
        print("\nProfile created successfully!")
        print(profile)
    except Exception as e:
        print(f"\nError creating profile: {str(e)}")

if __name__ == "__main__":
    main()