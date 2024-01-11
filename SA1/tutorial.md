Generate an Encryption Key
======================
In this activity, you will code to generate a key that can be used for encryption of data.


<img src= "https://s3-whjr-curriculum-uploads.whjr.online/c9d562b0-e98b-4790-8a57-3cddf2224d4c.gif" width = "auto" height = "auto">




Follow the given steps to complete this activity.




1. Generate a Fernet Key
* Open the file `main.py`.
* Import the `Fernet` module to create a key.
```
from cryptography.fernet import Fernet
```


* Generate the key using the 'Fernet' module.
```
key = Fernet.generate_key()
```


* Save the generated key in `encryption.key` file.
```
with open("encryptedKey.key", "wb") as encryptedKey:
    encryptedKey.write(key)
```


* Save and run the code to check the output.
