import random
from PIL import Image, ImageDraw, ImageFont

image = Image.new("RGB", (750, 750), (0,0,0))
fnt_title = ImageFont.truetype("LucidaTypewriterBold.ttf", 70)
fnt_stat = ImageFont.truetype("LucidaTypewriterBold.ttf", 30)

# global variables
HEIGHT,WIDTH = image.size
draw_image = ImageDraw.Draw(image)

mainRectangle = [(750,750), (WIDTH -50, HEIGHT - 200)]
draw_image.rectangle(mainRectangle, outline = "red", width = 15)
image.save("fullcard.jpg")