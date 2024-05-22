import secrets
import string

def generate_extremely_strong_password(length=24):
    if length < 12:
        raise ValueError("Password length must be at least 12 to include multiple repetitions of all character types.")

    # Define character pools
    uppercase_pool = string.ascii_uppercase
    lowercase_pool = string.ascii_lowercase
    digits_pool = string.digits
    special_pool = string.punctuation

    # Ensure the password contains at least three of each character type
    password = [
        secrets.choice(uppercase_pool),
        secrets.choice(uppercase_pool),
        secrets.choice(uppercase_pool),
        secrets.choice(lowercase_pool),
        secrets.choice(lowercase_pool),
        secrets.choice(lowercase_pool),
        secrets.choice(digits_pool),
        secrets.choice(digits_pool),
        secrets.choice(digits_pool),
        secrets.choice(special_pool),
        secrets.choice(special_pool),
        secrets.choice(special_pool)
    ]

    # Fill the rest of the password length with a random selection from all pools
    all_characters_pool = uppercase_pool + lowercase_pool + digits_pool + special_pool
    password += [secrets.choice(all_characters_pool) for _ in range(length - 12)]

    # Shuffle the list to avoid predictable patterns
    secrets.SystemRandom().shuffle(password)

    # Join the list into a string to form the final password
    return ''.join(password)

# Prompt user for password length
try:
    length = int(input("Enter the desired length for the password (at least 24 for better security): "))
    if length < 24:
        print("For better security, a length of at least 24 characters is recommended.")
        length = max(24, length)
except ValueError as ve:
    print(f"Invalid input: {ve}. Using default length of 24.")
    length = 24  # Default length

# Generate and print the extremely strong password
password = generate_extremely_strong_password(length=length)
print("Generated Extremely Strong Password:", password)
