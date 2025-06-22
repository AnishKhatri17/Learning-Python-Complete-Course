import random
import string

# chars = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy() # .copy() copies the exact same characters as holded by 'chars'

random.shuffle(key) # This will shuffle the key with each time the program runs.

print(f"chars: {chars}")
print(f"keys: {key}")


# EXCRYPT CODE
plain_text = input("Enter a message to Encrypt: ")
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]
    
print()
print(f"Orginal Message: {plain_text}")
print(f"Encrypted Message: {cipher_text}")


print("\n")
# DECRYPT CODE
cipher_text = input("Enter the Encrypted Message: ")
plain_text = ""

for letter in cipher_text:
    index = key.index(letter)
    plain_text += chars[index]

print()    
print(f"Encrypted Message: {cipher_text}")
print(f"Orginal Message: {plain_text}")
