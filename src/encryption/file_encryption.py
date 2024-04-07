# import required module
from cryptography.fernet import Fernet

# reading generated key
with open('filekey.key', 'rb') as filekey:
	key = filekey.read()

# using the generated key
fernet = Fernet(key)

# opening the original file to encrypt
with open('Fox_Solutions_Account.txt', 'rb') as file:
	original = file.read()
	
# encrypting the file
encrypted = fernet.encrypt(original)

# opening the file in write mode and 
# writing the encrypted data
with open('Fox_Solutions_Account_encrypted.txt', 'wb') as encrypted_file:
	encrypted_file.write(encrypted)
