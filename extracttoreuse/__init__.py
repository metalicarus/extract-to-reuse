
import logging
from PIL import Image
from extracttoreuse.config.config import Config
from extracttoreuse.log.wraplog import WrapLog
from extracttoreuse.gui.gui import Gui

class ExtractToUse:

    def __init__(self):

        gui = Gui()
        gui.show()


        # self.__log = WrapLog().log()
        # path_to_image = 'data/Caras-08-10.jpg'
        # img = Image.open(path_to_image)

        # self.__log.info('[APPLICATION][START]')
        # config = Config()
        # pytesseract = config.getPytesseract()
        # text = pytesseract.image_to_string(img)

        # file = open('data/text.txt', 'a')
        # file.write(text)
        # file.close()