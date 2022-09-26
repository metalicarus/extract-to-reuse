from _tkinter import *
from array import array
from tkinter import CENTER, LEFT, TRUE, Button, Entry, Frame, Grid, Label, Tk
from tkinter import filedialog
from tkinter.filedialog import FileDialog
from tkinter.messagebox import NO
from tkinter.ttk import Treeview
import os

from extracttoreuse.model.image import Image

class Gui:

    __root = Tk()
    __path = ""
    __images = []


    def __init__(self) -> None:
        pass

    def show(self) -> None:
        self.__root.title("Extract to reuse")
        self.__root.geometry('%dx%d+%d+%d' % (600, 500, (self.__root.winfo_screenwidth() - 600) / 2, (self.__root.winfo_screenheight() - 500) / 2))
        self.__root.resizable(width=False, height=False)
        self.__generatePathDialogBtn()
        self.__generateTable()
        self.__root.mainloop()
    
    def __listImages(self) -> None:
        self.__images = []
        for f in os.listdir(self.__path):
            if (f.endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif'))):
                self.__images.append(Image(self.__path + f))

    def __selectPath(self) -> None:
        self.__path = filedialog.askdirectory(initialdir="/", title="Select a dir")
        self.__populate()

    def __populate(self) -> None:
        index = 1
        self.__listImages()
        for image in self.__images:
            self.__root.treeview.insert(parent='', index='end', iid=index - 1, text='', values=(index, image.getPath()))
            index = index + 1

    def __generateTable(self) -> None:
        frame = Frame(self.__root)
        frame.pack()
        self.__root.treeview = Treeview(frame)
        self.__root.treeview['columns'] = ('id', 'image_path')
        self.__root.treeview.column("#0", width=0,  stretch=NO)
        self.__root.treeview.column("id",anchor=CENTER, width=40)
        self.__root.treeview.column("image_path",anchor=CENTER, width=400)
        self.__root.treeview.heading("#0",text="",anchor=CENTER)
        self.__root.treeview.heading("id",text="Id",anchor=CENTER)
        self.__root.treeview.heading("image_path",text="Image path",anchor=CENTER)
        self.__root.treeview.pack()

    def __generatePathDialogBtn(self) -> None:
        Button(self.__root, text= "Select a directory", command=self.__selectPath, width= 35).grid(row=1, column=1)