import os
os.system('clear')

# plainText = input("Enter the plain text: ")
# key1 = int(input("Enter the multiplicative key: "))
# key2 = int(input("Enter the additive key: "))

cipher ="ZEBBW"
aKey = 2
mKey = 7

cipher = cipher
#Same General Setup
def char(text):
  return ord(text)-ord('A')

def num(number):
  return chr(number+ord('A'))

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
# def encrypt(plainText, Mkey, Akey):
#   cipherText = ""
#   for i in plainText:
#     cipherText += num(((char(i)*Mkey)+Akey)%26)
#   return cipherText
# cipher = encrypt(plainText, key1, key2)
# print(cipher)


#Decryption according to affine cipher
def decrypt(cipherText, Mkey, Akey):
  plainText = ""
  new_Mkey = MInverseKey(Mkey)
  new_Akey = AInverseKey(Akey)
  print(new_Mkey)
  print(new_Akey)
  for i in cipherText:
    plainText += num(((char(i)*new_Mkey)+new_Akey)%26)
  return plainText
plain = decrypt(cipher, mKey, aKey)
print("\n\n")
print(plain)

def EuclideanAlgorithm(a, b):
  if b == 0:
    return a
  else:
    return EuclideanAlgorithm(b, a % b)
    
# There is an Error in this program I will fix it later.
