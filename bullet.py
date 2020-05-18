import os
from colorama import Fore, Back, Style
from screen import Obstacle
from board import Cell
import time
import config

class Bullet(Cell, Obstacle):
    def __init__(self, x, y):
        self.__my_co = {
            x : [y, y + 1]
        }
        self.__my_print = {
            0 : ['-', '>']
        }
        self.__living = 1
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
                new_co[i].append(j + 4)
                for k in range(j, j + 5):
                    if matrix[i][k]._type == 'N':
                        config.collision(matrix, matrix[i][k]._xco, matrix[i][k]._yco, matrix[i][k]._len1, matrix[i][k]._len2, 'b')
                        self.__living = 0
                        return
                    elif matrix[i][k]._type == 'D':
                        config.collision(matrix, i, k, matrix[i][k]._len1, matrix[i][k]._len2, 'b')
                        self.__living = 0
                        return
                    if matrix[i][k]._type == 'P':
                        config.collision(matrix, matrix[i][k]._xco, matrix[i][k]._yco, matrix[i][k]._len1, matrix[i][k]._len2, 'b')
                        self.__living = 0
                        return
        for i in new_co:
            for j in new_co[i]:
                if j >= last:
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