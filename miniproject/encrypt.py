import random
import string

chars=string.digits+string.ascii_letters+string.punctuation+" "
chars=list(chars)
keys=chars.copy()

random.shuffle(keys)

#print(f"chars:{chars}")
#print(f"keys:{keys}")

original_text=input("enter text to be encrypted:")
encrypted_text=""

for char in original_text:
    index=keys.index(char)
    encrypted_text+=chars[index]
print(f"encrypted text={encrypted_text}")

print("***************************************")
en_text=input("entre encrypted_text fro decryption:")
de_text=""

for char in en_text:
    index=chars.index(char)
    de_text+=keys[index]
print(f"decryped_text:{de_text}")

