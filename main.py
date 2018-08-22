from __future__ import print_function
import time, signal, sys, copy, datetime, os, random, subprocess
import config
import board
import person
import obstacle


def make_scene(scene, bd, mario):
    for i in range(1, 25):
        x = random.randint(3, 10)
        cl = obstacle.Clouds(x, i*15, 3, 4)
        scene.append(cl)

    for i in range(1, 8):
        size = random.randint(1, 3)
        if size == 1:
            x = bd._height - 8
            h = obstacle.Hills(x, i*40, 4, 8, 1)
        else:
            x = bd._height - 10
            h = obstacle.Hills(x, i*50, 6, 12, 2)
        scene.append(h)


def make_objects(objects, bd, mario, objects_y):
    br = obstacle.Bricks(bd._height-12, 18, 2, 8)
    objects.append(br)
    br = obstacle.Bricks(bd._height-18, 30, 2, 6)
    objects.append(br)
    br = obstacle.Bricks(bd._height-12, 40, 2, 8)
    objects.append(br)

    p = obstacle.Pipe(bd._height-11, 70, 7, 6)
    objects.append(p)
    p = obstacle.Pipe(bd._height-14, 82, 10, 10)
    objects.append(p)
    p = obstacle.Pipe(bd._height-22, 98, 18, 8)
    objects.append(p)

    h = obstacle.Obstacle(bd._height-4, 140, 3, 5)
    objects.append(h)
    
    br = obstacle.Bricks(bd._height-12, 160, 2, 6)
    objects.append(br)
    br = obstacle.Bricks(bd._height-17, 172, 2, 4)
    objects.append(br)
    br = obstacle.Bricks(bd._height-6, 200, 2, 10)
    objects.append(br)
    br = obstacle.Bricks(bd._height-8, 202, 2, 8)
    objects.append(br)
    br = obstacle.Bricks(bd._height-10, 204, 2, 6)
    objects.append(br)
    br = obstacle.Bricks(bd._height-12, 206, 2, 4)
    objects.append(br)
    br = obstacle.Bricks(bd._height-14, 208, 2, 2)
    objects.append(br)
    h = obstacle.Obstacle(bd._height-4, 210, 3, 5)
    objects.append(h)
    br = obstacle.Bricks(bd._height-14, 215, 2, 2)
    objects.append(br)
    br = obstacle.Bricks(bd._height-12, 215, 2, 4)
    objects.append(br)
    br = obstacle.Bricks(bd._height-10, 215, 2, 6)
    objects.append(br)
    br = obstacle.Bricks(bd._height-8, 215, 2, 8)
    objects.append(br)
    br = obstacle.Bricks(bd._height-6, 215, 2, 10)
    objects.append(br)

    br = obstacle.Bricks(bd._height-14, 240, 2, 6)
    objects.append(br)
    br = obstacle.Bricks(bd._height-14, 258, 2, 6)
    objects.append(br)
    br = obstacle.Bricks(bd._height-14, 276, 2, 8)
    objects.append(br)

    p = obstacle.Pipe(bd._height-11, 290, 7, 8)
    objects.append(p)
    p = obstacle.Pipe(bd._height-11, 303, 7, 8)
    objects.append(p)
    p = obstacle.Pipe(bd._height-11, 316, 7, 8)
    objects.append(p)

    br = obstacle.Bricks(bd._height-6, 330, 2, 20)
    objects.append(br)
    br = obstacle.Bricks(bd._height-8, 332, 2, 18)
    objects.append(br)
    br = obstacle.Bricks(bd._height-10, 334, 2, 16)
    objects.append(br)
    br = obstacle.Bricks(bd._height-12, 336, 2, 14)
    objects.append(br)
    br = obstacle.Bricks(bd._height-14, 338, 2, 12)
    objects.append(br)
    br = obstacle.Bricks(bd._height-16, 340, 2, 10)
    objects.append(br)
    br = obstacle.Bricks(bd._height-18, 342, 2, 8)
    objects.append(br)
    br = obstacle.Bricks(bd._height-20, 344, 2, 6)
    objects.append(br)
    br = obstacle.Bricks(bd._height-22, 346, 2, 4)
    objects.append(br)
    br = obstacle.Bricks(bd._height-24, 348, 2, 2)
    objects.append(br)

    f = obstacle.Pipe(bd._height-28, 357, 24, 1)
    objects.append(f)


