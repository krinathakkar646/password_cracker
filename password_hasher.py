import hashlib
import getpass

def hash_password(hash_type):
    try:
        # Hide user input while typing the password
        password = getpass.getpass("Enter a password to hash: ")

        # Hash the password
        hashed = hashlib.new(hash_type, password.encode()).hexdigest()

        # Store both the original password and hash in a file
        with open("hashed_password.txt", "w") as file:
            file.write(f"{hashed},{password}")

        print("\n✅ The password is hashed and stored securely.")
        print(f"🔐 Hashed ({hash_type}): {hashed}")

        return hashed

    except ValueError:
        print("❌ Invalid hash type! Use md5, sha1, sha256, etc.")
        return None
