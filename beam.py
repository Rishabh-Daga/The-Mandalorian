import os
from colorama import Fore, Back, Style
from screen import Obstacle
from board import Cell

class Beam(Obstacle, Cell):
    def __init__(self):
        Cell.__init__(self)
        Obstacle.__init__(self)
    
    def place(self, matrix, x, y, f1, f2, l1, l2):
        for i in range(len(self._obs)):
            for j in range(len(self._obs[i])):
                # print(i+x+f1)
                # print(j+y+f2)
                matrix[i+x+f1][j+y+f2]._char = self._obs[i][j]
                matrix[i+x+f1][j+y+f2]._xco = x
                matrix[i+x+f1][j+y+f2]._yco = y
                matrix[i+x+f1][j+y+f2]._type = 'N'
                matrix[i+x+f1][j+y+f2]._len1 = l1
                matrix[i+x+f1][j+y+f2]._len2 = l2