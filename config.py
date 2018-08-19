'''
This module contains all the configurations 
like symbols, constants, movements
'''

import os, time


#representations of various objects
_ground = "T"
_wall = "W"
_pipe = "O"
_block = "X"
_mario = "M"
_enemy = "E"
_empty = " "


#types of various objects
types = {
    _ground : "Ground",
    _wall : "Wall",
    _pipe : "Pipe",
    _block : "Block",
    _mario : "Mario",
    _enemy : "Enemy",
    _empty : "Unassigned"
}


#level properties
timelimit = [100, 100, 90, 80]

#key presses
RIGHT = 0
LEFT = 1
JUMP = 2
QUIT = 3


#inputs allowed
_inputs_allowed = {
    RIGHT : ['d'], 
    LEFT : ['a'],
    JUMP : ['w'],
    QUIT : ['q']
}


def get_key(key):
    for n in _inputs_allowed:
        for key in _inputs_allowed[n]:
            return n
    return -1


#Get a charcter from stdin
class Getch:

    def __init__(self):
        try:
            self.impl = GetchWindows()
        except ImportError:
            self.impl = GetchUnix()


    def __call__(self):
        return self.impl()


class GetchUnix:

    def __init__(self):
        import tty, sys

    def __call__(self):
        import sys
        import tty
        import termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

class GetchWindows:

    def __init__(self):
        import msvcrt


    def __call__(self):
        import msvcrt
        return msvcrt.getch()


getch = Getch()


class AlarmException(Exception):
    pass


def alarmHandler(signum, frame):
    raise AlarmException


def get_input(timeout=1):
    import signal
    signal.signal(signal.SIGALRM, alarmHandler)
    signal.alarm(timeout)
    try:
        text = getch()
        signal.alarm(0)
        return text
    except AlarmException:
        pass
    signal.signal(signal.SIGALRM, signal.SIG_IGN)
    return ''


# system colors
colors = {
    'Black'            : '\x1b[0;30m',
    'Blue'             : '\x1b[0;34m',
    'Green'            : '\x1b[0;32m',
    'Cyan'             : '\x1b[0;36m',
    'Red'              : '\x1b[0;31m',
    'Purple'           : '\x1b[0;35m',
    'Brown'            : '\x1b[0;33m',
    'Gray'             : '\x1b[0;37m',
    'Dark Gray'        : '\x1b[1;30m',
    'Light Blue'       : '\x1b[1;34m',
    'Light Green'      : '\x1b[1;32m',
    'Light Cyan'       : '\x1b[1;36m',
    'Light Red'        : '\x1b[1;31m',
    'Light Purple'     : '\x1b[1;35m',
    'Yellow'           : '\x1b[1;33m',
    'White'            : '\x1b[1;37m'
}


def getc(char):
    try:
        if char == _empty:
            return char
        elif char == _ground:
            color = 'Green'
        elif char == _wall:
            color = 'Brown'
        elif char == _pipe:
            color = 'Blue'
        elif char == _block:
            color = 'Dark Gray'
        elif char == _mario:
            color = 'Red'
        elif char == _enemy:
            color = 'Yellow'
        else:
            color = 'None'
        return colors[color] + char + '\x1b[0m'
    except:
        return char


def printc(char, color):
    try:
        return colors[color] + char + '\x1b[0m'
    except:
        return char


def print_screen(level, bd, mario, enemies, objects, scene):
    os.system('clear')
    bd.init_board(mario)
    for sc in scene:
        sc.draw(bd)
    for ob in objects:
        ob.draw(bd)
    mario.drawPlayer(bd)
    for en in enemies:
        en.drawEnemy(bd)
    # print ("SCORE: ", mario.score)
    # print ("TIME LEFT: ", timelimit[level] - mario.play_time(), end=' ')
    # print ("\t\t\tLIVES: ", mario.lives)
    bd.render(mario, enemies)
    #time.sleep(0.05)