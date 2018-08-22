'''
This module contains all the configurations
like symbols, constants, movements
'''

import os


# representations of various objects
_ground = "^"
_pipe = "-"
_block = "X"
_mario = "m"
_enemy = "e"
_empty = " "

# level properties
timelimit = [100, 100, 90, 80]


# Get a charcter from stdin
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
        import tty
        import sys

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


def get_input_jump(timeout=0.1):
    import signal
    signal.signal(signal.SIGALRM, alarmHandler)
    signal.setitimer(signal.ITIMER_REAL, timeout, timeout)
    try:
        text = getch()
        signal.alarm(0)
        return text
    except AlarmException:
        pass
    signal.signal(signal.SIGALRM, signal.SIG_IGN)
    return ''


def print_screen(level, bd, mario, enemies, objects, scene, coins):
    os.system('clear')
    bd.init_board(mario)
    for sc in scene:
        sc.draw(bd)
    for c in coins:
        c.draw(bd)
    for ob in objects:
        ob.draw(bd)
    mario.drawPlayer(bd)
    for en in enemies:
        en.drawEnemy(bd)
    bd.render(mario, enemies)
