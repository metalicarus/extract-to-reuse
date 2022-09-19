from pytesseract import pytesseract
from sys import platform
from os.path import exists
import json
from ..log.wraplog import WrapLog

class Config:

    def __init__(self):
        self.__log = WrapLog().log()
        self.__log.info('[CONFIG][__init__]')
        file = self.__getConfigFile()
        path = file['tesseract']['path'][platform] + file['tesseract']['file'][platform]
        if (platform == 'win32'):
            self.__log.info('[PLATFORM]=win32')
            self.__log.info(path)
            check = self.__checkPathToTesseract(path)
            if (check == False):
                self.__log.error("tesseract was not found")
                exit()
        else:
            self.__log.info('[PLATFORM]=linux')
        self.__path_to_tesseract = path

    def __checkPathToTesseract(self, path: str):
        return exists(path)

    def __getConfigFile(self):
        return json.load(open("data/params.json"))
    
    def getPytesseract(self) -> pytesseract:
        print(self.__path_to_tesseract)
        pytesseract.tesseract_cmd = self.__path_to_tesseract
        return pytesseract