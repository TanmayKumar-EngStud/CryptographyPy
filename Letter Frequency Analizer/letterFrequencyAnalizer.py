from os import system
system("clear")

# frequencyList ='etaoinsrhdlucmfywgpbvkxqjz'

def syn(text):
  dictionary = {'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0,'j':0,'k':0,'l':0,'m':0,'n':0,'o':0,'p':0,'q':0,'r':0,'s':0,'t':0,'u':0,'v':0,'w':0,'x':0,'y':0,'z':0}
  for i in text:
    if i in dictionary:
      dictionary[i] += 1
    else:
      dictionary[i] = 1
  return dictionary

def find(sDict, j):
  x = 0
  for i in sDict:
    if i[0] == j:
      x =i[1]
      break
  return x

def addInv(num):
  for i in range(26):
    if (num+i)%26 == 0:
      return i

def analyse(text):
  newText = ''
  text =  text.lower()
  frequencyList = 'etaoinsrhdlucmfywgpbvkxqjz'
  dictionary = syn(text)
  sDict = list(sorted(dictionary.items(), key=lambda x: x[1], reverse=True))
  maxFreq = sDict[0][1]
  key = (ord(sDict[0][0])- ord('A')) - (ord(frequencyList[0]) - ord('a'))
  newKey = addInv(key)
  for i in text:
    newText += chr((ord(i)-ord('A') + newKey)%26 + ord('A'))
  return newText


testingText = 'PXPXKXENVDRUXVTNLXHYMXGMAXYKXJNXGVRFXMAHWGXXWLEHGZXKVBIAXKMXQM'
print(f"\n\ninput text: {testingText}")
print(f"\n\nIs this the text: {analyse(testingText)}")



# "PXPXKXENVDRUXVTNLXHYMXGMAXYKXJNXGVRFXMAHWGXXWLEHGZXKVBIAXKMXQM"