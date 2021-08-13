import os
os.system('clear')
#just to clear the terminal while running

# plainText = input("Enter the plain text: ")
# key = int(input("Enter the key: "))

plainText = "Test"
key = 3

# This is to convert alphabets to their associated numbers


def char(text):
  return ord(text)-97

def num(number):
  return chr(number+97)

def keyInverse(key):
  for i in range(26):
    if key*i%26 == 1:
      return i


# Now we will make the multiplicative cipher
plainText = plainText.lower() #Taking lower for simplicity

def encrypt(plainText, key):
  cipherText = ""
  for i in plainText:
    cipherText += num(char(i)*key%26)
  return cipherText

#Now we will print the cipher text

cipher = encrypt(plainText, key)
print("The cipher text is: ", cipher)

#Now we will decrypt the cipher text
def decrypt(cipherText, key):
  new_key = keyInverse(key)
  plainText = ""
  for i in cipherText:
    plainText += num(char(i)*new_key%26)

  print(new_key)
  return plainText

# Defining Function for Extended Euclidean algorithm to find the inverse key
def egcd(a, b):
  if a == 0:
    return (b, 0, 1)
  else:
    g, y, x = egcd(b % a, a)
    return (g, x - (b // a) * y, y)


plain = decrypt(cipher, key)
#Now we will print the plain text
print("The plain text is: ", plain)