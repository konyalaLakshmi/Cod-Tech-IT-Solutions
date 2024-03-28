import string
import random

def generate_password(length, num_lower, num_upper, num_digits, num_symbols):
    """
    Generate a password with specified length and character types.

    Args:
    - length (int): Length of the password.
    - num_lower (int): Number of lowercase letters to include.
    - num_upper (int): Number of uppercase letters to include.
    - num_digits (int): Number of digits to include.
    - num_symbols (int): Number of symbols to include.

    Returns:
    - str: Generated password.
    """
    if length < (num_lower + num_upper + num_digits + num_symbols):
        raise ValueError("Length is too short for the specified character types.")

    all_chars = (
        string.ascii_lowercase * num_lower
        + string.ascii_uppercase * num_upper
        + string.digits * num_digits
        + string.punctuation * num_symbols
    )
    if len(all_chars) < length:
        raise ValueError("Not enough characters to meet the length requirement.")

    password = ''.join(random.sample(all_chars, length))
    return password

def main():
    print("*** Password Generator ***")
    try:
        length = int(input("Enter password length: "))
        num_lower = int(input("Enter number of lowercase letters: "))
        num_upper = int(input("Enter number of uppercase letters: "))
        num_digits = int(input("Enter number of digits: "))
        num_symbols = int(input("Enter number of symbols: "))

        password = generate_password(length, num_lower, num_upper, num_digits, num_symbols)
        print("Generated Password:", password)
    except ValueError as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
