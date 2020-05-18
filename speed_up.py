import os
from colorama import Fore, Back, Style
from screen import Obstacle
from board import Cell

class Speed(Cell, Obstacle):
    def __init__(self):
        Cell.__init__(self)
        Obstacle.__init__(self)
    
    def place(self, matrix, x, y):
        # self._xco = x
        # self._yco = y
        max = 0
        for i in range(len(self._obs)):
            if len(self._obs[i]) > max:
                max = len(self._obs[i])
            for j in range(len(self._obs[i])):
                if self._obs[i][j] != ' ':
                    matrix[i+x][j+y]._char = self._obs[i][j]
                    matrix[i+x][j+y]._xco = x
                    matrix[i+x][j+y]._yco = y
                    matrix[i+x][j+y]._type = 'S'
                    matrix[i+x][j+y]._len1 = len(self._obs)
                    matrix[i+x][j+y]._len2 = 5