from __future__ import print_function
import sys
import config


class Board():

    def __init__(self, height, width, buff_width, level):
        self._height = height
        self._width = width
        self._buff_width = buff_width
        self._left = 0
        self._right = self._width
        self.buff = [[' ' for x in range(self._buff_width)] for y in range(self._height)]
        self.level = level

    def init_board(self, mario):
        w = self._width
        h = self._height
        for i in range(h):
            for j in range(self._left, self._right):
                if (i < 1 or i > (h-2)):
                    self.buff[i][j] = "*"
                elif (i > (h-5) and i <= (h-2)):
                    self.buff[i][j] = "^"
                elif (j < (self._left+1) or j > (self._left+w-2)):
                    self.buff[i][j] = "*"
                else:
                    self.buff[i][j] = " "
        self.buff[1][self._right-16] = "K"
        self.buff[1][self._right-15] = "I"
        self.buff[1][self._right-14] = "L"
        self.buff[1][self._right-13] = "L"
        self.buff[1][self._right-12] = "S"
        self.buff[1][self._right-11] = ":"
        self.buff[1][self._right-10] = mario.kills
        self.buff[1][self._right-9] = " "
        self.buff[1][self._right-8] = "C"
        self.buff[1][self._right-7] = "O"
        self.buff[1][self._right-6] = "I"
        self.buff[1][self._right-5] = "N"
        self.buff[1][self._right-4] = "S"
        self.buff[1][self._right-3] = ":"
        self.buff[1][self._right-2] = mario.coins
        self.buff[2][self._right-16] = "L"
        self.buff[2][self._right-15] = "I"
        self.buff[2][self._right-14] = "V"
        self.buff[2][self._right-13] = "E"
        self.buff[2][self._right-12] = "S"
        self.buff[2][self._right-11] = ":"
        self.buff[2][self._right-10] = mario.lives
        self.buff[2][self._right-9] = " "
        self.buff[2][self._right-8] = "T"
        self.buff[2][self._right-7] = "I"
        self.buff[2][self._right-6] = "M"
        self.buff[2][self._right-5] = "E"
        self.buff[2][self._right-4] = ":"
        self.buff[2][self._right-3] = config.timelimit[1] - mario.play_time()
        for i in range(3):
            self.buff[self._height-28][354+i] = "_"
        self.buff[self._height-28][353] = "/"
        self.buff[self._height-29][354] = "/"
        self.buff[self._height-30][355] = "/"
        self.buff[self._height-31][356] = "/"
        self.buff[self._height-29][357] = "|"
        self.buff[self._height-30][357] = "|"
        self.buff[self._height-31][357] = "|"
        self.buff[self._height-29][358] = "|"
        self.buff[self._height-30][358] = "|"
        self.buff[self._height-31][358] = "|"

    def render(self, mario, enemies):
        if (mario.y >= self._left + (3/4)*self._width):
            self._left += 1
            self._right += 1
            mario.ini_y += 1
            for en in enemies:
                if en.y < self._left:
                    enemies.remove(en)
        for i in range(self._height):
            for j in range(self._left, self._right):
                if self.buff[i][j] == "*" or self.buff[i][j] == "^":
                    print("\033[1;32;40m" + self.buff[i][j], end=' ')
                elif self.buff[i][j] == "m":
                    print("\033[1;36;40m" + self.buff[i][j], end=' ')
                elif self.buff[i][j] == 'e':
                    print("\033[1;31;40m" + self.buff[i][j], end=' ')
                elif self.buff[i][j] == "c":
                    print("\033[1;34;40m" + self.buff[i][j], end=' ')
                elif self.buff[i][j] == "X":
                    print("\033[1;33;40m" + self.buff[i][j], end=' ')
                elif self.buff[i][j] == "/" or self.buff[i][j] == "\\":
                    print("\033[1;37;40m" + self.buff[i][j], end=' ')
                elif self.buff[i][j] == "$":
                    print("\033[1;35;40m" + self.buff[i][j], end=' ')
                elif self.buff[i][j] == "|" or self.buff[i][j] == "-":
                    print("\033[1;34;40m" + self.buff[i][j], end=' ')
                else:
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
