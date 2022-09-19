from _tkinter import *
from tkinter import Button, Entry, Frame, Grid, Label, Tk

class Gui:

    __root = Tk()

    def __init__(self) -> None:
        pass

    def show(self) -> None:
        self.__root.title("undefined")
        width=600
        height=500
        screenwidth = self.__root.winfo_screenwidth()
        screenheight = self.__root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.__root.geometry(alignstr)
        self.__root.resizable(width=False, height=False)


        txtfld=Entry(self.__root, text="This is Entry Widget", bd=5)
        txtfld.place(x=80, y=150)

 

        table = Grid(self.__root, )
        table.place(x=60, y=50)


        self.__root.mainloop()