# substitution_cipher

This Python script implements a simple substitution cipher for encrypting and decrypting messages. It randomly generates a key for substitution and uses it to encrypt and decrypt text entered by the user.

*Features

  - Random key generation on each run.
  - Custom character set including:
  - Uppercase and lowercase letters
  - Digits
  - Punctuation
  - Space
  - One-way encryption and decryption using a simple mapping logic.

*How It Works

1. The script creates a list of all possible characters.
2. It then shuffles this list to create a random substitution key.
3. For encryption, each character in the message is replaced with the character at the same index in the shuffled key.
4. For decryption, it reverses the process using the key.

Note: The key used for encryption and decryption must be the same. In this script, the encryption and decryption occur in a single run, so the key remains consistent. However, if you run the script again, a new key is generated, and decryption will not work for previously encrypted messages.

Usage

Run the script with Python.

