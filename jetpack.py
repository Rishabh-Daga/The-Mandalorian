import os
import time
import signal
import numpy as np
from board import Board
from screen import Screen, Obstacle
import config
from mando import Mando
from alarmexception import AlarmException
from getch import _getChUnix as getChar
from coins import Coin
from speed_up import Speed
from bullet import Bullet
from beam import Beam
from magnet import Magnet
from dragon import Dragon, dragonBullet
import random

def alarmhandler(signum, frame):
		''' input method '''
		raise AlarmException

def user_input(timeout=0.04):
    ''' input method '''
    signal.signal(signal.SIGALRM, alarmhandler)
    signal.setitimer(signal.ITIMER_REAL, timeout)
    
    try:
        text = getChar()()
        signal.alarm(0)
        return text
    except AlarmException:
        pass
    signal.signal(signal.SIGALRM, signal.SIG_IGN)
    return ''

os.system('clear')
cnt = 0
screen = Screen()
board = Board(40, 500)
board.createBoard()
screen.createSky(board.matrix, board.columns)
screen.createGround(board.matrix, board.columns)
l1 = 0
beam = Beam()
beam.loadObstacle('beam')
beamhead = Beam()
beamhead.loadObstacle('beam_head')
for j in range(12):
    f = random.randint(0,2)
    l = random.randint(6,10)
    m1 = random.randint(2+l, 30-l)
    m2 = random.randint(30+l1, 40+l1+10)
    for i in range(l):
        if f == 0:
            if i == 0 or i == l-1:            
                beamhead.place(board.matrix, m1, m2, 0, i*2, l, 2*l)
            else:
                beam.place(board.matrix, m1, m2, 0, i*2, l, 2*l)
        elif f == 1:
            if i == 0 or i == l-1:
                beamhead.place(board.matrix, m1, m2, i, i, l, l+1)
            else:
                beam.place(board.matrix, m1, m2, i, i, l, l+1)
        elif f == 2:
            if i == 0 or i == l-1:
                beamhead.place(board.matrix, m1, m2, i, 0, l, 2)
            else:
                beam.place(board.matrix, m1, m2, i, 0, l, 2)
        elif f == 3:
            if i == 0 or i == l-1:
                beamhead.place(board.matrix, m1, m2, i, -i, l, l+1)
            else:
                beam.place(board.matrix, m1, m2, i, -i, l, l+1)
    l1 = l+l1+20
speed = Speed()
speed.loadObstacle('speed_up')
l1 = 0
for i in range(5):
    m1 = random.randint(1, 33)
    m2 = random.randint(20+l1, 80+l1+10)
    speed.place(board.matrix, m1, m2)
    l1 = 5 + l1 +50
coin = Coin()
coin.loadObstacle('coin')
for i in range(7):
    c1 = random.randint(2,5)
    c2 = random.randint(3,8)
    x = random.randint(1,33)
    y = random.randint(30+i*20, 240+i*20)
    for j in range(c1):
        for k in range(c2):
            coin.place(board.matrix, x+j, y+k)
