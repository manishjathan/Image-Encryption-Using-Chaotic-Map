from tkinter import *
from tkinter import filedialog
import os
import generateArnoldMap as gam
import ImageTransformation as iT
from PIL import ImageTk, Image

def choose_File():
    filename = filedialog.askopenfilename()
    entry1.insert(0,str(filename))

def performArnoldShuffle():
    filePath = entry1.get()
    #print(filename)
    fileNameArr = filePath.split("/")
    fileName = fileNameArr[len(fileNameArr)-1]
    print(fileName)
    absFilePath = os.path.abspath(fileName)
    print(absFilePath)

    im = Image.open(absFilePath)
    image_size = im.size

    width = image_size[0]
    height = image_size[1]

    numberOfIterations = int(entry5.get())
    modN = int(entry6.get())

    mapList = gam.driverProgram(width,height,numberOfIterations,modN)
    imageMatrix = gam.cim.getImageMatrix(absFilePath)
    resImage = gam.createArnoldCatImage(imageMatrix,mapList,width,height)
    entry2.insert(0,resImage)

def performHenonManipulation():
    filename = entry1.get()
    resImage = iT.pixelManipulation(512, filename)
    entry3.insert(0,resImage)
    #print(filename)

def performEntireEncryption():
    performArnoldShuffle()
    filename = entry2.get()
    resImage = iT.pixelManipulation(512, filename)
    entry3.insert(0, resImage)
    entry4.insert(0, resImage)


def openFileForArnold():
    window = Toplevel(root)
    window.title("Arnold Map")
    window.geometry("600x600")
    path = entry2.get()
    img = ImageTk.PhotoImage(Image.open(path))
    panel = Label(window, image=img)
    panel.pack(side="bottom", fill="both", expand="yes")
    window.mainloop()

def openFileForHenon():
    window = Toplevel(root)
    window.title("Henon Map")
    window.geometry("600x600")
    path = entry3.get()
    img = ImageTk.PhotoImage(Image.open(path))
    panel = Label(window, image=img)
    panel.pack(side="bottom", fill="both", expand="yes")
    window.mainloop()

#from tkFileDialog import askopenfilename

root =Tk()
Frame1 = Frame(root)
Frame1.pack()

Frame2 = Frame(root)
Frame2.pack(side=TOP)

Frame3 = Frame(root)
Frame3.pack(side=TOP)

Frame4 = Frame(root)
Frame4.pack(side =TOP)

Frame5 = Frame(root)
Frame5.pack(side=TOP)

label_1 = Label(Frame1, text ="Image to be Encrypted : ",width = 125)
entry1 = Entry(Frame1,width =100)
button1 = Button(Frame1, text = "Select Image",command = choose_File)

label_2 = Label(Frame2,text = "No. Of Iterations:")
entry5 = Entry(Frame2,width = 80)

label_3 = Label(Frame2,text = "Value of mod N:")
entry6 = Entry(Frame2,width = 80)

button2 = Button(Frame3, text = "Generate Arnold Cat Map",command = performArnoldShuffle,width=20)
entry2 = Entry(Frame3,width =80)
button3 = Button(Frame3, text="Open Image",command = openFileForArnold)

button4 = Button(Frame4, text="Generate Henon Map",command = performHenonManipulation,width=20)
entry3 = Entry(Frame4,width =80)
button5 = Button(Frame4, text="Open Image",command = openFileForHenon)

button6 = Button(Frame5, text="Perform Encryption",command = performEntireEncryption,width=20)
entry4 = Entry(Frame5,width=80)
button7 = Button(Frame5, text="Open Image",command = openFileForHenon)

label_1.pack(side = TOP)
entry1.pack(side = TOP)
button1.pack(side = TOP)

label_2.pack(side = TOP)
entry5.pack(side = TOP)

label_3.pack(side = TOP)
entry6.pack(side =TOP)

button2.pack(side = LEFT)
entry2.pack(side=LEFT)
button3.pack(side=LEFT)

button4.pack(side = LEFT)
entry3.pack(side = LEFT)
button5.pack(side = LEFT)

button6.pack(side = LEFT)
entry4.pack(side =LEFT)
button7.pack(side=LEFT)

root.mainloop()