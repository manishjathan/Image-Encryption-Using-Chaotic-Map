import generateHenonMap as ghm
from PIL import Image

def pixelManipulation(size,imageName):
    imageMatrix = ghm.getImageMatrix(imageName)
    #for line in imageMatrix:
    #    print(line)
    print("ImageMatrix Rows : %d Cols : %d " % (len(imageMatrix), len(imageMatrix[0])))
    transformationMatrix = ghm.genTransformationMatrix(size)
    #for line in transformationMatrix:
    #    print(line)
    print("Transformation Matrix Rows : %d Cols : %d" %(len(transformationMatrix),len(transformationMatrix[0])))

    #Performing Ex-Or Operation between the transformation Matrix and ImageMatrix
    #Storing the result in resultant Matrix
    resultantMatrix = []
    for i in range(size):
        row = []
        for j in range(size):
            try:
                row.append(transformationMatrix[i][j] ^ imageMatrix[i][j])
            except:
                row = [transformationMatrix[i][j] ^ imageMatrix[i][j]]
        try:
            resultantMatrix.append(row)
        except:
            resultantMatrix = [row]

    print("Pixel Manipulated Values : ")
    for rows in resultantMatrix:
         print(rows)

    # mode = "L", here mode L stands for black and white and Size = "512 * 512"
    #Creating Henon Transformed Image from resultant matrix
    im = Image.new("L", (size, size))
    pix = im.load()
    for x in range(size):
        for y in range(size):
            pix[x, y] = resultantMatrix[x][y]
    im.save("HenonTransformedImage.bmp", "BMP")


pixelManipulation(512,"lena_gray")