from pyboy import PyBoy
from PIL import Image
pyboy = PyBoy('Games/Tetris.gb')

from time import time

start = time()
while True:
    pyboy.tick()
    
    if time() - start > 10:
        break

import numpy as np

pil_image = pyboy.screen_image()
img = pil_image.resize((8,8), Image.ANTIALIAS)
final = [(r, g, b) for r, g, b in np.asarray(img).reshape(-1, 3)]

from sense_hat import SenseHat

s = SenseHat()
s.set_pixels(final)