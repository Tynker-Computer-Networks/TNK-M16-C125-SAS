# Import the Fernet from cryptography
from cryptography.fernet import Fernet

# Genrate the secrete key
key = Fernet.generate_key()

# Store / write the key value inside the encryptedKey.key file
with open("encryptedKey.key", "wb") as encryptedKey:
    encryptedKey.write(key)
