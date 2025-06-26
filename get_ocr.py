import pytesseract as tess
from PIL import Image

try:
    img = Image.open("coffee-meme.png")
    text = tess.image_to_string(img)
    print(text)
except Exception as e:
    print(f"Error: {e}")
