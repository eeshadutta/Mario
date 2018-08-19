from __future__ import print_function
import signal,copy,sys,time,os
from random import randint
import config
import board


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
        if (self.y >= (bd.left+7)):
            self.y = self.y - 1

    def moveRight(self, bd):
        if (self.y <= (bd.left+(3/4)*bd.width)):
            self.y = self.y + 1

    def jump(self, bd, prev, enemies, objects, scene):
        speed_x = 4 
        speed_y = prev
        if (self.y <= bd.left+7) or (self.y >= (bd.left+(3/4)*bd.width)):
            speed_y = 0

        self.x = self.x - speed_x
        self.y = self.y + speed_y
        bd.init_board(self)
        self.drawPlayer(bd)
        for en in enemies:
            if (bd.buff[en.x][en.y] == 'm') or (bd.buff[en.x][en.y + 1] == "m"):
                self.killEnemy(en, enemies, bd)
        config.print_screen(self.level, bd, self, enemies, objects, scene)            
        bd.render(self, enemies)
        
        while (self.x < self.ini_x):
            speed_x = speed_x - 1
            self.y = self.y + speed_y
            bd.init_board(self)
            self.x = self.x - speed_x
            self.drawPlayer(bd)
            for en in enemies:
                if (bd.buff[en.x][en.y] == 'm') or (bd.buff[en.x][en.y + 1] == "m"):
                    self.killEnemy(en, enemies, bd)
            config.print_screen(self.level, bd, self, enemies, objects, scene)            
            time.sleep(.05)

    def reduceLife(self, bd, x, y, enemies):
        if self.lives > 0:
            self.lives = self.lives - 1
        if self.lives > 0:
            self.x = self.ini_x
            self.y = self.ini_y
        elif self.lives == 0:
            self.is_alive = 0
            self.gameOver(bd, enemies)

    def killEnemy(self, en, enemies, bd):
        en.die(enemies, bd)
        self.kills += 1

    def gameOver(self, bd, enemies):
        os.system('clear')
        bd.render(self, enemies)
        print("GAME OVER!!!")
        print("YOUR SCORE: ", 100 * self.kills + 50 * (config.timelimit[1] - self.play_time()))
        time.sleep(2)
        sys.exit(0)
        



class Enemy(Person):
    def __init__(self, x, y, is_alive, lives, bd):
        Person.__init__(self, x, y, is_alive, lives, bd)
        self.speed_y = 1
        self.type = 1 #1 for normal enemies and 2 for boss enemies

    def drawEnemy(self, bd):
        for i in range(2):
            for j in range(2):
                bd.buff[self.x + i][self.y + j] = "e"

    def moveEnemy(self, player, bd):
        dist = abs(self.y - player.y)
        if (dist >= bd.width/2):
            self.speed_y = 3
        else:
            self.speed_y = 1

        if (self.y > player.y):
            count = 0
            if bd.buff[self.x][self.y - 1] == " " or bd.buff[self.x][self.y - 1] == "m" or bd.buff[self.x][self.y - 1] == "/" or bd.buff[self.x][self.y - 1] == "\\" or bd.buff[self.x][self.y - 1] == "M":
                count = count + 1
            if bd.buff[self.x + 1][self.y - 1] == " " or bd.buff[self.x + 1][self.y - 1] == "m" or bd.buff[self.x + 1][self.y - 1] == "/" or bd.buff[self.x + 1][self.y - 1] == "\\" or bd.buff[self.x + 1][self.y - 1] == "M":
                count = count + 1
            if count == 2:
                self.y = self.y - self.speed_y

        elif (self.y < player.y):
            count = 0
            if bd.buff[self.x][self.y + 2] == " " or bd.buff[self.x][self.y + 2] == "m" or bd.buff[self.x][self.y + 2] == "/" or bd.buff[self.x][self.y + 2] == "\\" or bd.buff[self.x][self.y + 2] == "M":
                count = count + 1
            if bd.buff[self.x + 1][self.y + 2] == " " or bd.buff[self.x + 1][self.y + 2] == "m" or bd.buff[self.x + 1][self.y + 2] == "/" or bd.buff[self.x + 1][self.y + 2] == "\\" or bd.buff[self.x + 1][self.y + 2] == "M":
                count = count + 1
            if count == 2:
                self.y = self.y + self.speed_y

    def killPlayer(self, mario, bd, x, y, enemies):
        mario.reduceLife(bd, x, y, enemies)

    def die(self, enemies, bd):
        self.is_alive = 0
        enemies.remove(self)
        