from os import name
import random
from re import I
import requests
from PIL import Image, ImageDraw, ImageFont
from name import NameSelector
import Background
from bs4 import BeautifulSoup

image = Image.new("RGB", (750, 750), (0,0,0))
fnt_title = ImageFont.truetype("LucidaTypewriterBold.ttf", 45)
fnt_stat = ImageFont.truetype("LucidaTypewriterBold.ttf", 30)

# global variables
HEIGHT, WIDTH = image.size
draw_image = ImageDraw.Draw(image)
Background_image = Image.open("background.jpg")
image.paste(Background_image), (0, 0)
rarity_value = random.randint(1, 9)


# URL = "https://thispersondoesnotexist.com/image"
# person_image = Image.open(requests.get(URL, stream = True).raw)
# person_resize = person_image.resize((650, 550))
# image.paste(person_resize, (50, 100))
is_image = False

while is_image == False:
  
  URL = "https://marvel.fandom.com/wiki/Special:RandomInCategory/Characters"
  page = requests.get(URL)
  soup = BeautifulSoup(page.content, "html.parser")
  try:
    
    findImage = soup.find("img", class_= "pi-image-thumbnail").attrs["src"]
    img = Image.open(requests.get(findImage, stream = True).raw)
    is_image = True
  except:
    print("image was not found")
img.save('character.png')
person_img = Image.open('character.png')
person_resize = person_img.resize((635, 250))
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
star_image = Image.open("star.png").convert("RGBA")
star_resize = star_image.resize((35, 30))
for idx, i in enumerate(range(rarity_value)):
  
  image.paste(star_resize, (main_Rect[0][0] +(idx * 50), main_Rect[0][1] + 560), star_resize)
bannerRectangle = [(50, HEIGHT - 100), (WIDTH - 50, HEIGHT - 50)]
draw_image.rectangle(bannerRectangle, fill = "white")
draw_image.text((50, HEIGHT - 300), "Strength \n" + str(random.randint(1, 99)),
font = fnt_stat, align = "center")
draw_image.text((WIDTH / 2 - 75, HEIGHT - 300),
"Agility \n" + str(random.randint(1, 99)), font = fnt_stat, align = "center")
draw_image.text((WIDTH - 175, HEIGHT - 300), "Defense \n" + str(random.randint(1, 99)),
font = fnt_stat, align = "center")
name = NameSelector().get_name()
draw_image.text(
  (55, 10),
  name,
  font = fnt_title
)
star_image = Image.open("star.png").convert("RGBA")
star_resize = star_image.resize((35, 30))
for idx, i in enumerate(range(rarity_value)):
  
  image.paste(star_resize, (main_Rect[0][0] +(idx * 50), main_Rect[0][1] + 560), star_resize)
image.save("fullcard.jpg")
