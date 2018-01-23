import generateArnoldMap as gam
import createImageMatrix as cim
from PIL import Image
import os

def decryptArnoldImage(width,height,numberOfIterations,modN,imageName):

    im = Image.open(imageName)
    image_size = im.size
    width = image_size[0]
    height = image_size[1]

    mapList = gam.driverProgram(width,height,numberOfIterations,modN)
    print(mapList)
    henonDecryptedImage = cim.getImageMatrix(imageName)
    print(henonDecryptedImage)
    arnoldDecryptedImage = []


    for i in range(width):
        row = []
        for j in range(height):
            try:
                row.append((0))
            except:
                row = [(0)]
        try:
            arnoldDecryptedImage.append(row)
        except:
            arnoldDecryptedImage = [row]

    for map in mapList:
        for key,value in map.items():
            print(key[0],key[1],value[0],value[1])
            arnoldDecryptedImage[key[0]][key[1]] = (henonDecryptedImage[int(value[0])][int(value[1])])

    im = Image.new("L", (width, height))
    pix = im.load()
    for x in range(width):
        for y in range(height):
            pix[x, y] = arnoldDecryptedImage[x][y]
    im.save("ArnoldDecryptedImage.bmp", "BMP")
    return os.path.abspath("ArnoldDecryptedImage.bmp")

#decryptArnoldImage("C:/Users/capiot/PycharmProjects/ImageEncryption/HenonDecryptedImage.bmp")
