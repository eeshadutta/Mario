from __future__ import print_function
import time, signal, sys, copy, datetime, os
import config
import board
import person


def main():
    
    height, width = (30, 80)
    level = 1
    bd = board.Board(height, width, level)
    mario = person.Player(24, 7, 1)
    mario.drawPlayer()
    os.system('clear')
    bd.render()
    prev = -1
    
    while (True):
        
        inp = config.getch()
        x = mario.x
        y = mario.y
        if (inp == 'd'):
            mario.moveRight()
            prev = 0
        elif (inp == 'a'):
            mario.moveLeft()
            prev = 1
        elif (inp == 'w'):
            mario.jump(bd, prev)
        elif (inp == 'q'):
            sys.exit(0)
        mario.updatePlayer(x, y)
        os.system('clear')
        bd.render()

main()