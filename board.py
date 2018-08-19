from __future__ import print_function
import signal,copy,sys,time
from random import randint
import config


class Board():

    def __init__(self, height, width, buff_width, level):
        self.height = height
        self.width = width
        self.buff_width = buff_width
        self.left = 0
        self.right = self.width
        self.buff = [[' ' for x in range(self.buff_width)] for y in range(self.height)]
        self.level = level

    def init_board(self, mario):
        w = self.width
        h = self.height
        for i in range(h):
            for j in range(self.left, self.right):
                if (i<1 or i>(h-2)):
                    self.buff[i][j] = "*"
                elif (i>(h-5) and i<=(h-2)):
                    self.buff[i][j] = "^"
                elif (j<(self.left+1) or j>(self.left+w-2)):
                    self.buff[i][j] = "*"
                else:
                    self.buff[i][j] = " "
        self.buff[1][self.right-16] = "K"
        self.buff[1][self.right-15] = "I"
        self.buff[1][self.right-14] = "L"
        self.buff[1][self.right-13] = "L"
        self.buff[1][self.right-12] = "S"
        self.buff[1][self.right-11] = ":"
        self.buff[1][self.right-10] = mario.kills
        self.buff[1][self.right-9] = " "
        self.buff[1][self.right-8] = "C"
        self.buff[1][self.right-7] = "O"
        self.buff[1][self.right-6] = "I"
        self.buff[1][self.right-5] = "N"
        self.buff[1][self.right-4] = "S"
        self.buff[1][self.right-3] = ":"
        self.buff[1][self.right-2] = mario.coins
        self.buff[2][self.right-8] = "L"
        self.buff[2][self.right-7] = "I"
        self.buff[2][self.right-6] = "V"
        self.buff[2][self.right-5] = "E"
        self.buff[2][self.right-4] = "S"
        self.buff[2][self.right-3] = ":"
        self.buff[2][self.right-2] = mario.lives
        for i in range(3):
            self.buff[self.height-28][354+i] = "_"
        self.buff[self.height-28][353] = "/"
        self.buff[self.height-29][354] = "/"
        self.buff[self.height-30][355] = "/"
        self.buff[self.height-31][356] = "/"
        self.buff[self.height-29][357] = "|"
        self.buff[self.height-30][357] = "|"
        self.buff[self.height-31][357] = "|"
        self.buff[self.height-29][358] = "|"
        self.buff[self.height-30][358] = "|"
        self.buff[self.height-31][358] = "|"


    def render(self, mario, enemies):
        if (mario.y >= self.left + (3/4)*self.width):
            self.left += 1
            self.right += 1
            mario.ini_y += 1
            for en in enemies:
                if en.y < self.left:
                    enemies.remove(en)
        for i in range(self.height):
            for j in range(self.left, self.right):
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
        