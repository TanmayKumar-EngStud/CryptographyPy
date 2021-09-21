
from os import system
system("clear")

# plainText = input("Enter the plain text : ")
# key = input("Enter your key here : ")
import math
plainText = "FKMFIO"
key = "CDDG"

print(f"Plain Text is : {plainText}")
print(f"Key is        : {key}\n")


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

def generateTextMatrix(plainText, key):
    matrix = []
    cols = len(key[0])
    rows = math.floor(len(plainText)/cols)
    for i in range(rows):
        temp =[]
        for j in range(cols):
            temp.append(ord((plainText[i*cols + j]).lower()) - ord('a'))
        matrix.append(temp)
    return matrix


def MultiInv(n):
    for i in range(26):
        if n*i%26 == 1:
            return i

def matrixMultiplication(Matrix2, Matrix1):
    resultantMatrix = []
    for i in range(len(Matrix1)):
        temp = []
        for j in range(len(Matrix2[0])):
            temp.append(0)
        resultantMatrix.append(temp)
    for i in range(len(Matrix1)):
        for j in range(len(Matrix2[0])):
            for k in range(len(Matrix2)):
                resultantMatrix[i][j] += (Matrix1[i][k] * Matrix2[k][j])%26
    showMatrix(resultantMatrix)
    return resultantMatrix

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

    plainTextMatrix  = generateTextMatrix(plainText, keyMatrix)
    cipherTextMatrix = matrixMultiplication(keyMatrix, plainTextMatrix)
    
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

# cipherText = Encryption(plainText, key)
# print(f"\nGenerated Cipher Text : {cipherText}")

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
    print(f"Multiplicative Inverse of Determinant is :{multiInv}")
    newMatrix = divide(Adj(Matrix), multiInv)
    print("Inverse Matrix with (mod 26):")
    showMatrix(newMatrix)
    return newMatrix

def Decryption(cipherText, key):
    keyMatrix = makeKeyMatrix(key)
    cipherMatrix = generateTextMatrix(cipherText, keyMatrix)
    InvKey = InverseMatrix(keyMatrix)
    print("\nInverse Plain Matrix is:")
    plainMatrix = TakeMod(matrixMultiplication(InvKey, cipherMatrix))
    NewplainText =""

    for j in plainMatrix:
        for i in j:
            NewplainText += chr(i+ 65)
    return NewplainText

GeneratedPlainText = Decryption("FKMFIO", key)
print(f"\nGenerated Plain Text : {GeneratedPlainText}")