from PIL import Image
import createImageMatrix as cim
import numpy as np

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

def genArnoldMap(res,inputMatrix):
    map = {}
    res1 = np.zeros(shape = (2,1))
    res1 = matrixModulo(multiplyMatrix(res,inputMatrix,res1),50)
    count = 0
    while (res1 != inputMatrix) and (count < 10):
        res2 = np.zeros(shape = (2,1))
        res1 = matrixModulo(multiplyMatrix(res,res1,res2),50)
        count += 1
    newtuple = (res1[0][0],res1[1][0])
    actualtuple = (inputMatrix[0][0],inputMatrix[1][0])
    map[actualtuple] = newtuple
    return map

def driverProgram():
    n = 2
    mapList = []
    UTM  = np.triu(np.ones((n,n),dtype = int),0)
    LTM =  np.tril(np.ones((n,n),dtype = int),0)
    RM = np.zeros(shape = (n,n))
    res = multiplyMatrix(LTM,UTM,RM)
    print(res)
    for i in range(50):
        for j in range(50):
            inputMatrix = [[i],[j]]
            map = genArnoldMap(res,inputMatrix)
            try:
                mapList.append(map)
            except:
                mapList = [map]
    print(mapList)
    return mapList

def createArnoldCatImage():
    arnoldImageMatrix = []
    #Creating a zero matrix for arnold Cat map
    for i in range(50):
        row = []
        for j in range(50):
            try:
                row.append((0,0,0))
            except:
                row = [(0,0,0)]
        try:
            arnoldImageMatrix.append(row)
        except:
            arnoldImageMatrix = [row]

    #Inserting pixel values into arnold Cat Image Matrix
    for map in mapList:
        for keys in map.keys():
            print(imageMatrix[keys[0]][keys[1]],int(map[keys][0]),int(map[keys][1]))
            arnoldImageMatrix[int(map[keys][0])][int(map[keys][1])] = (imageMatrix[keys[0]][keys[1]])

    print(arnoldImageMatrix)
    file = open("ArnoldImageMatrix.csv", "w")
    file.write(str(arnoldImageMatrix))
    file.close()

    im = Image.new("RGB", (50, 50))
    pix = im.load()
    for x in range(50):
        for y in range(50):
            pix[x, y] = arnoldImageMatrix[x][y]
    im.save("test.png", "PNG")

mapList = driverProgram()
imageMatrix = cim.getImageMatrix()
createArnoldCatImage()






