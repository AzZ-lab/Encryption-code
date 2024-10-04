import random
import string

#allows you to get a string of characters.
chara= " " + string.punctuation + string.digits + string.ascii_letters
chara=list(chara) #puts the string of characters into a list
key = chara.copy()

random.shuffle(key)#this shuffles the list of keys

print(f"chara: {chara}")
print(f"key  : {key}")

#encrypt

plain_text = input("enter text to be encrypted: ")
cipher_text = ""

for letter in plain_text:
    index= chara.index(letter)
    cipher_text += key[index]

print(f"original message : {plain_text}")
print(f"encrypted message: {cipher_text}")


