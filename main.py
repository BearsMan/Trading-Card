from os import name
import random
from re import I
import requests
from PIL import Image, ImageDraw, ImageFont
from name import NameSelector
import Background

image = Image.new("RGB", (750, 750), (0,0,0))
fnt_title = ImageFont.truetype("LucidaTypewriterBold.ttf", 70)
fnt_stat = ImageFont.truetype("LucidaTypewriterBold.ttf", 30)

# global variables
HEIGHT, WIDTH = image.size
draw_image = ImageDraw.Draw(image)
Background_image = Image.open("background.jpg")
image.paste(Background_image), (0, 0)

URL = "https://thispersondoesnotexist.com/image"
person_image = Image.open(requests.get(URL, stream = True).raw)
person_resize = person_image.resize((650, 550))
image.paste(person_resize, (50, 100))
main_Rect = [
  (50, 100), 
  (WIDTH - 50, HEIGHT - 400)
]
draw_image.rectangle(
  main_Rect, 
  outline = "red", 
  width = 15
)
bannerRectangle = [(50, HEIGHT - 100), (WIDTH - 50, HEIGHT - 50)]
draw_image.rectangle(bannerRectangle, fill = "white")
draw_image.text((50, HEIGHT - 300), "Strength \n 24",
font = fnt_stat, align = "center")
draw_image.text((WIDTH / 2 - 75, HEIGHT - 300),
"Agility \n 30", font = fnt_stat, align = "center")
draw_image.text((WIDTH - 175, HEIGHT - 300), "Defense \n 99",
font = fnt_stat, align = "center")
name = NameSelector().get_name()
draw_image.text(
  (55, 10),
  name,
  font = fnt_title
)

image.save("fullcard.jpg")