import os
os.system('clear')

# Text = input("\n\nEnter the text: ")
# key = int(input("Enter the key: "))

Text = "VIT"
key =7

Text = Text.lower()
# I used ord function to convert the letter to its ASCII value.
ascii = ord('a')

#Function for converting plain text to cipher text
def caesar(Text, key):
    cipherText = ""
    for i in range(len(Text)):
          cipherText += chr((ord(Text[i]) - ascii + key) % 26 + ascii)

    return cipherText #working well

cipherText =caesar(Text, key)
#output for cipher text
print(caesar(Text, key))

#Function for converting into cipher text to plain text
def painText(Text, key):
    PlainText = ""
    for i in range(len(Text)):
      PlainText += chr((ord(Text[i])-ascii  + Zn(key)) % 26 + ascii)
    print("Inverse of the key is :",Zn(key))
    return PlainText

def Zn(i):
  for inverse in range(26):
    if(inverse + i)%26 == 0:
      return inverse


print("\n")
#text for plain text
print(painText(cipherText, key))
