from PIL import Image


def getImageMatrix(imageName):
    im = Image.open(imageName)
    pix = im.load()
    image_size = im.size #Get the width and hight of the image for iterating over
    print("Image Size : ",image_size)
    image_matrix = []
    for width in range(int(image_size[0])):
        row = []
        for height in range(int(image_size[1])):
           try:
               #Getting only the blue pixels
                row.append((pix[width,height]))
           except:
                row=[pix[width, height]]
        try:
            image_matrix.append(row)
        except:
            image_matrix = [row]

    file = open("ImageMatrix.csv","w")
    file.write(str(image_matrix))
    file.close()
    return image_matrix


#imageMatrix = getImageMatrix()

