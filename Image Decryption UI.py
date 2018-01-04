from tkinter import *
from tkinter import filedialog
import os
import HenonDecryption as hD
import ArnoldDecryption as aD
from PIL import ImageTk, Image

def choose_File():
    filename = filedialog.askopenfilename()
    entry1.insert(0,str(filename))

def decryptArnoldShuffle():
    filePath = entry1.get()
    resImage = aD.decryptArnoldImage(filePath)
    entry2.insert(0,resImage)


def decryptHenonManipulation():
    filename = entry1.get()
    resImage = hD.decryptHenonImage(filename)
    entry3.insert(0,resImage)
    #print(filename)

def performEntireDecryption():
    decryptArnoldShuffle()
    filename = entry2.get()
    resImage = hD.decryptHenonImage(filename)
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
topFrame = Frame(root)
topFrame.pack()

middleFrame = Frame(root)
middleFrame.pack(side=BOTTOM)


bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

encryptionFrame = Frame(root)
encryptionFrame.pack(side=BOTTOM)

label_1 = Label(topFrame, text ="Image to be Decrypted : ",width = 125)
entry1 = Entry(topFrame,width =100)
button1 = Button(topFrame, text = "Select Image",command = choose_File)

button2 = Button(middleFrame, text = "Decrypt Arnold Cat Map",command = decryptArnoldShuffle,width=20)
entry2 = Entry(middleFrame,width =80)
button3 = Button(middleFrame, text="Open Image",command = openFileForArnold)

button4 = Button(bottomFrame, text="Decrypt Henon Map",command = decryptHenonManipulation,width=20)
entry3 = Entry(bottomFrame,width =80)
button5 = Button(bottomFrame, text="Open Image",command = openFileForHenon)

button6 = Button(encryptionFrame, text="Perform Decryption",command = performEntireDecryption,width=20)
entry4 = Entry(encryptionFrame,width=80)
button7 = Button(encryptionFrame, text="Open Image",command = openFileForArnold)

label_1.pack(side = TOP)
entry1.pack(side = TOP)
button1.pack(side = TOP)


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