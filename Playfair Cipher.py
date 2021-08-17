from os import system
system('clear')



def makeKey(keyValue):
  keyValue = keyValue.replace(" ", "").lower()
  newPlainText = ""+keyValue[0]
  for i in range(len(keyValue)):
    if keyValue[i] not in newPlainText:
      newPlainText += keyValue[i]

  keyValue = newPlainText

  alpha = "ABCDEFGHJKLMNOPQRSTUVWXYZ".lower() 
  # Here you can see that i have removed "I".
  # I am taking J
  key = []
  for i in range(5):
    temp = []
    for j in range(5):
      if i*5+j < len(keyValue):
        temp.append(keyValue[i*5+j])
        alpha = alpha.replace(keyValue[i*5+j], "")
        #This will automatically remove the letter from the alphabet
      else :
        temp.append(alpha[0])
        alpha = alpha.replace(alpha[0],"")
    key.append(temp)

  return key


#Checking the matrix key
def show(key):
  for i in range(5):
    print("\t", end="")
    for j in range(5):
      print(key[i][j], end=" ")
    print()

def makePair(plainText):
  textList = []
  i=0
  while i <len(plainText):
    if i == len(plainText)-1:
      textList.append(plainText[i]+"x")
      break
    if plainText[i] == plainText[i+1]:
      textList.append(plainText[i]+"x")
      i+=1
    else:
      textList.append(plainText[i]+plainText[i+1])
      i+=2
    
  return textList

def findChar(char, Matrix):
  for i in range(5):
    for j in range(5):
      if Matrix[i][j] == char:
        return list([i,j])

def giveValue(char, Matrix):
  x1,y1 = findChar(char[0], Matrix)
  x2,y2 = findChar(char[1], Matrix)
  newChar = ""
  if x1 == x2:#Column is same
    newChar += Matrix[(x1+1)%5][y1]+Matrix[(x2+1)%5][y2]
  elif y1 == y2:#Row is same
    newChar += Matrix[x1][(y1+1)%5]+Matrix[x2][(y2+1)%5]
  else :
    newChar += Matrix[x1][y2]+Matrix[x2][y1]
    #Intersection of Row(char1) and Column(char2)
    #newChar = "Intersection(Row(char1),Column(char2))+Intersection(Column(char1),Row(char2))"
  return newChar


def encryption(plainText, key):
  #removing Duplicates
  keyMatrix = makeKey(key)
  show(keyMatrix)
  plainText = plainText.replace(" ", "").lower()
  print(plainText)
  #making pair of plainText
  textList = makePair(plainText)

  cipherText = ""
  for i in textList:
    print(i)
    cipherText += giveValue(i, keyMatrix)

  return cipherText

def Decryption(cipherText, key):
  keyMatrix = makeKey(key)
  plainText = ""
  textList = makePair(cipherText)
  for i in textList:
    plainText += giveValue(i, keyMatrix)
  return plainText



plainText = input("Enter the plain text: ")
key = input("Enter the key: ")

# plainText = "Vellore"
# key = "Monarchy"
cipherText =encryption(plainText, key)
print("\nCipher Text: ", cipherText)
print("\n\n")
generatedPlainText = Decryption(cipherText, key)
print("\nDecrypted Plain Text: ", generatedPlainText)

# Since we considered x as a special character, we have to replace it with space
generatedPlainText = generatedPlainText.replace("x", "")

print(f"\n\nDecrypted text with no special characters : {generatedPlainText}")