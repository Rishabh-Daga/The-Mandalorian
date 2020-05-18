import sys

score = 0
bs = 0
lives = 10
shield_available = False
shield_active = False
dragon_lives = 10
gravity = True
mag = True
acc = 0
time = 75

def collision(matrix, x, y, l1, l2, flag):
    global bs, score, lives, shield_active, shield_available, dragon_lives, mag
    # print(x)
    # print(y)
    # print(l1)
    # print(l2)
    # print('inside')
    # print(matrix[x][y]._type+'hello')
    if matrix[x][y]._type == 'C':
        if flag == 'm':
            score = score + 1
    elif matrix[x][y]._type == 'S':
        if flag == 'm':
            if(bs<3):
                bs = bs + 1
    elif matrix[x][y]._type == 'M':
        if flag == 'b':
            # print('tty')
            if shield_active:
                shield_active = False
                shield_available = False
                return
            else:
                if(lives > 0):
                    lives = lives - 1
                    # print("**********", lives, "*****")
                    return
    elif matrix[x][y]._type == 'P':
        if flag == 'b':
            mag = False
            score = score + 40
    elif matrix[x][y]._type == 'D':
        # print('hello')
        if flag == 'b':
            dragon_lives = dragon_lives - 1
            if(dragon_lives > 0):
                # print('wtf')
                return
            else:
                for i in range(37):
                    for j in range(444, 500):
                        matrix[i][j]._char = ' '
                        matrix[i][j]._type = 'B'
                        matrix[i][j]._xco = 0
                        matrix[i][j]._yco = 0
                        matrix[i][j]._len1 = 0
                        matrix[i][j]._len2 = 0
                return
    #     else:
    #         lives = lives - 1
    elif matrix[x][y]._type == 'N':
        if flag == 'm':
            if shield_active == False:
                lives = lives - 1
            else:
                shield_active = False
                shield_available = False
        else:
            score = score + 25
    elif matrix[matrix[x][y]._xco][matrix[x][y]._yco]._type == 'U':
        if flag == 'm':
            # print('here')
            if shield_active == False:
                lives = lives - 1
            else:
                shield_active = False
                shield_available = False
    # f=0
    # if matrix[x][y]._type == 'D':
        # f=1
    for i in range(l1):
        for j in range(l2):
            matrix[i+x][j+y]._char = ' '
            matrix[i+x][j+y]._type = 'B'
            matrix[i+x][j+y]._xco = 0
            matrix[i+x][j+y]._yco = 0