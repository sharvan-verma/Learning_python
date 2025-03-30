import random
import string
import time
# Define the character set 🌟
chars = " " + string.punctuation + string.digits + string.ascii_letters
char = list(chars)
key = char.copy()

random.shuffle(key)  # Shuffle the key list to create a random mapping 🔑

# ENCRYPT 🔒
print("\n✨ --- ENCRYPTION --- ✨")
plain_txt = input("➡️  Enter a message to encrypt: ")
chiper_text = ""  # store the encrypted message 📝

for letter in plain_txt:
    index = char.index(letter)  # Find the index of the letter in the original character set 🔍
    chiper_text += key[index]  # Append the corresponding character from the shuffled key to the encrypted message 🔐

print("\nEncrypting... 💫")
time.sleep(1)
print(f"📜 Original message: {plain_txt}")

print(f"🔒 Encrypted message: {chiper_text}")

# DECRYPT 🔓
print("\n🔑 --- DECRYPTION --- 🔑")
chiper_text = input("⬅️ Enter a message to decrypt: ")
plain_txt = ""  # store the decrypted message 📝

for letter in chiper_text:
    index = key.index(letter)  # Find the index of the letter in the shuffled key 🔍
    plain_txt += char[index]  # Append the corresponding character from the original character set to the decrypted message 🔓


print("\nDecrypting... 💫")
time.sleep(1)
print(f"🔓 Decrypted message: {plain_txt}")
print(f"🔐 Encrypted message: {chiper_text}")
print("\n🎉 Done! 🎉")