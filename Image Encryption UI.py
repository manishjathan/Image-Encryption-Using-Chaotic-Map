from tkinter import *
from tkinter import filedialog
import os
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
    entry2.insert(0,absFilePath)


def performHenonManipulation():
    filename = entry1.get()
    print(filename)

def openFile():
    #root.destroy()
    window = Tk()
    window.title("Join")
    window.geometry("600x600")
    window.configure(background='grey')

    path = "lena_gray.bmp"
    fullpath = os.path.abspath(path)
    print(fullpath)
    # Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
    img = ImageTk.PhotoImage(Image.open(fullpath))

    # The Label widget is a standard Tkinter widget used to display a text or image on the screen.
    panel = Label(window, image=img)

    # The Pack geometry manager packs widgets in rows or columns.
    panel.pack(side="bottom", fill="both", expand="yes")

    # Start the GUI
    window.mainloop()
#from tkFileDialog import askopenfilename

root =Tk()
topFrame = Frame(root)
topFrame.pack()

middleFrame = Frame(root)
middleFrame.pack(side=BOTTOM)

bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

label_1 = Label(topFrame, text ="Image to be Encrypted : ",width = 125)
entry1 = Entry(topFrame,width =100)
button1 = Button(topFrame, text = "Select Image",command = choose_File)

button2 = Button(middleFrame, text = "Generate Arnold Cat Map",command = performArnoldShuffle)
entry2 = Entry(middleFrame,width =80)
button3 = Button(middleFrame, text="Open Image",command = openFile)


button4 = Button(bottomFrame, text="Generate Henon Map",command = performHenonManipulation)
entry3 = Entry(bottomFrame,width =80)
button5 = Button(bottomFrame, text="Open Image")

label_1.pack(side = TOP)
entry1.pack(side = TOP)
button1.pack(side = TOP)


button2.pack(side = LEFT)
entry2.pack(side=LEFT)
button3.pack(side=LEFT)

button4.pack(side = LEFT)
entry3.pack(side = LEFT)
button5.pack(side = LEFT)

root.mainloop()