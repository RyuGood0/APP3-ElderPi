from sense_hat import SenseHat

s = SenseHat()

blank = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

"""
make game of snake on 8x8 grid
"""

def make_map():
    logo = [blank]*64
    return logo

import random
def make_apple():
  apple = (random.randint(0, 7), random.randint(0, 7))

  while apple in snake_body:
      apple = (random.randint(0, 7), random.randint(0, 7))
  
  return apple

def make_snake(dir, snake_body):
  new_snake = [(x, y) for x, y in snake_body]
  
  if dir == "up":
    new_snake.insert(0, (snake_body[0][0], snake_body[0][1]-1))
  elif dir == "down":
    new_snake.insert(0, (snake_body[0][0], snake_body[0][1]+1))
  elif dir == "left":
    new_snake.insert(0, (snake_body[0][0]-1, snake_body[0][1]))
  elif dir == "right":
    new_snake.insert(0, (snake_body[0][0]+1, snake_body[0][1]))
      
  if new_snake[0][0] > 7 or new_snake[0][0] < 0 or new_snake[0][1] < 0 or new_snake[0][1] > 7:
    s.show_message("You died!")
    exit(1)

  new_snake = new_snake[:-1]
  
  return new_snake

def update_map(apple, snake):
  map = [blank]*64
  
  for part in snake:
    map[part[1]*8 + part[0]] = white
    
  map[apple[1]*8 + apple[0]] = red
  
  return map

x = 3
y = 3

snake_body = [(x, y), (x-1, y), (x-2, y)]
apple = make_apple()
map = update_map(apple, snake_body)

from time import sleep
while True:
    s.set_pixels(map)
    event = s.stick.wait_for_event()
    
    if event.action == "pressed":
      snake_body = make_snake(event.direction, snake_body)
    
    if snake_body[0] == apple:
      if snake_body[-1][0] > snake_body[-2][0]:
        snake_body.append((snake_body[-1][0]+1, snake_body[-1][1]))
      elif snake_body[-1][0] < snake_body[-2][0]:
        snake_body.append((snake_body[-1][0]-1, snake_body[-1][1]))
      elif snake_body[-1][1] > snake_body[-2][1]:
        snake_body.append((snake_body[-1][0], snake_body[-1][1]+1))
      elif snake_body[-1][1] > snake_body[-2][1]:
        snake_body.append((snake_body[-1][0], snake_body[-1][1]-1))
      
      apple = make_apple()
    elif snake_body[0] in snake_body[1:]:
        s.show_message("You died!")
        break
      
    map = update_map(apple, snake_body)
      
    sleep(0.1)