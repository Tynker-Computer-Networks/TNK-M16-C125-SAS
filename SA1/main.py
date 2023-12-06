# Import the Fernet from cryptography.fernet
from cryptography.fernet import Fernet

# Call generate_key() method from Fernet and save the returned value in key variable
key = Fernet.generate_key()

# Store / write the key value inside the encryptedKey.key file
with open("encryptedKey.key", "wb") as encryptedKey:
    encryptedKey.write(key)
