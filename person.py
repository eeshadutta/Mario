from __future__ import print_function
import sys
import time
import os
import subprocess
import config


class Person:
    def __init__(self, x, y, is_alive, lives, bd):
        self.ini_x = x
        self.ini_y = y
        self.x = x
        self.y = y
        self.is_alive = is_alive
        self.lives = lives
        self.kills = 0
        self.coins = 0


class Player(Person):
    def __init__(self, x, y, is_alive, lives, bd, level):
        Person.__init__(self, x, y, is_alive, lives, bd)
        self.score = 0
        self.start_time = round(time.time())
        self.level = level

    def play_time(self):
        return (round(time.time()) - self.start_time)

    def drawPlayer(self, bd):
        for i in range(2):
            for j in range(2):
                bd.buff[self.x + i][self.y + j] = "m"

    def moveLeft(self, bd):
        if (self.y >= (bd._left+7)):
            if bd.buff[self.x][self.y-1] == " " or bd.buff[self.x][self.y-1] == "/" or bd.buff[self.x][self.y-1] == "\\" or bd.buff[self.x][self.y-1] == "C":
                self.y = self.y - 1

    def moveRight(self, bd):
        if (self.y <= (bd._left+(3/4)*bd._width)):
            if bd.buff[self.x][self.y+2] == " " or bd.buff[self.x][self.y+2] == "/" or bd.buff[self.x][self.y+2] == "\\" or bd.buff[self.x][self.y+2] == "C":
                self.y = self.y + 1

    def jump(self, bd, sp_x, sp_y, enemies, objects, scene, coins):
        speed_x = sp_x
        speed_y = sp_y
        flag = 0
        x_threshold = self.ini_x
        x_threshold += 1
        x_ini = self.x
        while (self.x < x_threshold):
            inp = config.get_input_jump()
            if inp == "d":
                if self.y < bd._left+(3/4)*bd._width:
                    speed_y = 1
                else:
                    speed_y = 0
            if inp == "a":
                if self.y > bd._left+7:
                    speed_y = -1
                else:
                    speed_y = 0
            if inp == "q":
                self.gameOver(bd, enemies, "GAME ENDED")

            if self.x < x_ini - 10 or flag == 2:
                speed_x = -2

            if speed_x < 0:
                if speed_y == 0:
                    if bd.buff[self.x+2][self.y] == "X" or bd.buff[self.x+2][self.y] == "-" or bd.buff[self.x+2][self.y] == "|":
                        speed_x = 0
                        speed_y = 0
                        flag = 1
                    elif bd.buff[self.x+3][self.y] == "X" or bd.buff[self.x+3][self.y] == "-" or bd.buff[self.x+3][self.y] == "|" or bd.buff[self.x+3][self.y] == "^":
                        speed_x = -1
                        speed_y = 0
                        flag = 1
                    elif bd.buff[self.x+2][self.y+1] == "X" or bd.buff[self.x+2][self.y+1] == "-" or bd.buff[self.x+2][self.y+1] == "|":
                        speed_x = 0
                        speed_y = 0
                        flag = 1
                    elif bd.buff[self.x+3][self.y+1] == "X" or bd.buff[self.x+3][self.y+1] == "-" or bd.buff[self.x+3][self.y+1] == "|" or bd.buff[self.x+3][self.y+1] == "^":
                        speed_x = -1
                        speed_y = 0
                        flag = 1
                elif speed_y > 0:
                    if bd.buff[self.x+2][self.y+1] == "X" or bd.buff[self.x+2][self.y+1] == "-" or bd.buff[self.x+2][self.y+1] == "|":
                        speed_x = 0
                        speed_y = 0
                        flag = 1
                    elif bd.buff[self.x+3][self.y+1] == "X" or bd.buff[self.x+3][self.y+1] == "-" or bd.buff[self.x+3][self.y+1] == "|" or bd.buff[self.x+3][self.y+1] == "^":
                        speed_x = -1
                        speed_y = 1
                        flag = 1
                    elif bd.buff[self.x+2][self.y+2] == "X" or bd.buff[self.x+2][self.y+2] == "-" or bd.buff[self.x+2][self.y+1] == "|":
                        speed_x = -2
                        speed_y = 0
                        flag = 0
                    elif bd.buff[self.x+3][self.y+2] == "X" or bd.buff[self.x+3][self.y+2] == "-" or bd.buff[self.x+3][self.y+2] == "|" or bd.buff[self.x+3][self.y+2] == "^":
                        speed_x = -2
                        speed_y = 0
                        flag = 0
                else:
                    if bd.buff[self.x+2][self.y] == "X" or bd.buff[self.x+2][self.y] == "-" or bd.buff[self.x+2][self.y] == "|":
                        speed_x = 0
                        speed_y = 0
                        flag = 1
                    elif bd.buff[self.x+3][self.y] == "X" or bd.buff[self.x+3][self.y] == "-" or bd.buff[self.x+3][self.y] == "|" or bd.buff[self.x+3][self.y] == "^":
                        speed_x = -1
                        speed_y = -1
                        flag = 1
                    elif bd.buff[self.x+2][self.y-1] == "X" or bd.buff[self.x+2][self.y-1] == "-" or bd.buff[self.x+2][self.y-1] == "|":
                        speed_x = -2
                        speed_y = 0
                        flag = 0
                    elif bd.buff[self.x+3][self.y-1] == "X" or bd.buff[self.x+3][self.y-1] == "-" or bd.buff[self.x+3][self.y-1] == "|" or bd.buff[self.x+3][self.y-1] == "^":
                        speed_x = -2
                        speed_y = 0
                        flag = 0

            elif speed_x > 0:
                if speed_y == 0:
                    if bd.buff[self.x-1][self.y] == "X" or bd.buff[self.x-1][self.y] == "-" or bd.buff[self.x-1][self.y] == "|":
                        speed_x = 0
                        speed_y = 0
                        flag = 2
                    elif bd.buff[self.x-2][self.y] == "X" or bd.buff[self.x-2][self.y] == "-" or bd.buff[self.x-2][self.y] == "|":
                        speed_x = 1
                        speed_y = 0
                        flag = 2
                    elif bd.buff[self.x-1][self.y+1] == "X" or bd.buff[self.x-1][self.y+1] == "-" or bd.buff[self.x-1][self.y+1] == "|":
                        speed_x = 0
                        speed_y = 0
                        flag = 2
                    elif bd.buff[self.x-2][self.y+1] == "X" or bd.buff[self.x-2][self.y+1] == "-" or bd.buff[self.x-2][self.y+1] == "|":
                        speed_x = 1
                        speed_y = 0
                        flag = 2
                elif speed_y > 0:
                    if bd.buff[self.x-1][self.y+1] == "X" or bd.buff[self.x-1][self.y+1] == "-" or bd.buff[self.x-1][self.y+1] == "|":
                        speed_x = 0
                        speed_y = 0
                        flag = 2
                    elif bd.buff[self.x-2][self.y+1] == "X" or bd.buff[self.x-2][self.y+1] == "-" or bd.buff[self.x-2][self.y+1] == "|":
                        speed_x = 1
                        speed_y = 1
                        flag = 2
                    elif bd.buff[self.x-1][self.y+2] == "X" or bd.buff[self.x-1][self.y+2] == "-" or bd.buff[self.x-1][self.y+2] == "|":
                        speed_x = 2
                        speed_y = 0
                        flag = 0
                    elif bd.buff[self.x-2][self.y+2] == "X" or bd.buff[self.x-2][self.y+2] == "-" or bd.buff[self.x-2][self.y+2] == "|":
                        speed_x = 2
                        speed_y = 0
                        flag = 0
                else:
                    if bd.buff[self.x-1][self.y] == "X" or bd.buff[self.x-1][self.y] == "-" or bd.buff[self.x-1][self.y] == "|":
                        speed_x = 0
                        speed_y = 0
                        flag = 2
                    elif bd.buff[self.x-2][self.y] == "X" or bd.buff[self.x-2][self.y] == "-" or bd.buff[self.x-2][self.y] == "|":
                        speed_x = 1
                        speed_y = -1
                        flag = 2
                    elif bd.buff[self.x-1][self.y-1] == "X" or bd.buff[self.x-1][self.y-1] == "-" or bd.buff[self.x-1][self.y-1] == "|":
                        speed_x = 2
                        speed_y = 0
                        flag = 0
                    elif bd.buff[self.x-2][self.y-1] == "X" or bd.buff[self.x-2][self.y-1] == "-" or bd.buff[self.x-2][self.y-1] == "|":
                        speed_x = 2
                        speed_y = 0
                        flag = 0
            self.x = self.x - speed_x
            if self.x > self.ini_x:
                self.reduceLife(bd, self.x, self.y, enemies)
                return
            self.y = self.y + speed_y

            for i in range(2):
                for j in range(2):
                    x = self.x + i
                    y = self.y + j
                    if bd.buff[x][y] == "$":
                        self.earnCoins()
                        subprocess.Popen(['aplay', './Sounds/mb_coin.wav'])
                        os.system('clear')
                        for c in coins:
                            if c.x == x and c.y == y:
                                coins.remove(c)
                            if c.x == x and c.y + 1 == y:
                                coins.remove(c)
                        break

            x_threshold = self.ini_x

            os.system("clear")
            bd.init_board(self)
            self.drawPlayer(bd)
            for en in enemies:
                if (bd.buff[en.x][en.y] == 'm') or (bd.buff[en.x][en.y + 1] == "m"):
                    subprocess.Popen(['aplay', './Sounds/mb_touch.wav'])
                    os.system('clear')
                    self.killEnemy(en, enemies, bd)
            config.print_screen(self.level, bd, self, enemies, objects, scene, coins)
            time.sleep(.05)

            if flag == 1:
                break

        if self.x >= self.ini_x:
            if bd.buff[self.x+2][self.y] == " " and bd.buff[self.x+2][self.y+1] == " ":
                self.reduceLife(bd, self.x, self.y, enemies)
                return

    def reduceLife(self, bd, x, y, enemies):
        subprocess.Popen(['aplay', './Sounds/mb_die.wav'])
        os.system('clear')
        if self.lives > 0:
            self.lives = self.lives - 1
        if self.lives > 0:
            self.x = self.ini_x
            for y in range(self.y):
                if bd.buff[self.x][self.ini_y + y] == " " and bd.buff[self.x][self.ini_y + y + 1] == " ":
                    self.y = self.ini_y + y
                    break
        elif self.lives == 0:
            self.is_alive = 0
            self.gameOver(bd, enemies, "SORRY YOU LOST. BETTER LUCK NEXT TIME")

    def killEnemy(self, en, enemies, bd):
        en.die(enemies, bd)
        self.kills += 1

    def earnCoins(self):
        self.coins += 1

    def gameOver(self, bd, enemies, msg):
        os.system('clear')
        bd.render(self, enemies)
        print(msg)
        print("YOUR SCORE: ", 100 * self.kills + 100 * self.coins + 50 * (config.timelimit[1] - self.play_time()))
        time.sleep(1)
        sys.exit(0)


