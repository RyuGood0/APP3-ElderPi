from sense_hat import SenseHat
import time

s = SenseHat()
s.low_light = True

nothing = (0,0,0)
white = (255, 255, 255)

def flash_bang():
    W = white
    logo = [
    W, W, W, W, W, W, W, W,
    W, W, W, W, W, W, W, W,
    W, W, W, W, W, W, W, W,
    W, W, W, W, W, W, W, W,
    W, W, W, W, W, W, W, W,
    W, W, W, W, W, W, W, W,
    W, W, W, W, W, W, W, W,
    W, W, W, W, W, W, W, W,
    ]
    return logo

def blank():
    O = nothing
    logo = [
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    ]
    return logo

import random
while True: 
    s.set_pixels(flash_bang())
    time.sleep(random.random()*0.1)
    s.set_pixels(blank())
    time.sleep(random.random()*0.1)