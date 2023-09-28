import random
from PIL import Image, ImageDraw


# Create an image for the card.
image = Image.new("RGB", (750, 1050))
WIDTH, HEIGHT = image.size
num_rect = random.randint(50, 100)
draw_image = ImageDraw.Draw(image)

# for loops for width, and height.
for i in range(num_rect):
# create a rectangle shape.
  rec_width = random.randint(10, 100)
  rec_height = random.randint(10, 100)
  rec_x = random.randint(0, WIDTH)
  rec_y = random.randint(0, HEIGHT)

  rec_shape = [
    (rec_x, rec_y), 
    (rec_x + rec_width, rec_y + rec_height)
  ]

# Draw rectangle
  draw_image.rectangle(
    rec_shape, 
    fill = (
      random.randint(0, 255), 
      random.randint(0, 255), 
      random.randint(0, 255)
    )
  )
image.save("background.jpg")