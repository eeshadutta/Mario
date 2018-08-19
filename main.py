from __future__ import print_function
import time, signal, sys, copy, datetime, os, random
import config
import board
import person
import obstacle


def make_scene(scene, bd, mario):
    for i in range(1, 65):
        x = random.randint(3, 10)
        cl = obstacle.Clouds(x, i*15, 3, 4)
        scene.append(cl)

    for i in range(1, 25):
        size = random.randint(1, 3)
        if size == 1:
            x = bd.height - 8
            h = obstacle.Hills(x, i*40, 4, 8, 1)
        else:
            x = bd.height - 10
            h = obstacle.Hills(x, i*40, 6, 12, 2)
        scene.append(h)


def make_objects(objects, bd, mario, objects_y):
    br = obstacle.Bricks(bd.height-12, 18, 2, 8)
    objects.append(br)
    br = obstacle.Bricks(bd.height-18, 30, 2, 6)
    objects.append(br)
    br = obstacle.Bricks(bd.height-12, 40, 2, 8)
    objects.append(br)

    p = obstacle.Pipe(bd.height-11, 70, 7, 6)
    objects.append(p)
    p = obstacle.Pipe(bd.height-14, 82, 10, 10)
    objects.append(p)
    p = obstacle.Pipe(bd.height-22, 98, 18, 8)
    objects.append(p)

    h = obstacle.Obstacle(bd.height-4, 140, 3, 5)
    objects.append(h)
    
    br = obstacle.Bricks(bd.height-12, 160, 2, 6)
    objects.append(br)
    br = obstacle.Bricks(bd.height-17, 172, 2, 4)
    objects.append(br)
    br = obstacle.Bricks(bd.height-6, 200, 2, 10)
    objects.append(br)
    br = obstacle.Bricks(bd.height-8, 202, 2, 8)
    objects.append(br)
    br = obstacle.Bricks(bd.height-10, 204, 2, 6)
    objects.append(br)
    br = obstacle.Bricks(bd.height-12, 206, 2, 4)
    objects.append(br)
    br = obstacle.Bricks(bd.height-14, 208, 2, 2)
    objects.append(br)
    h = obstacle.Obstacle(bd.height-4, 210, 3, 5)
    objects.append(h)
    br = obstacle.Bricks(bd.height-14, 215, 2, 2)
    objects.append(br)
    br = obstacle.Bricks(bd.height-12, 215, 2, 4)
    objects.append(br)
    br = obstacle.Bricks(bd.height-10, 215, 2, 6)
    objects.append(br)
    br = obstacle.Bricks(bd.height-8, 215, 2, 8)
    objects.append(br)
    br = obstacle.Bricks(bd.height-6, 215, 2, 10)
    objects.append(br)

    br = obstacle.Bricks(bd.height-14, 240, 2, 6)
    objects.append(br)
    br = obstacle.Bricks(bd.height-14, 258, 2, 6)
    objects.append(br)
    br = obstacle.Bricks(bd.height-14, 276, 2, 8)
    objects.append(br)

    p = obstacle.Pipe(bd.height-11, 290, 7, 8)
    objects.append(p)
    p = obstacle.Pipe(bd.height-11, 303, 7, 8)
    objects.append(p)
    p = obstacle.Pipe(bd.height-11, 316, 7, 8)
    objects.append(p)


    br = obstacle.Bricks(bd.height-6, 330, 2, 20)
    objects.append(br)
    br = obstacle.Bricks(bd.height-8, 332, 2, 18)
    objects.append(br)
    br = obstacle.Bricks(bd.height-10, 334, 2, 16)
    objects.append(br)
    br = obstacle.Bricks(bd.height-12, 336, 2, 14)
    objects.append(br)
    br = obstacle.Bricks(bd.height-14, 338, 2, 12)
    objects.append(br)
    br = obstacle.Bricks(bd.height-16, 340, 2, 10)
    objects.append(br)
    br = obstacle.Bricks(bd.height-18, 342, 2, 8)
    objects.append(br)
    br = obstacle.Bricks(bd.height-20, 344, 2, 6)
    objects.append(br)
    br = obstacle.Bricks(bd.height-22, 346, 2, 4)
    objects.append(br)
    br = obstacle.Bricks(bd.height-24, 348, 2, 2)
    objects.append(br)

    f = obstacle.Pipe(bd.height-28, 357, 24, 1)
    objects.append(f)


def spawn(enemies, num_enemies, bd, mario, objects_y):
    while (num_enemies > 0):
        x = mario.x
        y = random.randint(bd.left + (bd.width / 2), bd.right - 3)
        if y not in objects_y:
            en = person.Enemy(x, y, 1, 1, bd)
            enemies.append(en)
            num_enemies -= 1
    

def main():
    
    height, width, buff_width = (40, 80, 1000)
    level = 1
    bd = board.Board(height, width, buff_width, level)        
    mario = person.Player((height-6), 7, 1, 3, bd, level)
    prev = 0
    enemies = []
    objects = []
    objects_y = []
    scene = []
    make_scene(scene, bd, mario)
    make_objects(objects, bd, mario, objects_y)
    spawn(enemies, 2, bd, mario, objects_y)
    config.print_screen(level, bd, mario, enemies, objects, scene)
    prev_round = datetime.datetime.now()

    
    while (True):
        cur_round = datetime.datetime.now()
        if (cur_round - prev_round) >= datetime.timedelta(seconds=0.1):
            for en in enemies:
                en.moveEnemy(mario, bd)
                if (bd.buff[mario.x][mario.y] == "e") and (bd.buff[mario.x + 1][mario.y] == "e"):
                    en.killPlayer(mario, bd, mario.x, mario.y, enemies)
                elif (bd.buff[mario.x][mario.y + 1] == "e") and (bd.buff[mario.x + 1][mario.y + 1] == "e"):
                    en.killPlayer(mario, bd, mario.x, mario.y+1, enemies)
            if len(enemies) < 2:
                spawn(enemies, 1, bd, mario, objects_y)
            config.print_screen(level, bd, mario, enemies, objects, scene)
            prev_round = cur_round


        inp = config.get_input()
        if inp == "q":
            sys.exit(0)                
        if (inp == "d"):
            mario.moveRight(bd)
            prev = 1
        elif (inp == "a"):
            mario.moveLeft(bd)
            prev = -1
        elif (inp == "w"):
            mario.jump(bd, prev, enemies, objects, scene)
            prev = 0
        elif (inp == "q"):
            sys.exit(0)

        config.print_screen(level, bd, mario, enemies, objects, scene)

        
main()