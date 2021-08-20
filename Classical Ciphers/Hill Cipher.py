import math
from os import system
system("clear")

# plainText = input("Enter the plain text : ")
# key = input("Enter your key here : ")

plainText = "ACT"
key = "HILLMAG"

print(f"Plain Text is : {plainText}")
print(f"Key is        : {key}\n")

#I am adding fillers so that if the len(key) is not perfect square thus we can use this additional 
#alphabet to fill the rest of the key matrix
def makeKeyMatrix(key):
    matrix = []
    # I am adding fillers because even if the key's Length is not equivalent to a prefect square 
    # It will still give the correct result.
    fillers = "abcdefghijklmnopqrstuvwxyz"
    MAXLEN = math.ceil(math.sqrt(len(key)))
    for i in range(MAXLEN):
      temp = []
      for j in range(MAXLEN):
        if len(key) < i*MAXLEN + j + 1:
          temp.append(ord(fillers[0])- 97)
          fillers = fillers[1:]
        else:
          temp.append(ord(key[i*MAXLEN + j].lower()) -97)
          fillers = fillers.replace(key[i*MAXLEN + j].lower(), "")
      matrix.append(temp)
    return matrix


#This is just for presentation of how the matrix will look like
def showMatrix(matrix):
    for i in range(len(matrix)):
        for j in range (len(matrix[i])):
            print(f"{matrix[i][j]:{5}}", end=" ")
        print()


def generateTextMatrix(plainText, length = len(plainText)):
    matrix = []
    for i in range(length):
        temp =[]
        if i < len(plainText):
            temp.append(ord(plainText[i].lower()) - 97)
        else:
            temp.append(ord('q') - 97)
        matrix.append(temp)
    return matrix

# def mod(a,b):
#     return a%b

def MultiInv(n):
    for i in range(26):
        if n*i%26 == 1:
            print(f"\nMultiplicative Inverse of Modulation of Determinant is : {i}\n")
            return i
    # if n == 0:
    #     return (26, 0, 1)
    # else:
    #     g, y, x = MultiInv(26 % n)
    #     return (g, x - (26 // n) * y, y)

def matrixMultiply(matrix1, matrix2):
    matrix3 = []
    for i in range(len(matrix1)):
        matrix3.append([])
        for j in range(len(matrix2[0])):
            temp = 0
            for k in range(len(matrix2)):
                temp += (matrix1[i][k] * matrix2[k][j])%26
            matrix3[i].append(temp)
    return matrix3

def TakeMod(Matrix):
    result = []
    for i in range (len(Matrix)):
        temp = []
        for j in range( len(Matrix[0])):
            temp.append(Matrix[i][j]%26)
        result.append(temp)
    return result


def Encryption(plainText, key):
    keyMatrix = makeKeyMatrix(key)
    print("This is the key matrix :")
    showMatrix(keyMatrix)

    plainTextMatrix  = generateTextMatrix(plainText, len(keyMatrix[0]))
    cipherTextMatrix = matrixMultiply(keyMatrix, plainTextMatrix)
    
    cipherText = ""
    print("\nPlain Text Matrix :")
    showMatrix(plainTextMatrix)
    cipherTextMatrix = TakeMod(cipherTextMatrix)
    print("\nCipher Text Matrix :")
    showMatrix(cipherTextMatrix)

    for i in range(len(cipherTextMatrix)):
        for j in range(len(cipherTextMatrix[0])):
            cipherText += chr(cipherTextMatrix[i][j] + 65)
    return cipherText

cipherText = Encryption(plainText, key)
print(f"\nGenerated Cipher Text : {cipherText}")

#Generates the Smaller matrix, just the part of calculation for taking determinant.
def MiniMatrix(Matrix,i):
    newMatrix = []
    for j in range(1, len(Matrix)):
        temp=[]
        for k in range(1, len(Matrix)):
            temp.append(Matrix[j%len(Matrix)][(i+k)%len(Matrix)])
        newMatrix.append(temp)
    if(newMatrix ==[]):
        return 1
    return newMatrix

def Det(Matrix, num =0):
    if len(Matrix)==2:
        return (Matrix[0][0]*Matrix[1][1] - Matrix[1][0]*Matrix[0][1])
    for i in range (len(Matrix)):
        k =MiniMatrix(Matrix,i) 
        num += Matrix[0][i]*Det(k, num)
    return num

def Transpose(Matrix):
    result = []
    size = len(Matrix)
    for i in range (size):
        temp =[]
        for j in range(size):
            temp.append(Matrix[j][i])
        result.append(temp)
    return result

def generateAdj(Matrix):

    newMatrix = Matrix
    newMatrix.append(Matrix[0])
    newMatrix.append(Matrix[1])
    for i in range(len(Matrix)-2):
        newMatrix[i].append(newMatrix[i][0])
        newMatrix[i].append(newMatrix[i][1])
    return newMatrix

def Adj(Matrix):
    newMatrix =generateAdj(Matrix)
    resultantMatrix = []
    for i in range(1,len(newMatrix)-1):
        temp= []
        for j in range(1,len(newMatrix)-1):
            part = newMatrix[i][j]*newMatrix[i+1][j+1] - newMatrix[i+1][j]*newMatrix[i][j+1]
            temp.append(part%26)
        resultantMatrix.append(temp)
    resultantMatrix= Transpose(resultantMatrix)

    print("\nAdjoint With (mod 26): ")
    showMatrix(resultantMatrix)
    return resultantMatrix

def divide(Matrix, number):
    newMatrix=[]
    size = len(Matrix)
    for i in range (size):
        temp = []
        for j in range(size):
            temp.append(((Matrix[i][j]*number)%26))
        newMatrix.append(temp)
    return newMatrix

def InverseMatrix(Matrix):
    newMatrix= []
    det = Det(Matrix)%26
    multiInv = MultiInv(det)
    print(f"\nMultiplicative Inverse of Determinant is :{multiInv}")
    newMatrix = divide(Adj(Matrix), multiInv)
    print("\nInverse Matrix with (mod 26):")
    showMatrix(newMatrix)
    return newMatrix

def Decryption(cipherText, key):
    keyMatrix = makeKeyMatrix(key)
    cipherMatrix = generateTextMatrix(cipherText)
    InvKey = InverseMatrix(keyMatrix)
    plainMatrix = TakeMod(matrixMultiply(InvKey, cipherMatrix))
    NewplainText =""

    for i in plainMatrix:
        NewplainText += chr(i[0]+ 65)
    return NewplainText

GeneratedPlainText = Decryption(cipherText, key)
print(f"\nGenerated Plain Text : {GeneratedPlainText}")