from PIL import Image
import createImageMatrix as cim
import numpy as np
import os

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

def genArnoldMap(res,inputMatrix,numberOfIterations,modN):
    map = {}
    res1 = np.zeros(shape = (2,1))
    res1 = matrixModulo(multiplyMatrix(res,inputMatrix,res1),modN)
    count = 0
    while (res1 != inputMatrix) and (count < numberOfIterations):
        res2 = np.zeros(shape = (2,1))
        res1 = matrixModulo(multiplyMatrix(res,res1,res2),modN)
        count += 1
    newtuple = (res1[0][0],res1[1][0])
    actualtuple = (inputMatrix[0][0],inputMatrix[1][0])
    map[actualtuple] = newtuple
    #print(map)
    return map

def driverProgram(width,height,numberOfIterations,modN):
    n = 2
    mapList = []
    UTM  = np.triu(np.ones((n,n),dtype = int),0)
    LTM =  np.tril(np.ones((n,n),dtype = int),0)
    RM = np.zeros(shape = (n,n))
    res = multiplyMatrix(LTM,UTM,RM)
    #print(res)
    for i in range(width):
        for j in range(height):
            inputMatrix = [[i],[j]]
            map = genArnoldMap(res,inputMatrix,numberOfIterations,modN)
            try:
                mapList.append(map)
            except:
                mapList = [map]
    #print(mapList)
    return mapList

def createArnoldCatImage(imageMatrix,mapList,width,height):
    arnoldImageMatrix = []
    #Creating a zero matrix for arnold Cat map
    for i in range(width):
        row = []
        for j in range(height):
            try:
                row.append((0))
            except:
                row = [(0)]
        try:
            arnoldImageMatrix.append(row)
        except:
            arnoldImageMatrix = [row]

    #Inserting pixel values into arnold Cat Image Matrix
    for map in mapList:
        for keys in map.keys():
            #print(imageMatrix[keys[0]][keys[1]],int(map[keys][0]),int(map[keys][1]))
            arnoldImageMatrix[int(map[keys][0])][int(map[keys][1])] = (imageMatrix[keys[0]][keys[1]])

    #print(arnoldImageMatrix)
    file = open("ArnoldImageMatrix.csv", "w")
    file.write(str(arnoldImageMatrix))
    file.close()

    im = Image.new("L", (width, height))
    pix = im.load()
    for x in range(width):
        for y in range(height):
            pix[x, y] = arnoldImageMatrix[x][y]
    im.save("test.bmp", "BMP")
    absPath = os.path.abspath("test.bmp")
    return absPath

#mapList = driverProgram()
#imageMatrix = cim.getImageMatrix("C:\\Users\\capiot\\PycharmProjects\\ImageEncryption\\lena_gray.bmp")
#resImage = createArnoldCatImage(imageMatrix,mapList)
#print(resImage)








