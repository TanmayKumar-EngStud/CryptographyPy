from os import system
system('clear')
class DES:
  # Matrices for plain text 
  IP = [58,	50,	42,	34,	26,	18,	10,	2,
      60,	52,	44,	36,	28,	20,	12,	4,
      62,	54,	46,	38,	30,	22,	14,	6,
      64,	56,	48,	40,	32,	24,	16,	8,
      57,	49,	41,	33,	25,	17,	9,	1,
      59,	51,	43,	35,	27,	19,	11,	3,
      61,	53,	45,	37,	29,	21,	13,	5,
      63,	55,	47,	39,	31,	23,	15,	7]
  
  XP = [ 32, 1 , 2 , 3 , 4 , 5 , 4 , 5,
         6 , 7 , 8 , 9 , 8 , 9 , 10, 11,
         12, 13, 12, 13, 14, 15, 16, 17,
         16, 17, 18, 19, 20, 21, 20, 21,
         22, 23, 24, 25, 24, 25, 26, 27,
         28, 29, 28, 29, 30, 31, 32, 1 ]

  P =[40, 8, 48, 16, 56, 24, 64, 32,
      39, 7, 47, 15, 55, 23, 63, 31,
      38, 6, 46, 14, 54, 22, 62, 30,
      37, 5, 45, 13, 53, 21, 61, 29,
      36, 4, 44, 12, 52, 20, 60, 28,
      35, 3, 43, 11, 51, 19, 59, 27,
      34, 2, 42, 10, 50, 18, 58, 26,
      33, 1, 41,  9, 49, 17, 57, 25 ]

  # S-boxes
  
  s1 = [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7,
        0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8,
        4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0,
        15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
  s2 = [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10,
        3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5,
        0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15,
        13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]
  s3 = [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8,
        13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1,
        13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7,
        1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]
  s4 = [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15,
        13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9,
        10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4,
        3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]
  s5 = [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9,
        14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6,
        4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14,
        11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]
  s6 = [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11,
        10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8,
        9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6,
        4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]
  s7 = [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1,
        13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6,
        1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2,
        6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]
  s8 = [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7,
        1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2,
        7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8,
        2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]
  
  P_box = [16,	7,	20,	21,	29,	12,	28,	17,
            1,	15,	23,	26,	5,	18,	31,	10,
            2,	8,	24,	14,	32,	27,	3,	9,
            19,	13,	30,	6,	22,	11,	4,	25]
  IPinv = [ 40,	8,	48,	16,	56,	24,	64,	32,
            39,	7,	47,	15,	55,	23,	63,	31,
            38,	6,	46,	14,	54,	22,	62,	30,
            37,	5,	45,	13,	53,	21,	61,	29,
            36,	4,	44,	12,	52,	20,	60,	28,
            35,	3,	43,	11,	51,	19,	59,	27,
            34,	2,	42,	10,	50,	18,	58,	26,
            33,	1,	41,	9,	49,	17,	57,	25]

  # Matrices for keys
  PC_1 = [57,	49,	41,	33,	25,	17,	9,
          1,	58,	50,	42,	34,	26,	18,
          10,	2,	59,	51,	43,	35,	27,
          19,	11,	3,	60,	52,	44,	36,
          63,	55,	47,	39,	31,	23,	15,
          7,	62,	54,	46,	38,	30,	22,
          14,	6,	61,	53,	45,	37,	29,
          21,	13,	5,	28,	20,	12,	4 ]
  PC_2 = [14, 17, 11, 24, 1, 5,
          3, 28, 15, 6, 21, 10,
          23, 19, 12, 4, 26, 8,
          16, 7, 27, 20, 13, 2,
          41, 52, 31, 37, 47, 55,
          30, 40, 51, 45, 33, 48,
          44, 49, 39, 56, 34, 53,
          46, 42, 50, 36, 29, 32]

  def C0_D0(self,key): #Correct
    c0 = []
    d0 = []
    x = []
    for i in self.PC_1:
      x.append(key[i-1])
    for i in range(56):
      c0.append(x[i])
      d0.append(x[i+28])
    return ''.join(c0),''.join(d0)
  def lShift(self,C,D, index): #Correct
    if (index == 1 or index == 2 or index == 9 or index == 16):
      return C[1:] + C[0], D[1:] + D[0]
    else:
      return C[2:] + C[0:2], D[2:] + D[0:2]
  def XOR(self,KeyBuffer, R): #Correct
    ans = ''
    for i in range(len(KeyBuffer)):
      if (KeyBuffer[i] == R[i]):
        ans += '0'
      else:
        ans += '1'
    return ans
  def swap(self, R, L):
    temp = R
    R = L
    L = temp
    return R, L
  def key48_generator(self,C,D):
    key = []
    x = str(C) + str(D)
    for i in self.PC_2:
      key.append(x[i-1])
    i =0
    return ''.join(key)
  
  def permute(self,X,p):
    ans = []
    for i in p:
      ans.append(X[i-1])
    i= 0
    return ''.join(ans)
  
  def substituteS(self, r, S):
    row = int(r[0] + r[5],2)
    col = int(r[1:5],2)
    ans = bin(S[row*16 +col])[2:].zfill(4)
    return ans

  def S_box(self, R):
    r1 = self.substituteS(R[0:6],self.s1)
    r2 = self.substituteS(R[6:12],self.s2)
    r3 = self.substituteS(R[12:18],self.s3)
    r4 = self.substituteS(R[18:24],self.s4)
    r5 = self.substituteS(R[24:30],self.s5)
    r6 = self.substituteS(R[30:36],self.s6)
    r7 = self.substituteS(R[36:42],self.s7)
    r8 = self.substituteS(R[42:48],self.s8)
    return r1+r2+r3+r4+r5+r6+r7+r8
  
  def Iteration(self, L, R, C, D, iterationNo):
    # Key Conversion
    C,D = self.lShift(C,D,iterationNo)
    KeyBuffer = self.key48_generator(C,D)
    R = self.permute(self.R, self.XP)
    R = self.XOR(KeyBuffer, R)
    buff32 = self.S_box(R)
    buff32 = self.permute(buff32, self.P_box)
    newR = self.XOR(buff32, self.L)
    self.L, self.R =self.swap(self.L,newR)

  # Conversion Functions
  def hex2bin(self,hex):
    return bin(int(hex, 16))[2:].zfill(64)
  def bin2hex(bin):
    return hex(int(bin, 2))[2:].zfill(2)
  
  def __init__(self, plaintext, key):
    #store the plain text and the key in Hexadecimal format

      p_text = []
      for i in plaintext:
        p_text.append(ord(i))
      while len(p_text)%8 != 0:
        p_text.append(0)
      
      key_input = []
      for i in key: # This must be the 16 digits of hexadecimal key
        key_input.append(ord(i))
      while len(key_input) < 8:
        key_input.append(0)
      self.plaintext = ' '.join(hex(x)[2:] for x in p_text[0:8])
      self.key       = ' '.join(hex(x)[2:] for x in key_input[0:8])
  
  def remSpace(self,text):
    return text.replace(" ", "")
  def encrypt(self): 
    
    pNum = list(self.plaintext.split(" "))
    kNum = list(self.key.split(" "))
    i= len(pNum)
    j= len(kNum)
    pText = ' '.join(bin(int(x,16))[2:].zfill(8) for x in pNum)
    kText = ' '.join(bin(int(x,16))[2:].zfill(8) for x in kNum)
    self.plaintext = self.remSpace(pText)
    self.key       = self.remSpace(kText)
    self.plaintext = self.permute(self.plaintext, self.IP)
    orgKey = self.key
    self.key       = self.permute(self.key, self.PC_1)
    self.L = self.plaintext[0:32]
    self.R = self.plaintext[32:64]

    C,D = self.key[0:28], self.key[28:56]
    for i in range(16):
      self.Iteration(self.L, self.R, C, D, i)
    self.R, self.L = self.swap(self.R, self.L)
    data = self.L + self.R
    data = self.permute(data, self.IPinv)
    cipher = []
    for i in range(0,len(data),8):
      cipher.append(int(data[i:i+8],2))

    cipher = ''.join(chr(x) for x in cipher)
    self.cipherText = cipher
    self.key = orgKey
    return cipher
  
  def decrypt(self):
    cNum = list(hex(ord(x)) for x in cipherText)
    cText = ' '.join(bin(int(x,16))[2:].zfill(8) for x in cNum)
    self.cipherText = self.remSpace(cText)
    
    self.cipherText = self.permute(self.cipherText, self.IP)
    self.key       = self.permute(self.key, self.PC_1)
    self.L = self.cipherText[0:32]
    self.R = self.cipherText[32:64]

    C,D = self.key[0:28], self.key[28:56]
    for i in range(16):
      self.Iteration(self.R, self.L, C, D, i)
    self.R, self.L = self.swap(self.R, self.L)
    data = self.L + self.R
    data = self.permute(data, self.IPinv)
    cipher = []
    for i in range(0,len(data),8):
      cipher.append(int(data[i:i+8],2))

    cipher = ''.join(chr(x) for x in cipher)
    self.cipherText = cipher
    return cipher


plainText = "BOOMS"
key = "CAPITAL"
des = DES(plainText, key)
cipherText = des.encrypt()
print(cipherText)
plainText = des.decrypt()
print(plainText)
