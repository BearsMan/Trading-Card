import random
from PIL import Image, ImageDraw

from main import HEIGHT, WIDTH

image = Image.new("RGB", (750, 1050))
WIDTH,HEIGHT = image.size
num_rect = 