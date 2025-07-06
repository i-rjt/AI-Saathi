import easyocr
import pytesseract
from PIL import Image, ImageEnhance, ImageFilter


reader = easyocr.Reader(['en'])
text = reader.readtext('./image/temp.jpg', detail=0)

print(text)