def put_coins(coins, bd):
    coin = obstacle.Coins(bd._height-19,32,1,1)
    coins.append(coin)
    coin = obstacle.Coins(bd._height-19,33,1,1)
    coins.append(coin)
    coin = obstacle.Coins(bd._height-20,54,1,1)
    coins.append(coin)
    coin = obstacle.Coins(bd._height-20,52,1,1)
    coins.append(coin)
    coin = obstacle.Coins(bd._height-7,79,1,1)
    coins.append(coin)
    coin = obstacle.Coins(bd._height-11,141,1,1)
    coins.append(coin)
    coin = obstacle.Coins(bd._height-11,142,1,1)
    coins.append(coin)
    coin = obstacle.Coins(bd._height-11,143,1,1)
    coins.append(coin)

    coin = obstacle.Coins(bd._height-23,173,1,1)
    coins.append(coin)
    coin = obstacle.Coins(bd._height-23,174,1,1)
    coins.append(coin)
    
    coin = obstacle.Coins(bd._height-18,211,1,1)
    coins.append(coin)
    coin = obstacle.Coins(bd._height-18,212,1,1)
    coins.append(coin)
    coin = obstacle.Coins(bd._height-18,213,1,1)
    coins.append(coin)

    coin = obstacle.Coins(bd._height-16,294,1,1)
    coins.append(coin)
    coin = obstacle.Coins(bd._height-16,307,1,1)
    coins.append(coin)
    coin = obstacle.Coins(bd._height-16,320,1,1)
    coins.append(coin)
    
    coin = obstacle.Coins(bd._height-7,330,1,1)
    coins.append(coin)
    coin = obstacle.Coins(bd._height-11,334,1,1)
    coins.append(coin)
    coin = obstacle.Coins(bd._height-15,338,1,1)
    coins.append(coin)
    coin = obstacle.Coins(bd._height-19,342,1,1)
    coins.append(coin)
    coin = obstacle.Coins(bd._height-23,346,1,1)
    coins.append(coin)


def spawn(enemies, num_enemies, bd, mario, objects_y):
    while (num_enemies > 0):
        x = mario.ini_x
        y = random.randint(bd._left + (bd._width / 2), bd._right - 3)
        if bd.buff[x][y] == " " and bd.buff[x][y+1] == " " and bd.buff[x+1][y] == " " and bd.buff[x+1][y+1] == " " and bd.buff[x+2][y] != " " and bd.buff[x+2][y+1] != " ":
            en = person.Enemy(x, y, 1, 1, bd)
            enemies.append(en)
            num_enemies -= 1


def main():
    
    height, width, buff_width = (40, 80, 400)
    level = 1
    bd = board.Board(height, width, buff_width, level)        
    mario = person.Player((height-6), 7, 1, 3, bd, level)
    enemies = []
    objects = []
    objects_y = []
    scene = []
    coins = []
    make_scene(scene, bd, mario)
    make_objects(objects, bd, mario, objects_y)
    put_coins(coins, bd)
    os.system('clear')
    bd.init_board(mario)
    for sc in scene:
        sc.draw(bd)
    for c in coins:
        c.draw(bd)
    for ob in objects:
        ob.draw(bd)
    mario.drawPlayer(bd)
    spawn(enemies, 2, bd, mario, objects_y)
    config.print_screen(level, bd, mario, enemies, objects, scene, coins)
    prev_round = datetime.datetime.now()
    
    while (True):
        cur_round = datetime.datetime.now()
        if (cur_round - prev_round) >= datetime.timedelta(seconds=0.1):
            for en in enemies:
                en.moveEnemy(mario, bd)
                if bd.buff[en.x+2][en.y] == " " and bd.buff[en.x+2][en.y] == " ":
                    enemies.remove(en)
                if (bd.buff[mario.x][mario.y] == "e") and (bd.buff[mario.x + 1][mario.y] == "e"):
                    en.killPlayer(mario, bd, mario.x, mario.y, enemies)
                elif (bd.buff[mario.x][mario.y + 1] == "e") and (bd.buff[mario.x + 1][mario.y + 1] == "e"):
                    en.killPlayer(mario, bd, mario.x, mario.y+1, enemies)
            if len(enemies) < 2:
                spawn(enemies, 1, bd, mario, objects_y)
            config.print_screen(level, bd, mario, enemies, objects, scene, coins)
            prev_round = cur_round

        inp = config.get_input()
        if inp == "q":
            mario.gameOver(bd, enemies, "GAME ENDED")
            if bd.buff[mario.x+2][mario.y+1] == " " and bd.buff[mario.x+2][mario.y+2] == " ":
                mario.jump(bd, -2, 1, enemies, objects, scene, coins)
            else:
                mario.moveRight(bd)
        elif (inp == "d"):
            if bd.buff[mario.x+2][mario.y+1] == " " and bd.buff[mario.x+2][mario.y+2] == " ":            
                mario.jump(bd, -2, 1, enemies, objects, scene, coins)
            else:
                mario.moveRight(bd)
        elif (inp == "a"):
            if bd.buff[mario.x+2][mario.y] == " " and bd.buff[mario.x+2][mario.y-1] == " ":
                mario.jump(bd, -2, -1, enemies, objects, scene, coins)
            else:
                mario.moveLeft(bd)
        elif (inp == "w"):
            subprocess.Popen(['aplay', './Sounds/mb_jump.wav'])
            os.system('clear')
            mario.jump(bd, 2, 0, enemies, objects, scene, coins)

        for i in range(2):
            for j in range(2):
                x = mario.x + i
                y = mario.y + j
                if bd.buff[x][y] == "$":
                    mario.earnCoins()
                    subprocess.Popen(['aplay', './Sounds/mb_coin.wav'])
                    os.system('clear')
                    for c in coins:
                        if c.x == x and c.y == y:
                            coins.remove(c)
                        if c.x == x and c.y + 1 == y:
                            coins.remove(c)
                    break

        if mario.y >= 355:
            mario.gameOver(bd, enemies, "CONGRATS!! YOU HAVE WON!!")
        if mario.play_time() == 100:
            mario.gameOver(bd, enemies, "TIME OVER. YOU LOST. BETTER LUCK NEXT TIME.")
        

        config.print_screen(level, bd, mario, enemies, objects, scene, coins)

        
main()