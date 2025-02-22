from PIL import Image
from IPython.display import display


def display_image(path: str, width: int = 500, height: int = 300):
    img = Image.open(path)
    img = img.resize((width, height), Image.Resampling.LANCZOS)
    display(img)
