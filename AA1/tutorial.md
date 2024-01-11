Create a Single Fernet Key
======================
In this activity, you will add the functionality to not create a key if a Fernet key is already created such that the file can be decrypted without an error.


<img src= "https://s3-whjr-curriculum-uploads.whjr.online/c9d562b0-e98b-4790-8a57-3cddf2224d4c.gif" width = "100%" height = "50%">




Follow the given steps to complete this activity.




1. Create the path to `encryptedKey.key` file.
* Open the file main.py.
* Create a `keyfile` variable.
```
keyFile = "encryptedKey.key"


```


2. Create a new key.
* Check if the path stored in `keyFile` does not exist.
* Indent the code to create the key inside the if block and replace `encryptedKey.key` with `keyFile`.


```
if not os.path.exists(keyFile):
  key = Fernet.generate_key()
  with open(keyFile, "wb") as encryptedKey:
    encryptedKey.write(key)
```
* Read the content of `keyFile` and store them as `key`.
```
else:
  with open(keyFile, "rb") as encryptedKey:
      key = encryptedKey.read()


```
* Save and run the code to check the output.


