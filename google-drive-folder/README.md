# Add folders to google drive with ease

Aight folks, this requires a bit more of coding (not really, just configuring)

Firstly setup the API for Google Drive, this might be troublesome but life is fun when its aint easy.
Follow [this](https://developers.google.com/drive/api/v3/enable-drive-api "SUPER GUIDE") tutorial to configure the API, you should add your email address to the Test Users to allow yourself to access the API

Next, just download the **OAuth 2.0 Client IDs** credentials and save it in this folder as `credentials.json`
. That's it, you're the owner of this handy tool now, dont forget to install the requirements

Also when you run `main.py` for the first time, a new file named token.pickle will be created, don't delete it or you will have to go through the verification process again.

# Usage
Use it as if you're accessing paths in Unix (with /),
To indicate that the following is creating into the same folder aka have the same level, seperate those folders with `|`

for child within child of the same folder, use `>`

don't use `/` after using `>` please, that's enough for me

eg: `documents/child1/child2>child3>child4|child2>child3>child4`
output:
```
↳documents
        ↳child1
                        ↳child2
                                ↳child3
                                        ↳child4
                        ↳child2
                                ↳child3
                                        ↳child4
```
eg2: `documents/child1/child2/child 3/child 4`
```
↳documents
        ↳child1
                ↳child2
                        ↳child 3
                                ↳child 4
```
The feature is quite limited for a tech savy, or developer, so this might not be satisfactory, please make any contributions if you think you can improve this to be better
