import random

def makeDictionary(alphabet):
   alphabet = list(alphabet)
   random.shuffle(alphabet)
   return ''.join(alphabet)

def encrypt(message, dictionary, alphabet):
    keyIndices = [alphabet.index(k.lower()) for k in plaintext]
    return ''.join(dictionary[keyIndex] for keyIndex in keyIndices)

def decrypt(cipher, dictionary, alphabet):
    keyIndices = [dictionary.index(k) for k in cipher]
    return ''.join(alphabet[keyIndex] for keyIndex in keyIndices)


alphabet = 'abcdefghijklmnopqrstuvwxyz.,! '

d = makeDictionary(alphabet)
msg = "This is a string that needs to be encrypted"


newText = encrypt(plaintext, d, alphabet)

print(msg)
print(newText)
print(decrypt(newText, d, alphabet))