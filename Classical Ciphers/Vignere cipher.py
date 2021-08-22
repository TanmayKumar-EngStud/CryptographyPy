from os import system
system('clear')


plainText = "Give money"
key  = "Lock"

print(f"Plain Text is : {plainText}")
print(f"Key is        : {key}")

def numMatrix(plainText):
  result = []
  plainText = plainText.lower()
  plainText = plainText.replace(" ", "")

  for i in plainText:
    result.append(ord(i) - ord('a'))
  return result

def encryption(plainText, key):
  Text = numMatrix(plainText)
  K = numMatrix(key)
  kSize = len(key)
  cipher = []
  for i in range(len(Text)):
    cipher.append((Text[i]+K[i%kSize])%26)
  cipherText =""
  for i in range(len(cipher)):
    cipherText += chr(cipher[i]+ord('A'))
  return cipherText


cipherText = encryption(plainText, key)
print(f"Cipher Text recieved is: {cipherText}")

def addInv(k):
  for i in range(26):
    if (i+k)%26 == 0:
      return i

def Decryption(cipherText, key):
  Text  = numMatrix(cipherText)
  K = numMatrix(key)
  kSize = len(key)
  plain = []
  for i in range(len(Text)):
    plain.append((Text[i]+addInv(K[i%kSize]))%26)
  GenplainText = ""
  for i in plain:
    GenplainText += chr(i + ord('A'))
  return GenplainText

GenPlainText = Decryption(cipherText, key)
print(f"Generated Cipher Text is : {GenPlainText}")