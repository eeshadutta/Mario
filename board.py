from __future__ import print_function
import signal,copy,sys,time
from random import randint
import config


#buff = [[' ' for x in range(80)] for y in range(30)]


class Board():

    def __init__(self, height, width, level):
        self.height = height
        self.width = width
        #self.width_sc = width
        self.buff = [[' ' for x in range(self.width)] for y in range(self.height)]
        self.level = level

        self.init_board()

    def init_board(self):
        w = self.width
        h = self.height
        for i in range(h):
            for j in range(w):
                if (i<1 or i>(h-2)):
                    self.buff[i][j] = "*"
                elif (i>(h-5) and i<=(h-2)):
                    self.buff[i][j] = "^"
                elif (j<1 or j>(w-2)):
                    self.buff[i][j] = "*"
                else:
                    self.buff[i][j] = " "

    def render(self):
        for i in range(self.height):
            for j in range(self.width):
                print(self.buff[i][j], end=' ')
            print()

    def process_input(self, player, key_press):
        if key_press == config.RIGHT:
            player.moveRight()
        elif key_press == config.LEFT:
            player.moveLeft()
        elif key_press == config.QUIT:
            sys.exit(0)

        player.drawPlayer()
        