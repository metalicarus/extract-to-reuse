from pytesseract import pytesseract
from sys import platform
from os.path import exists
import json
import logging
logging.basicConfig(filename='application.log', encoding='utf-8', level=logging.DEBUG )

class Config:

    def __init__(self):
        logging.info('[CONFIG][__init__]')
        file = self.__getConfigFile()
        path = file['tesseract']['path'][platform] + file['tesseract']['file'][platform]

        if (platform == 'win32'):
            logging.info('[PLATFORM]=win32')
            logging.info(path)
            check = self.__checkPathToTesseract(path)
            if (check == False):
                logging.error("tesseract was not found")
                exit()
        else:
            logging.info('[PLATFORM]=linux')
        
        self.__path_to_tesseract = path

    def __checkPathToTesseract(self, path: str):
        return exists(path)

    def __getConfigFile(self):
        return json.load(open("data/params.json"))
    
    def getPytesseract(self) -> pytesseract:
        print(self.__path_to_tesseract)
        pytesseract.tesseract_cmd = self.__path_to_tesseract
        return pytesseract