magnet = Magnet()
magnet.loadObstacle('magnet')
x1 = 20
x2 = 200
magnet.place(board.matrix, x1, x2)
mando = Mando()
mando.loadMando(board.matrix, 'n', cnt)
board.printBoard(cnt, config.dragon_lives)
dragon = Dragon()
dragon.loadObstacle('dragon')
dragon.place(board.matrix, 20, 445)
st = time.time()
prev_gravity_time = time.time()
dBtime = time.time()
shield_time = time.time()
gtime = time.time()
flag = 'G'
bullets = []
dragon_bullets = []
while True:
    p = user_input()
    if config.time <= 0:
        flag = 'T'
        break
    if config.dragon_lives <= 0:
        while mando.xpos < 32:
            time.sleep(0.01)
            mando.xpos = mando.xpos + 1
            mando.loadMando(board.matrix, 'd', cnt)
            board.printBoard(cnt, config.dragon_lives)
        while mando.ypos < cnt+120:
            time.sleep(0.01)
            mando.ypos = mando.ypos + 1
            mando.loadMando(board.matrix, 'r', cnt)
            board.printBoard(cnt, config.dragon_lives)
        os.system('clear')
        flag = 'W'
        break
    if p == 'q':
        break
    elif p == 'd':
        if mando.ypos < cnt + 120 and mando.ypos + 1 != x2 and mando.ypos < 410:
            mando.ypos = mando.ypos + 1
            mando.loadMando(board.matrix, 'r', cnt)
        board.printBoard(cnt, config.dragon_lives)
    elif p == 'a':
        if mando.ypos > cnt + 1:
            mando.ypos = mando.ypos - 1
            mando.loadMando(board.matrix, 'l', cnt)
        board.printBoard(cnt, config.dragon_lives)
    elif p == 'w':
        config.acc = 0
        if mando.xpos > 1 and config.gravity:
            mando.xpos = mando.xpos - 1
            mando.loadMando(board.matrix, 'u', cnt)
        if mando.xpos < dragon.xpos and cnt+130 > 400 and ~(mando.xpos > x1-20 and mando.xpos < x1+20 and mando.ypos < x2+20 and mando.ypos > x2-20 and x2 > cnt):
            dragon.moveUp(board.matrix, dragon.xpos-1, dragon.ypos)
            dragon.xpos = dragon.xpos - 1
        board.printBoard(cnt, config.dragon_lives)
    elif p == 's':
        if mando.xpos < 32 and config.gravity:
            mando.xpos = mando.xpos + 1
            mando.loadMando(board.matrix, 'd', cnt)
        if cnt+130 > 400 and dragon.xpos < 20 and ~(mando.xpos > x1-20 and mando.xpos < x1+20 and mando.ypos < x2+20 and mando.ypos > x2-20 and x2 > cnt):
            print(mando.xpos)
            dragon.moveDown(board.matrix, dragon.xpos+1, dragon.ypos)
            dragon.xpos = dragon.xpos + 1
        board.printBoard(cnt, config.dragon_lives)
    elif p == 'f':
        bullet = Bullet(mando.xpos, mando.ypos + 6)
        bullets.append(bullet)
    elif p == ' ':
        if config.shield_available and config.shield_active == False:
            config.shield_active = True
            shield_time = time.time()
    if time.time() - shield_time > 5:
        if config.shield_active == False and config.shield_available == False:
            config.shield_available = True
            shield_time = time.time()
    if time.time() - shield_time > 10:
        if config.shield_active:
            config.shield_available = False
            config.shield_active = False
            shield_time = time.time()
    if time.time() - dBtime > 0.5 and cnt + 130 > 450:
        if config.dragon_lives > 0:
            dBtime = time.time()
            dBullet = dragonBullet(mando.xpos, dragon.ypos - 2, board.matrix)
            dragon_bullets.append(dBullet)
    if time.time() - prev_gravity_time > 0.15:
        if config.gravity == True:
            config.acc = config.acc + 0.3
            # print(mando.xpos)
            if mando.xpos == 32:
                config.acc = 0  
            # print(int(config.acc))
            mando.gravity(board.matrix, cnt, int(config.acc))
            if cnt+130 > 400 and dragon.xpos < 20 and ~(mando.xpos > x1-20 and mando.xpos < x1+20 and mando.ypos < x2+20 and mando.ypos > x2-20 and x2 > cnt):
                dragon.moveDown(board.matrix, dragon.xpos+1, dragon.ypos)
                dragon.xpos = dragon.xpos + 1
            prev_gravity_time = time.time()
        else:
            config.acc = 0
    if time.time() - gtime > 1:
        config.time -= 1
        gtime = time.time()
    end = time.time()
    diff = end -st
    if(diff> 0.15-config.bs*0.03):
        for i in bullets:
            i.move(board.matrix, cnt + 125)
        for i in dragon_bullets:
            i.move(board.matrix, cnt)
        if mando.xpos > x1-20 and mando.xpos < x1+20 and mando.ypos < x2+20 and mando.ypos > x2-20 and x2 > cnt and config.mag:
            config.gravity = False
            if mando.xpos > x1:
                if mando.xpos > x1 + 1:
                    mando.xpos = mando.xpos - 1
                    mando.loadMando(board.matrix, 'u', cnt)
            elif mando.xpos < x1:
                if mando.xpos+5 < x1:
                    mando.xpos = mando.xpos + 1
                    mando.loadMando(board.matrix, 'd', cnt)
            if mando.ypos < x2:
                if mando.xpos > x1:
                    t = x2 - 1
                else:
                    t = x2 + 1
                if mando.ypos+5 < t:
                    mando.ypos = mando.ypos + 1
                    mando.ypos
                    mando.loadMando(board.matrix, 'r', cnt)
            elif mando.ypos > x2:
                if mando.xpos > x1:
                    t = x2 - 1
                else:
                    t = x2 + 1
                if mando.ypos > t:
                    mando.ypos = mando.ypos - 1
                    mando.ypos
                    mando.loadMando(board.matrix, 'l', cnt)
        else:
            config.gravity = True
        st = end
        if cnt + 130 < 500 and ~(mando.xpos > x1-20 and mando.xpos < x1+20 and mando.ypos < x2+20 and mando.ypos > x2-20 and x2 > cnt):
            cnt = cnt+1
            if mando.ypos + 1 != x2-1 or mando.ypos != x2+1:
                mando.ypos = mando.ypos + 1
            mando.loadMando(board.matrix, 'r', cnt)
        # if cnt + 130 > 100:
        #     dragon.place(board.matrix, 20, 130)
        # if(cnt == mando.ypos):
        # if mando.ypos < 260:
        # if(130+cnt<300):
        if(config.lives <= 0):
            os.system('clear')
            flag = 'L'
            break
        # print(config.dragon_lives)
        # print(config.gravity)
        board.printBoard(cnt, config.dragon_lives)
        # if config.dragon_lives == 0:
        #     # t1.join()
        #     break
# t1.join()
# board.printBoard(cnt, config.dragon_lives)
if flag == 'W':
    with open ('./objects/win.txt') as file:
        for line in file:
            print(line, end = '')
elif flag == 'G':
    print('YOU QUIT')
elif flag == 'L':
    with open ('./objects/lose.txt') as file:
        for line in file:
            print(line, end = '')
    print('GAME OVER')
elif flag == 'T':
    with open ('./objects/time.txt') as file:
        for line in file:
            print(line, end = '')
    
