from _tkinter import *
from array import array
from tkinter import CENTER, Button, Entry, Frame, Grid, Label, Tk
from tkinter.messagebox import NO
from tkinter.ttk import Treeview
import os

from extracttoreuse.model.image import Image

class Gui:

    __root = Tk()

    def __init__(self) -> None:
        pass

    def listImages(self):
        path = "C:\\Users\\silvamateus\\python\\extract-to-reuse\\data\\"
        images = []
        for f in os.listdir(path):
            if (os.path.isfile(path + f)):
                if (f.endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif'))):
                    images.append(Image(path + f))
        return images

    def show(self) -> None:
        
        self.__root.title("undefined")
        width=600
        height=500
        screenwidth = self.__root.winfo_screenwidth()
        screenheight = self.__root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.__root.geometry(alignstr)
        self.__root.resizable(width=False, height=False)

        game_frame = Frame(self.__root)
        game_frame.pack()
        my_game = Treeview(game_frame)

        my_game['columns'] = ('id', 'image_path')

        my_game.column("#0", width=0,  stretch=NO)
        my_game.column("id",anchor=CENTER, width=40)
        my_game.column("image_path",anchor=CENTER, width=400)
    

        my_game.heading("#0",text="",anchor=CENTER)
        my_game.heading("id",text="Id",anchor=CENTER)
        my_game.heading("image_path",text="Image path",anchor=CENTER)
 
 
        index = 1
        for image in self.listImages():
            my_game.insert(parent='', index='end', iid=index - 1, text='', values=(index, image.getPath()))
            index = index + 1

        my_game.pack()

        self.__root.mainloop()