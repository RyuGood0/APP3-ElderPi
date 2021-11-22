blank = (0, 0, 0)
White = (255, 255, 255)
red = (255, 0, 0)

"""
make game of snake on 8x8 grid
"""

def make_map():
    O = blank
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

map = make_map()

x = 3
y = 3

snake_length = 3

snake_body = [(x, y), (x-1, y), (x-2, y)]

for part in snake_body:
    map[part[1]*8 + part[0]] = White

import random
apple = (random.randint(0, 7), random.randint(0, 7))

while apple in snake_body:
    apple = (random.randint(0, 7), random.randint(0, 7))

map[apple[1]*8 + apple[0]] = red

for i in range(8):
    print(map[i*8:i*8+8])