import generateArnoldMap as gam
import createImageMatrix as cim
import numpy as np
from PIL import Image

henonEncryptedImage = "HenonTransformedImage.bmp"
mapList = gam.driverProgram()

henonDecryptedImage = cim.getImageMatrix("HenonDecryptedImage.bmp")
arnoldDecryptedImage = []
for i in range(512):
    row = []
    for j in range(512):
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

im = Image.new("L", (512, 512))
pix = im.load()
for x in range(512):
    for y in range(512):
        pix[x, y] = arnoldDecryptedImage[x][y]
im.save("ArnoldDecryptedImage.bmp", "BMP")
