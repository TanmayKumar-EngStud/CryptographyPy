from os import system

system('clear')
plainText = "HIJACKINGS"

key = "HELLO"

def BlocksCreation(plainText):
  block=[]
  while len(plainText)%8 != 0:
    plainText+=" "
  for i in range(0,len(plainText),8):
    block.append(plainText[i:i+8])
  return block

def keyRefining(key):
  if len(key)<8:
    a= "X"
    while len(key) !=8:
      key.append(a)
    return key
  else:
    return key[0:8]

def HexA(plainText): #Working well
  plainText = BlocksCreation(plainText)
  result =[]
  ans = ""
  for plain in plainText:
    ans+= hex(ord(plain[0]))[2:]
    for i in range(1,len(plain)):
      ans+=" "
      ans+= hex(ord(plain[i]))[2:]
    result.append(ans)
    ans = ""
  return result


print(HexA(plainText))