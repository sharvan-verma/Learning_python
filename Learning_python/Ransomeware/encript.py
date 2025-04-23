import os
from cryptography.fernet import Fernet

def encrypt_files(directory="."):
    """Encrypts all files in the given directory (excluding this script and key file)."""
    files_to_encrypt = []
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        if os.path.isfile(filepath) and filename != "encrypt.py" and filename != "seckey.key" and filename != "decrypt.py":
            files_to_encrypt.append(filepath)
    
    print("Files to encrypt:", files_to_encrypt)

    key = Fernet.generate_key()
    with open("seckey.key", "wb") as key_file:
        key_file.write(key)

    for filepath in files_to_encrypt:
        try:
            with open(filepath, "rb") as file:
                content = file.read()
            fernet = Fernet(key)
            encrypted_content = fernet.encrypt(content)
            with open(filepath, "wb") as file:
                file.write(encrypted_content)
            print(f"Encrypted {filepath}")
        except Exception as e:
            print(f"Error encrypting {filepath}: {e}")
    print("Encryption complete.")

encrypt_files()
