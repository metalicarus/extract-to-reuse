from PIL import Image
from pytesseract import pytesseract

path_to_tesseract = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
path_to_image = 'Caras-08-10.jpg'

pytesseract.tesseract_cmd = path_to_tesseract
img = Image.open(path_to_image)

text = pytesseract.image_to_string(img)

file = open('texto.txt', 'a')
file.write(text)
file.close()