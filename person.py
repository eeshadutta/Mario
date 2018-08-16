from __future__ import print_function
import signal,copy,sys,time,os
from random import randint
import config
import board


class Person:
    def __init__(self, x, y, is_alive=1):
        self.ini_x = x
        self.ini_y = y
        self.x = x
        self.y = y
        self.is_alive = is_alive


class Player(Person):
    def __init__(self, x, y, is_alive):
        Person.__init__(self, x, y, is_alive)
        Person.lives = 3

    def drawPlayer(self):
        for i in range(2):
            for j in range(2):
                board.buff[self.x + i][self.y + j] = "m"

    def updatePlayer(self, x_or, y_or):
        for i in range(2):
            for j in range(2):
                board.buff[x_or + i][y_or + j] = " "
        for i in range(2):
            for j in range(2):
                board.buff[self.x + i][self.y + j] = "m"

    def moveLeft(self):
        self.y = self.y - 1

    def moveRight(self):
        self.y = self.y + 1

    def jump(self, bd, prev):
        speed_x = 4 
        speed_y = 0
        if (prev == 0):
            speed_y = 1
        elif (prev == 1):
            speed_y = -1
            
        self.x = self.x - speed_x
        self.y = self.y + speed_y
        self.updatePlayer(self.x + speed_x, self.y - speed_y)
        os.system('clear')
        bd.render()
        
        while (self.x < self.ini_x):
            speed_x = speed_x - 1
            self.x = self.x - speed_x
            self.y = self.y + speed_y
            self.updatePlayer(self.x + speed_x, self.y - speed_y)
            os.system('clear')
            bd.render()
            time.sleep(.05)