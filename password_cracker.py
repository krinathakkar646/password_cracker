import os
import hashlib

def crack_password(hash_value, hash_type, wordlist_path):
    try:
        with open(wordlist_path, "r", encoding="latin-1") as wordlist:
            for word in wordlist:
                word = word.strip()
                hashed_word = hashlib.new(hash_type, word.encode()).hexdigest()

                if hashed_word == hash_value:
                    print("\n✅ Password Found in Wordlist!")
                    print(f"🔓 Original Password: {word}")
                    return word

        print("\n❌ Password Not Found in Wordlist")
        return None

    except FileNotFoundError:
        print("\n❌ Wordlist file not found! Please check the path:", wordlist_path)
        return None

if __name__ == "__main__":
    hash_type = input("Enter hash type (md5, sha256, sha1, etc.): ")

    from password_hasher import hash_password
    hash_value = hash_password(hash_type)

    if hash_value:
        # Ensure the wordlist is found in the same directory
        script_dir = os.path.dirname(os.path.abspath(__file__))
        wordlist_path = os.path.join(script_dir, "rockyou.txt")

        crack_password(hash_value, hash_type, wordlist_path)
