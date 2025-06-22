import random
import string

def generate_password(length, use_upper, use_lower, use_digits, use_special):
    characters = ""
    if use_upper:
        characters += string.ascii_uppercase
    if use_lower:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    if not characters:
        return "❌ Error: No character types selected."

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("🔐 Password Generator")

    try:
        length = int(input("Enter desired password length: "))
        if length <= 0:
            print("❌ Length must be a positive number.")
            return
    except ValueError:
        print("❌ Invalid input. Please enter a number.")
        return

    print("\nInclude the following character types:")
    use_upper = input("Include UPPERCASE letters? (y/n): ").lower() == 'y'
    use_lower = input("Include lowercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Include digits? (y/n): ").lower() == 'y'
    use_special = input("Include special characters? (y/n): ").lower() == 'y'

    password = generate_password(length, use_upper, use_lower, use_digits, use_special)
    print(f"\n✅ Generated Password: {password}")

if __name__ == "__main__":
    main()
