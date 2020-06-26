# Password_Manager_GUI
A Password Manager that holds information for local safekeeping. A random password generator was implemented to generate a robust password containing 25 characters. 
All the information is stored in a database after encrypting it using the cryptography module. After creating a user, the decrypting key is stored in a txt file which
needs to kept in a secure place. This key will be used to log into the database.

## Required Packages
- PyQt5
- cryptography

To install the packages type in terminal:
```{r, engine='bash', count_lines}
pip install -r requirements.txt
```
