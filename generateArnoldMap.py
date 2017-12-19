import createImageMatrix as cim
import numpy as np
from scipy.linalg import toeplitz


def multiplyMatrix(A,B,res):
    if len(A[0]) == len(B):
        for i in range(len(A)):
            for j in range(len(B[0])):
                for k in range(len(A[0])):
                    res[i][j] =  res[i][j] + A[i][k]*B[k][j]
    return res

def matrixModulo(inputMatrix,n):
    newMatrix = []
    for row in inputMatrix:
        newRow= []
        for el in row:
            newEl = el%n
            try:
                newRow.append(newEl)
            except:
                newRow = [newEl]
        try:
            newMatrix.append(newRow)
        except:
            newMatrix = [newRow]
    return newMatrix

def findMatch(res,inputMatrix):
    res1 = np.zeros(shape = (175,175))
    res1 = matrixModulo(multiplyMatrix(res,inputMatrix,res1),175)
    count = 0
    while (res1 != inputMatrix) and (count < 1000):
        res2 = np.zeros(shape = (175,175))
        res1 = matrixModulo(multiplyMatrix(res,res1,res2),175)
        count += 1
        print(count)
    print("Number of Iterations : ",count)



def driverProgram():
    n = 175
    UTM  = np.triu(np.ones((n,n),dtype = int),0)
    LTM =  np.tril(np.ones((n,n),dtype = int),0)
    RM = np.zeros(shape = (n,n))
    res = multiplyMatrix(LTM,UTM,RM)
    print(res)
    bluePixelMatrix = cim.getImageMatrix(2)
    findMatch(res,bluePixelMatrix)

driverProgram()

#redPixelMatrix = cim.getImageMatrix(0)
#greenPixelMatrix = cim.getImageMatrix(1)
#bluePixelMatrix = cim.getImageMatrix(2)







