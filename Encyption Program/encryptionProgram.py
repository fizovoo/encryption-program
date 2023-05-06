import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()

random.shuffle(key)

# print(f"chars: {chars}")
# print(f"key : {key}")

#ENCRYPT

plain_text = input("Enter message to encrypt: ")
cipher_text = ""

# for every letter in the plain text get the index of each letter character and then refer to the key of the letter and then add the new character to the encrypted message
for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index] 

print(f"original message: {plain_text}")
print(f"encrypted message: {cipher_text}")

#DECRYPT
cipher_text = input("Enter message to decrypt: ")
plain_text = ""

# for every letter in the ciphered text get the index of each letter in the key and then refer to the character of the letter and then add the new key to the encrypted message
for letter in cipher_text:
    index = key.index(letter)
    plain_text += chars[index] 

print(f"encrypted message: {cipher_text}")
print(f"original message: {plain_text}")