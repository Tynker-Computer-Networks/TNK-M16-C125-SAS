Encrypt the files only Once
======================
In this activity, you will code to encrypt the file only if the file cannot be decrypted with the saved Fernet key.


<img src= "https://s3-whjr-curriculum-uploads.whjr.online/f50b92bd-501c-43cb-9398-fc0407a391e7.gif" width = "100%" height = "50%">




Follow the given steps to complete this activity.




1. Create `isEncrypted(filePath, key)` function.
* Open the file main.py.
* Create the `isEncrypted()` function that takes two parameters `filePath` and `key`.
* Open the file at the given `filePath` and try to decrypt a single line with the `key`.
* Return `True` if the file is decrypted, as the file was encrypted otherwise return `False` as the file was not encrypted so we can not decrypt it.
```
def isEncrypted(filePath, key):
  with open(filePath, 'rb') as file:
    firstLine = file.readline()
    try:
      Fernet(key).decrypt(firstLine)
      return True
    except Exception as e:
      return False


```


* Call `isEncrypted()` function with the `file` and `key`, store the result in `isEncrypted` variable
* Perform the encryption of file if `isEncrypted` is `False`, i.e indent the code to encrypt the file under the if block that checks.


```
if (not encrypted):
  with open(file, "rb") as file1:
      rawData = file1.read()
  encryptedRawData = Fernet(key).encrypt(rawData)
  with open(file, "wb") as file2:
      file2.write(encryptedRawData)
      file2.close()
```


* Save and run the code to check the output.
