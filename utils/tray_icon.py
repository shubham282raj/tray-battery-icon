from PIL import Image, ImageDraw, ImageFont

def get_max_font_size(text, max_width, max_height):
    size = 1
    font = ImageFont.load_default(size)

    width, height = 0, 0
    
    while width < max_width and height < max_height:
        left, top, right, bottom = font.getbbox(text)
        width = right - left
        height = top - bottom
        size += 1
        font = ImageFont.load_default(size)
        
    return size - 1

def create_tray_icon(number, color):
    width = 32
    height = 32
    text = str(number)
    image = Image.new('RGBA', (width, height), (255, 255, 255, 1))
    
    # draw on the image created
    draw = ImageDraw.Draw(image)

    max_font_size = get_max_font_size(text, width, height)

    draw.text((0,0), text, font=ImageFont.load_default(size=max_font_size), fill=color)

    return image