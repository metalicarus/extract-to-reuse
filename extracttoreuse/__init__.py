
import logging
from PIL import Image
from extracttoreuse.config.config import Config

logging.basicConfig(filename='application.log', encoding='utf-8', level=logging.DEBUG )


class ExtractToUse:

    def __init__(self):

        path_to_image = 'data/Caras-08-10.jpg'
        img = Image.open(path_to_image)

        logging.info('[APPLICATION][START]')
        config = Config()
        pytesseract = config.getPytesseract()
        text = pytesseract.image_to_string(img)

        file = open('data/text.txt', 'a')
        file.write(text)
        file.close()