from PIL import Image, ImageOps
im = Image.open("SampleImage.jpg") #Can be many different formats.
pix = im.load()

def getImageMatrix(colorValue):
    image_size = im.size #Get the width and hight of the image for iterating over
    print("Image Size : ",image_size)
    image_matrix = []
    for width in range(int(image_size[0])):
        row = []
        for height in range(int(image_size[1])):
           try:
               #Getting only the blue pixels
                row.append((pix[width,height][colorValue]))
           except:
                row=[pix[width, height][colorValue]]
        try:
            image_matrix.append(row)
        except:
            image_matrix = [row]

    file = open(str(colorValue) +".csv","w")
    file.write(str(image_matrix))
    file.close()
    return image_matrix




