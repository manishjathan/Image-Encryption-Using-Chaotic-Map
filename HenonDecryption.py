#Input : Henon Encrypted Image
#Processing:
    #get pixel values of Henon Encrypted Image
    #Ex-Or with Henon generated Matrix
#Output : Henon  Decrypted Image

import createImageMatrix as cim
import generateHenonMap as ghm
from PIL import Image
import os

def decryptHenonImage(imageName):
    imageMatrix = cim.getImageMatrix(imageName)
    transformationMatrix = ghm.genTransformationMatrix(len(imageMatrix))

    henonDecryptedImage = []
    for i in range(len(imageMatrix)):
        row = []
        for j in range(len(imageMatrix)):
            try:
                row.append(imageMatrix[i][j] ^ transformationMatrix[i][j])
            except:
                row = [imageMatrix[i][j] ^ transformationMatrix[i][j]]

        try:
            henonDecryptedImage.append(row)
        except:
            henonDecryptedImage = [row]

    width  = len(imageMatrix[0])
    height = len(imageMatrix)

    im = Image.new("L", (width, height))
    pix = im.load()
    for x in range(width):
        for y in range(height):
            pix[x, y] = henonDecryptedImage[x][y]
    im.save("HenonDecryptedImage.bmp", "BMP")
    #return henonDecryptedImage
    return os.path.abspath("HenonDecryptedImage.bmp")
