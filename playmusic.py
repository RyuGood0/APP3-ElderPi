import os
import sys
import shlex
from subprocess import Popen

import random
from sense_hat import SenseHat
s = SenseHat()
def playmusic():

    path = '/home/pi/songs'

    print(path + '\n')
    musics = os.listdir(path) # list of all musics

    song = random.randint(0,len(musics)-1)


    print(song)
    proces = Popen(shlex.split('mpg321 "' + path + '/'+musics[song] + '"'))
    while True:
        event = s.stick.wait_for_event()
        if event.action == "pressed":
            if event.direction == 'middle':
                proces.terminate()
                break
            elif event.direction == 'right':
                song = (song + 1) % (len(musics) -1)
                proces.terminate()
                proces = Popen(shlex.split('mpg321 "' + path + '/'+musics[song] + '"'))

            elif event.direction == 'left':
                song = song - 1
                if song == -1 : 
                    song = len(musics) -1 
                proces.terminate()
                proces = Popen(shlex.split('mpg321 "' + path + '/'+musics[song] + '"'))

