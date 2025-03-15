import secrets
import string

def generate_strong_password(length=12):
    if length < 12:
        raise ValueError("Password length should be at least 12 characters for strong security.")
    
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(alphabet) for _ in range(length))
    
    return password

if __name__ == "__main__":
    length = int(input("Enter the desired length for the password (at least 12): "))
    password = generate_strong_password(length)
    print(f"Generated strong password: {password}")