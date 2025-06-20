import random
import string

characters = " " + string.punctuation + string.digits + string.ascii_letters
characters = list(characters)
key = characters.copy()

random.shuffle(key)

# print(f"characters: {characters}")
# print(f"key       : {key}")

# ENCRYPT
plain_text = input("Enter a message to encrypt: ")
cipher_text = ""

for letter in plain_text:
    index = characters.index(letter)
    cipher_text = cipher_text + key[index]

print(f"Original message : {plain_text}")
print(f"Encrypted message: {cipher_text}")

# DECRYPT
cipher_text = input("Enter a message to encrypt: ")
plain_text = ""

for letter in cipher_text:
    index = key.index(letter)
    plain_text = plain_text + cipher_text[index]

print(f"Encrypted message: {cipher_text}")
print(f"Original message : {plain_text}")