class Enemy(Person):
    def __init__(self, x, y, is_alive, lives, bd):
        Person.__init__(self, x, y, is_alive, lives, bd)
        self.speed_y = 1
        self.type = 1    # 1 for normal enemies and 2 for boss enemies

    def drawEnemy(self, bd):
        for i in range(2):
            for j in range(2):
                bd.buff[self.x + i][self.y + j] = "e"

    def moveEnemy(self, player, bd):
        dist = abs(self.y - player.y)
        if (dist >= bd._width/2):
            self.speed_y = 3
        else:
            self.speed_y = 1

        if (self.y > player.y):
            count = 0
            if bd.buff[self.x][self.y - 1] == " " or bd.buff[self.x][self.y - 1] == "m" or bd.buff[self.x][self.y - 1] == "/" or bd.buff[self.x][self.y - 1] == "\\" or bd.buff[self.x][self.y - 1] == "M" or bd.buff[self.x][self.y - 1] == "$":
                count = count + 1
            if bd.buff[self.x][self.y - 2] == " " or bd.buff[self.x][self.y - 2] == "m" or bd.buff[self.x][self.y - 2] == "/" or bd.buff[self.x][self.y - 2] == "\\" or bd.buff[self.x][self.y - 2] == "M" or bd.buff[self.x][self.y - 2] == "$":
                count = count + 2
            if bd.buff[self.x][self.y - 3] == " " or bd.buff[self.x][self.y - 3] == "m" or bd.buff[self.x][self.y - 3] == "/" or bd.buff[self.x][self.y - 3] == "\\" or bd.buff[self.x][self.y - 3] == "M" or bd.buff[self.x][self.y - 3] == "$":
                count = count + 3
            if count == 1:
                self.speed_y = 1
            elif count == 6 and self.speed_y != 1:
                self.speed_y = 3
            if count == 1 or count == 6:
                self.y = self.y - self.speed_y

        elif (self.y < player.y):
            count = 0
            if bd.buff[self.x][self.y + 2] == " " or bd.buff[self.x][self.y + 2] == "m" or bd.buff[self.x][self.y + 2] == "/" or bd.buff[self.x][self.y + 2] == "\\" or bd.buff[self.x][self.y + 2] == "M":
                count = count + 1
            if bd.buff[self.x][self.y + 3] == " " or bd.buff[self.x][self.y + 3] == "m" or bd.buff[self.x][self.y + 3] == "/" or bd.buff[self.x][self.y + 3] == "\\" or bd.buff[self.x][self.y + 3] == "M" or bd.buff[self.x][self.y + 3] == "$":
                count = count + 2
            if bd.buff[self.x][self.y + 4] == " " or bd.buff[self.x][self.y + 4] == "m" or bd.buff[self.x][self.y + 4] == "/" or bd.buff[self.x][self.y + 4] == "\\" or bd.buff[self.x][self.y + 4] == "M" or bd.buff[self.x][self.y + 4] == "$":
                count = count + 3
            if count == 1:
                self.speed_y = 1
            elif count == 6 and self.speed_y != 1:
                self.speed_y = 3
            if count == 1 or count == 6:
                self.y = self.y + self.speed_y

    def killPlayer(self, mario, bd, x, y, enemies):
        mario.reduceLife(bd, x, y, enemies)

    def die(self, enemies, bd):
        self.is_alive = 0
        enemies.remove(self)
