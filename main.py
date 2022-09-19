from sys import platform
from config import Config
import logging
from PIL import Image

logging.basicConfig(filename='application.log', encoding='utf-8', level=logging.DEBUG )

def __init__():
    # path_to_tesseract = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    path_to_image = 'Caras-08-10.jpg'

    # pytesseract.tesseract_cmd = path_to_tesseract
    img = Image.open(path_to_image)

    # text = pytesseract.image_to_string(img)



    logging.info('[APPLICATION][START]')
    config = Config()
    pytesseract = config.getPytesseract()
    text = pytesseract.image_to_string(img)

    file = open('texto.txt', 'a')
    file.write(text)
    file.close()

if __name__ == '__main__':
    __init__()