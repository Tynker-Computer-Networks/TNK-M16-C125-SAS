Decrypt the File Data
======================
In this activity, you will code to decrypt the files when the correct key is entered by the user.


<img src= "https://s3-whjr-curriculum-uploads.whjr.online/4cbf2a3a-90b2-41c3-8878-bb443971972d.gif" width = "auto" height = "auto">




Follow the given steps to complete this activity.




1. Decrypt the file data
* Open the file decrypt.py.
* Set a `seacretPhrase` as string "hello".
* Ask user to enter a password and save it in as `enteredPhrase`
```
secretPhrase = "hello"


enteredPhrase = input("Enter valid phrase to decrypt the files\n")


```


* Notify the user on the wrong password if the secret password doesn't match with the tried passwords.
```
if (secretPhrase != enteredPhrase):
    print(" 👹👹👹👹 Invalid Phrase try one more time or Pay me more 👹👹👹👹 ")


```
* Open the `encryptedKey.key` file and store its content in `secretKey`
```
else:
    try:
        with open("encryptedKey.key", "rb") as encryptedKey:
            secretKey = encryptedKey.read()


```
* Loop through each file in the `files` and perform following:
  * Open the file and read the raw data.
  * Decrypt the raw data.
  * Store the decrypted data back in the file.
```
        for file in files:
            with open(file, "rb") as theFile:
                    rawData = theFile.read()
           
            decryptedRawData = Fernet(secretKey).decrypt(rawData)


            with open(file, "wb") as theFile:
                    theFile.write(decryptedRawData)
```


* Notify the user about the recovery of their information.
```
        print("You have successfully recovered all the files!!")
    # Except pass
    except:
        pass
```
* Save and run the code to check the output.
