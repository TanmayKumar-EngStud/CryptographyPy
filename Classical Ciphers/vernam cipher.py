from os import system
system('clear')

plainText = "Hi I am Tanmay Kumar Singh Call me TKS"
key = "TGHYPTXYUO"


print(f"Plain Text is : {plainText}")
print(f"Key is        : {key}")

def modify(text):
  text = text.lower()
  text = text.replace(" ", "")
  result = []
  for i in text:
    result.append(ord(i) - ord('a'))
  return result

def Encryption(plainText, key):
  pText = modify(plainText)
  Key = modify(key)
  cMatrix = []
  for i in range (len(pText)):
    cMatrix.append((pText[i]+Key[i%len(Key)])%26)
  cText = ""
  for i in cMatrix:
    cText += chr(i+ord('A'))
  return cText

cipherText = Encryption(plainText,key)
print(f"The cipher text generated is :{cipherText}")

def addInv(num):
  for i in range(26):
    if (i+num)%26 == 0:
      return i

def Decryption(cipherText, key):
  cText = modify(cipherText)
  Key = modify(key)
  pMatrix = []

  for i in range( len(cText)):
    pMatrix.append((cText[i]+ addInv(Key[i%len(Key)]))%26)
  pText =""
  for i in pMatrix:
    pText += chr(i+ord('A'))
  return pText


GenPlainText = Decryption(cipherText,key)
print(f"The generated plain text is :{GenPlainText}")