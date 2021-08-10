import os
os.system('clear')

# plainText = input("Enter the plain text: ")
# key1 = int(input("Enter the multiplicative key: "))
# key2 = int(input("Enter the additive key: "))

plainText ="Testing"
key1 = 7
key2 = 5

plainText = plainText.lower()
#Same General Setup
def char(text):
  return ord(text)-97

def num(number):
  return chr(number+97)

# This is multiplicative inverse of key
def MInverseKey(key):
  for i in range(26):
    if key*i%26 == 1:
      return i

#This is additive inverse of key
def AInverseKey(key):
  for i in range(26):
    if (key+i)%26 == 1:
      return i

#Encryption according to affine cipher
def encrypt(plainText, Mkey, Akey):
  cipherText = ""
  for i in plainText:
    cipherText += num(((char(i)*Mkey)+Akey)%26)
  return cipherText
cipher = encrypt(plainText, key1, key2)
print(cipher)


#Decryption according to affine cipher
def decrypt(cipherText, Mkey, Akey):
  plainText = ""
  new_Mkey = MInverseKey(key1)
  new_Akey = AInverseKey(key2)
  print(new_Mkey)
  print(new_Akey)
  for i in cipherText:
    plainText += num(((char(i)+new_Akey)*new_Mkey)%26)
  return plainText
plain = decrypt(cipher, key1, key2)
print("\n\n",plain)
