from sense_hat import SenseHat

s = SenseHat()

blank = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

"""
make game of snake on 8x8 grid
"""

import random
def make_apple():
  # on crée une pomme au hasard
  apple = (random.randint(0, 7), random.randint(0, 7))

  while apple in snake_body:
      apple = (random.randint(0, 7), random.randint(0, 7))
  
  return apple

def make_snake(dir, snake_body, got_apple):
  # on crée le serpent
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
    return None

  if got_apple:
    return new_snake
  else:
    return new_snake[:-1]
  
def update_map(apple, snake):
  # on met à jour la map avec les nouvelles positions de la pomme et du serpent
  map = [blank]*64
  
  for part in snake:
    map[part[1]*8 + part[0]] = white
    
  map[apple[1]*8 + apple[0]] = red
  
  return map

spawn_x = 3
spawn_y = 3

snake_body = [(spawn_x, spawn_y), (spawn_x-1, spawn_y), (spawn_x-2, spawn_y)]
apple = make_apple()
map = update_map(apple, snake_body)
got_apple = False

from time import sleep
def snake():
  # on crée une boucle de jeu qui fait tourner le jeu
  while True:
      s.set_pixels(map)
      event = s.stick.wait_for_event()
      
      if event.action == "pressed":
        snake_body = make_snake(event.direction, snake_body, got_apple)
        if snake_body == None:
          return
        got_apple = False
      
      if snake_body[0] == apple:
        apple = make_apple()
        got_apple = True
      elif snake_body[0] in snake_body[1:]:
          s.show_message("You died!")
          return
        
      map = update_map(apple, snake_body)
        
      sleep(0.1)