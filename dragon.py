import os
from colorama import Fore, Back, Style
from screen import Obstacle
from board import Cell
import config
import time

class dragonBullet:
    def __init__(self, x, y, matrix):
        self.__my_co = {
            x : [y, y - 1]
        }
        self.__my_print = {
            0 : [')', '(']
        }
        self.__living = 1
        l = 0
        m = 0
        for i in self.__my_co:
            m = 0
            for j in self.__my_co[i]:
                if matrix[i][j]._type != 'C' and matrix[i][j]._type != 'S':
                    matrix[i][j]._char = self.__my_print[l][m]
                m += 1
            l += 1
        return
    
    def move(self, matrix, last):
        if self.__living == 0:
            return
        for i in self.__my_co:
            for j in self.__my_co[i]:
                if matrix[i][j]._type != 'C' and matrix[i][j]._type != 'S':
                    matrix[i][j]._char = ' '
                    matrix[i][j]._type = 'B'
       
        new_co = {}
        for i in self.__my_co:
            new_co[i] = []
            for j in self.__my_co[i]:
                new_co[i].append(j - 4)
                for k in range(j-4, j + 1):
                    if matrix[i][k]._type == 'M':
                        config.collision(matrix, i, k, matrix[i][k]._len1, matrix[i][k]._len2, 'b')
                        self.__living = 0
                        print("########", k,"##########",i)
                        return

        for i in new_co:
            for j in new_co[i]:
                if j <= last:
                    self.__living = 0
                    return
         
        self.__my_co = new_co
        l = 0
        m = 0
        for i in self.__my_co:
            m = 0
            for j in self.__my_co[i]:
                if matrix[i][j]._type != 'C' and matrix[i][j]._type != 'S':
                    matrix[i][j]._char = self.__my_print[l][m]
                m += 1
            l += 1
        return
class Dragon(Cell, Obstacle):
    def __init__(self):
        Obstacle.__init__(self)
        Cell.__init__(self)
        self.__xpos = 0
        self.__ypos = 0
        # Bullet.__init__(self)

    @property
    def xpos(self):
        return self.__xpos
    
    @xpos.setter
    def xpos(self, a):
        self.__xpos = a
    @property
    def ypos(self):
        return self.__ypos

    def place(self, matrix, x, y):
        # self._xco = x
        # self._yco = y
        self.__xpos = x
        self.__ypos = y
        for i in range(len(self._obs)):
            if i==0:
                max = len(self._obs[i])
            else:
                if len(self._obs[i]) > max:
                    max = len(self._obs[i])
            for j in range(len(self._obs[i])):
                # if self._obs[i][j] != ' ':
                matrix[i+x][j+y]._char = self._obs[i][j]
                matrix[i+x][j+y]._xco = x
                matrix[i+x][j+y]._yco = y
                matrix[i+x][j+y]._type = 'D'
                matrix[i+x][j+y]._len1 = len(self._obs)
                matrix[i+x][j+y]._len2 = 68
    
    def moveUp(self, matrix, x, y):
        for i in range(len(self._obs)):
            for j in range(len(self._obs[i])):
                # if i == len(self._obs)-2:
                    # print(j)
                matrix[i+x+1][j+y]._char = ' '
                matrix[i+x+1][j+y]._type = 'B'
                matrix[i+x+1][j+y]._xco = 0
                matrix[i+x+1][j+y]._yco = 0
                matrix[i+x+1][j+y]._len1 = 0
                matrix[i+x+1][j+y]._len2 = 0

                matrix[i+x][j+y]._char = self._obs[i][j]
                matrix[i+x][j+y]._type = 'D'
                matrix[i+x][j+y]._xco = x
                matrix[i+x][j+y]._yco = y
                matrix[i+x][j+y]._len1 = len(self._obs)
                matrix[i+x][j+y]._len2 = 68
    
    def moveDown(self, matrix, x, y):
        # print(x)
        # print(y)
        # print(i)
        # print(j)
        for i in range(len(self._obs)):
            for j in range(len(self._obs[i])):
                # if i == 0:
                matrix[i+x-1][j+y]._char = ' '
                matrix[i+x-1][j+y]._type = 'B'
                matrix[i+x-1][j+y]._xco = 0
                matrix[i+x-1][j+y]._yco = 0
                matrix[i+x-1][j+y]._len1 = 0
                matrix[i+x-1][j+y]._len2 = 0

        for i in range(len(self._obs)):
            for j in range(len(self._obs[i])):
                matrix[i+x][j+y]._char = self._obs[i][j]
                matrix[i+x][j+y]._type = 'D'
                matrix[i+x][j+y]._xco = x
                matrix[i+x][j+y]._yco = y
                matrix[i+x][j+y]._len1 = len(self._obs)
                matrix[i+x][j+y]._len2 = 68