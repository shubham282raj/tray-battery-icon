from PIL import Image

def create_tray_icon():
    width = 32
    height = 32
    image = Image.new('RGBA', (width, height), (255, 255, 255, 1))

    return image