import random  # Import the random module for generating random elements.
import string  # Import the string module for working with strings.

def generate_password(min_length, numbers=True, special_characters=True):
    # Define character sets.
    letters = string.ascii_letters  # Uppercase and lowercase letters.
    digits = string.digits  # Numbers 0-9.
    special = string.punctuation  # Special characters like !@#$%^&*()_+.

    characters = letters  # Initialize characters with letters.
    if numbers:
        characters += digits  # If numbers are desired, add them to characters.
    if special_characters:
        characters += special  # If special characters are desired, add them to characters.

    pwd = ""  # Initialize an empty string for the password.
    meets_criteria = False  # Initialize a flag to check if the criteria are met.
    has_number = False  # Initialize a flag to check if the password has at least one number.
    has_special = False  # Initialize a flag to check if the password has at least one special character.

    # Generate the password until it meets the criteria.
    while not meets_criteria or len(pwd) < min_length:
        new_char = random.choice(characters)  # Choose a random character from the characters set.
        pwd += new_char  # Append the chosen character to the password.

        if new_char in digits:
            has_number = True  # Check if the new character is a digit.
        elif new_char in special:
            has_special = True  # Check if the new character is a special character.

        meets_criteria = True  # Assume the password meets the criteria.
        if numbers:
            meets_criteria = has_number  # If numbers are required, the password must have at least one.
        if special_characters:
            meets_criteria = meets_criteria and has_special  # If special characters are required, the password must have at least one.

    return pwd  # Return the generated password.

# Get user input for password requirements.
min_length = int(input("Enter the minimum length: "))  # Minimum password length.
has_number = input("Do you want to have numbers (y/n)? ").lower() == "y"  # Whether to include numbers.
has_special = input("Do you want to have special characters (y/n)? ").lower() == "y"  # Whether to include special characters.

# Generate the password based on user input.
pwd = generate_password(min_length, has_number, has_special)

# Print the generated password.
print("The generated password is: ", pwd)
