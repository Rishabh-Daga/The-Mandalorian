import os
import numpy
from colorama import Fore, Back, Style, init
from board import Board
import config

init()

class Mando:
    def __init__(self):
        self.__mando = []
        self.__xpos = 32
        self.__ypos = 5
        with open('./objects/mandonew.txt') as man:
            for line in man:
                self.__mando.append(line.strip('\n'))

    @property
    def xpos(self):
        return self.__xpos
    
    @xpos.setter
    def xpos(self, a):
        self.__xpos = a
    @property
    def ypos(self):
        return self.__ypos
    
    @ypos.setter
    def ypos(self, a):
        self.__ypos = a
    def loadMando(self, matrix, flag, cnt):
        # self.__mando = []
        # print(len(self.__mando))
        self.checkCollision(matrix)
        if self.__xpos > 0 and self.__ypos > 0:
            for i in range(len(self.__mando)):
                for j in range(len(self.__mando[i])):
                    if flag == 'r' and j == 0 and self.__ypos < 500:
                        if matrix[i+self.__xpos][j+self.__ypos-1]._type == 'P':
                            matrix[i+self.__xpos][j+self.__ypos-1]._char = 'm'
                        else:
                            matrix[i+self.__xpos][j+self.__ypos-1]._char = ' '
                            matrix[i+self.__xpos][j+self.__ypos-1]._type = 'B'
                    elif flag == 'l' and j == len(self.__mando[i])-1 and self.__ypos > 0:
                        if matrix[i+self.__xpos][j+self.__ypos+1]._type == 'P':
                            matrix[i+self.__xpos][j+self.__ypos+1]._char = 'm'
                        else:
                            matrix[i+self.__xpos][j+self.__ypos+1]._char = ' '
                            matrix[i+self.__xpos][j+self.__ypos+1]._type = 'B'
                    elif flag == 'u' and i == len(self.__mando)-1 and self.__xpos > 0:
                        if matrix[i+self.__xpos+1][j+self.__ypos]._type == 'P':
                            matrix[i+self.__xpos+1][j+self.__ypos]._char = 'm'
                        else:
                            matrix[i+self.__xpos+1][j+self.__ypos]._char = ' '
                            matrix[i+self.__xpos+1][j+self.__ypos]._type = 'B'
                    elif flag == 'd' and i == 0 and self.__xpos < 33:
                        if matrix[i+self.__xpos-1][j+self.__ypos]._type == 'P':
                            matrix[i+self.__xpos-1][j+self.__ypos]._char == 'm'
                        else:
                            matrix[i+self.__xpos-1][j+self.__ypos]._char = ' '
                            matrix[i+self.__xpos-1][j+self.__ypos]._type = 'B'
                    if matrix[i+self.__xpos][j+self.__ypos]._type != 'P':
                        matrix[i+self.__xpos][j+self.__ypos]._char = self.__mando[i][j]
                        matrix[i+self.__xpos][j+self.__ypos]._type = 'M'
    
    def gravity(self, matrix, cnt, acc):
        self.checkCollision(matrix)
        if self.__xpos<32 and self.__xpos > 0 and self.__ypos > 0:
            for i in range(max(1,min(acc, 32-self.__xpos-1))):
                self.__xpos = self.__xpos + 1
                self.loadMando(matrix, 'd', cnt)

    def checkCollision(self, matrix):

        for i in range(len(self.__mando)):
            for j in range(len(self.__mando[i])):
                
                if matrix[i+self.__xpos][j+self.__ypos+1]._type == 'C':
                    # #print('hello1')
                    config.collision(matrix, matrix[i+self.__xpos][j+self.__ypos+1]._xco, matrix[i+self.__xpos][j+self.__ypos+1]._yco, matrix[i+self.__xpos][j+self.__ypos+1]._len1, matrix[i+self.__xpos][j+self.__ypos+1]._len2, 'm')
                elif matrix[i+self.__xpos][j+self.__ypos-1]._type == 'C':
                    # #print('hello1')
                    config.collision(matrix, matrix[i+self.__xpos][j+self.__ypos-1]._xco, matrix[i+self.__xpos][j+self.__ypos-1]._yco, matrix[i+self.__xpos][j+self.__ypos-1]._len1, matrix[i+self.__xpos][j+self.__ypos-1]._len2, 'm')
                elif matrix[i+self.__xpos+1][j+self.__ypos]._type == 'C':
                    # #print('hello1')
                    config.collision(matrix, matrix[i+self.__xpos+1][j+self.__ypos]._xco, matrix[i+self.__xpos+1][j+self.__ypos]._yco, matrix[i+self.__xpos+1][j+self.__ypos]._len1, matrix[i+self.__xpos+1][j+self.__ypos]._len2, 'm')
                elif matrix[i+self.__xpos-1][j+self.__ypos]._type == 'C':
                    # #print('hello1')
                    config.collision(matrix, matrix[i+self.__xpos-1][j+self.__ypos]._xco, matrix[i+self.__xpos-1][j+self.__ypos]._yco, matrix[i+self.__xpos-1][j+self.__ypos]._len1, matrix[i+self.__xpos-1][j+self.__ypos]._len2, 'm')
                elif matrix[i+self.__xpos][j+self.__ypos+1]._type == 'S':
                    #print('hello1')
                    config.collision(matrix, matrix[i+self.__xpos][j+self.__ypos+1]._xco, matrix[i+self.__xpos][j+self.__ypos+1]._yco, matrix[i+self.__xpos][j+self.__ypos+1]._len1, matrix[i+self.__xpos][j+self.__ypos+1]._len2, 'm')
                elif matrix[i+self.__xpos][j+self.__ypos-1]._type == 'S':
                    #print('hello1')
                    config.collision(matrix, matrix[i+self.__xpos][j+self.__ypos-1]._xco, matrix[i+self.__xpos][j+self.__ypos-1]._yco, matrix[i+self.__xpos][j+self.__ypos-1]._len1, matrix[i+self.__xpos][j+self.__ypos-1]._len2, 'm')
                elif matrix[i+self.__xpos+1][j+self.__ypos]._type == 'S':
                    #print('hello1')
                    config.collision(matrix, matrix[i+self.__xpos+1][j+self.__ypos]._xco, matrix[i+self.__xpos+1][j+self.__ypos]._yco, matrix[i+self.__xpos+1][j+self.__ypos]._len1, matrix[i+self.__xpos+1][j+self.__ypos]._len2, 'm')
                elif matrix[i+self.__xpos-1][j+self.__ypos]._type == 'S':
                    #print('hello1')
                    config.collision(matrix, matrix[i+self.__xpos-1][j+self.__ypos]._xco, matrix[i+self.__xpos-1][j+self.__ypos]._yco, matrix[i+self.__xpos-1][j+self.__ypos]._len1, matrix[i+self.__xpos-1][j+self.__ypos]._len2, 'm')
                elif matrix[i+self.__xpos][j+self.__ypos+1]._type == 'N':
                    #print('hello1')
                    config.collision(matrix, matrix[i+self.__xpos][j+self.__ypos+1]._xco, matrix[i+self.__xpos][j+self.__ypos+1]._yco, matrix[i+self.__xpos][j+self.__ypos+1]._len1, matrix[i+self.__xpos][j+self.__ypos+1]._len2, 'm')
                elif matrix[i+self.__xpos][j+self.__ypos-1]._type == 'N':
                    #print('hello1')
                    config.collision(matrix, matrix[i+self.__xpos][j+self.__ypos-1]._xco, matrix[i+self.__xpos][j+self.__ypos-1]._yco, matrix[i+self.__xpos][j+self.__ypos-1]._len1, matrix[i+self.__xpos][j+self.__ypos-1]._len2, 'm')
                elif matrix[i+self.__xpos+1][j+self.__ypos]._type == 'N':
                    #print('hello1')
                    config.collision(matrix, matrix[i+self.__xpos+1][j+self.__ypos]._xco, matrix[i+self.__xpos+1][j+self.__ypos]._yco, matrix[i+self.__xpos+1][j+self.__ypos]._len1, matrix[i+self.__xpos+1][j+self.__ypos]._len2, 'm')
                elif matrix[i+self.__xpos-1][j+self.__ypos]._type == 'N':
                    #print('hello1')
                    config.collision(matrix, matrix[i+self.__xpos-1][j+self.__ypos]._xco, matrix[i+self.__xpos-1][j+self.__ypos]._yco, matrix[i+self.__xpos-1][j+self.__ypos]._len1, matrix[i+self.__xpos-1][j+self.__ypos]._len2, 'm')
                # elif matrix[i+self.__xpos][j+self.__ypos+1]._type == 'U':
                #     #print('hello1')
                #     config.collision(matrix, matrix[i+self.__xpos][j+self.__ypos+1]._xco, matrix[i+self.__xpos][j+self.__ypos+1]._yco, matrix[i+self.__xpos][j+self.__ypos+1]._len1, matrix[i+self.__xpos][j+self.__ypos+1]._len2, 'm')
                # elif matrix[i+self.__xpos][j+self.__ypos-1]._type == 'U':
                #     #print('hello1')
                #     config.collision(matrix, matrix[i+self.__xpos][j+self.__ypos-1]._xco, matrix[i+self.__xpos][j+self.__ypos-1]._yco, matrix[i+self.__xpos][j+self.__ypos-1]._len1, matrix[i+self.__xpos][j+self.__ypos-1]._len2, 'm')
                # elif matrix[i+self.__xpos+1][j+self.__ypos]._type == 'U':
                #     #print('hello1')
                #     config.collision(matrix, matrix[i+self.__xpos+1][j+self.__ypos]._xco, matrix[i+self.__xpos+1][j+self.__ypos]._yco, matrix[i+self.__xpos+1][j+self.__ypos]._len1, matrix[i+self.__xpos+1][j+self.__ypos]._len2, 'm')
                # elif matrix[i+self.__xpos-1][j+self.__ypos]._type == 'U':
                #     #print('hello1')
                #     config.collision(matrix, matrix[i+self.__xpos-1][j+self.__ypos]._xco, matrix[i+self.__xpos-1][j+self.__ypos]._yco, matrix[i+self.__xpos-1][j+self.__ypos]._len1, matrix[i+self.__xpos-1][j+self.__ypos]._len2, 'm')