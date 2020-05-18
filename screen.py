import os
import numpy
import random
from colorama import Fore, Back, Style, init
init()

class Obstacle:
    def __init__(self):
        self._obs = []
        # self._xco = 0
        # self._yco = 0

    def loadObstacle(self, obstacle):
        # print(obstacle)
        file = './objects/%s.txt' % obstacle
        with open(file) as obs:
            for line in obs:
                self._obs.append(line.strip('\n'))

class Screen:
    def __init__(self):
        self.__sky = '~'
        self.__ground = '_'
        self.__magnet = []
        self.__shield = []
        self.__speed = []
    
    def createGround(self, matrix, columns):
        for i in range(columns):
            matrix[37][i]._char = self.__ground

    def createSky(self, matrix, columns):
        for i in range(columns):
            matrix[0][i]._char = self.__sky
    
    def placeMagnets(self, matrix, columns):
        with open('./objects/magnet.txt') as mag:
            for line in mag:
                self.__magnet.append(line.strip('\n'))
        m1 = random.randint(12,20)
        m2 = random.randint(1,7)
        b= random.randint(180,250)
        for i in range(len(self.__magnet)):
            for j in range(len(self.__magnet[i])):
                matrix[i+m1][j+100]._char = self.__magnet[i][j]
                matrix[i+m1][j+100]._type = 'M'
                matrix[i+m2][j+b]._char = self.__magnet[i][j]
                matrix[i+m2][j+b]._type = 'M'

    def placePowerUps(self, matrix, columns):
        with open('./objects/speed_up.txt') as speed:
            for line in speed:
                self.__speed.append(line.strip('\n'))
        for i in range(len(self.__speed)):
            for j in range(len(self.__speed[i])):
                matrix[i+30][j+40]._char = self.__speed[i][j]
                matrix[i+23][j+190]._char = self.__speed[i][j]
