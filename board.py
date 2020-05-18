import os
import numpy as np
from colorama import Fore, Back, Style, init
import config
init()


class Cell:
    def __init__(self):
        self._type = 'B'
        self._char = ' '
        self._xco = 0
        self._yco = 0
        self._len1 = 0
        self._len2 = 0

    # def display(self):
    #     print(self._char)

class Board:
    def __init__(self, rows, columns):
        # Cell.__init__(self)
        self.__rows = rows
        self.__columns = columns
        self.__matrix = [[Cell() for j in range(self.__columns)] for i in range(self.__rows)]
        # self.__type = 'board'
    @property
    def matrix(self):
        return self.__matrix
    @property
    def rows(self):
        return self.__rows
    @property
    def columns(self):
        return self.__columns
    def createBoard(self):
        pass
        # self.__matrix = np.full((self.__rows, self.__columns), Cell)
        # for i in range(self.__rows):
        #     for j in range(self.__columns):
        #         self.__matrix[i].append(Cell())
        # for i in range(0, self.__columns):
        #     self.__matrix[0][i] = '~'
    
    def printBoard(self,cnt, dLife):
        # os.system('clear')
        print("\033[0;0H")
        print(Fore.RED + "LIVES LEFT:", str(config.lives)+' ', end = '    \t \t' + Style.RESET_ALL)
        print(Fore.RED + "Score:", config.score, end = '    \t \t' + Style.RESET_ALL)
        print(Fore.RED + "Shield Available: ", config.shield_available , end='    \t \t'+ Style.RESET_ALL)
        print(Fore.RED + "Shield Active: ", config.shield_active , end='\n'+ Style.RESET_ALL)
        print(Fore.RED + "Boss Lives", dLife , end='    \t \t'+ Style.RESET_ALL)
        print(Fore.RED + "Game Time:", config.time, end='    \t \t'+ Style.RESET_ALL)
        print(Fore.RED + "Game Speed:",str(config.bs+1)+'x', end='\n'+ Style.RESET_ALL)
        for i in range(0, self.__rows):
            for j in range(0+cnt ,130+cnt):
                if i==0:
                    print(Back.BLUE + self.__matrix[i][j]._char + Style.RESET_ALL, end='')
                elif self.__matrix[i][j]._char == 'm':
                    print(Back.RED + Fore.RED + self.__matrix[i][j]._char + Style.RESET_ALL, end='')
                elif self.__matrix[i][j]._char == 't':
                    print(Back.YELLOW + Fore.YELLOW + self.__matrix[i][j]._char + Style.RESET_ALL, end='')
                elif self.__matrix[i][j]._char == 'v':
                    if config.shield_active:
                        print(Back.BLUE + Fore.BLUE + self.__matrix[i][j]._char + Style.RESET_ALL, end='')
                    else:
                        print(Back.GREEN + Fore.GREEN + self.__matrix[i][j]._char + Style.RESET_ALL, end='')
                elif self.__matrix[i][j]._char == 'c':
                    if config.shield_active:
                        print(Back.RED + Fore.RED + self.__matrix[i][j]._char + Style.RESET_ALL, end='')
                    else:
                        print(Back.BLUE + Fore.BLUE + self.__matrix[i][j]._char + Style.RESET_ALL, end='')
                elif self.__matrix[i][j]._char == 'p':
                    if config.shield_active:
                        print(Back.YELLOW + Fore.YELLOW+ self.__matrix[i][j]._char + Style.RESET_ALL, end='')
                    else:
                        print(Back.MAGENTA + Fore.MAGENTA + self.__matrix[i][j]._char + Style.RESET_ALL, end='')
                elif self.__matrix[i][j]._char == 's':
                    print(Fore.RED + self.__matrix[i][j]._char + Style.RESET_ALL, end='')
                elif self.__matrix[i][j]._char == 'x':
                    print(Back.BLUE + Fore.BLUE + self.__matrix[i][j]._char + Style.RESET_ALL, end='')
                elif self.__matrix[i][j]._char == '$':
                    print(Fore.BLUE + self.__matrix[i][j]._char + Style.RESET_ALL, end='')
                elif self.__matrix[i][j]._char == 'H':
                    print(Back.RED + Fore.RED + self.__matrix[i][j]._char + Style.RESET_ALL, end='')
                elif self.__matrix[i][j]._char == 'F':
                    print(Fore.YELLOW + self.__matrix[i][j]._char + Style.RESET_ALL, end='')
                elif self.__matrix[i][j]._char == '>' or self.__matrix[i][j]._char == '=':
                    print(Fore.WHITE + self.__matrix[i][j]._char + Style.RESET_ALL, end='')
                elif self.__matrix[i][j]._type == 'D':
                    print(Fore.YELLOW + self.__matrix[i][j]._char + Style.RESET_ALL, end='')
                    # if self.__matrix[i][j]._char == 'a' or self.__matrix[i][j]._char == '|':
                    #     print(Back.RED + Fore.RED + self.__matrix[i][j]._char + Style.RESET_ALL, end='')
                    # else:
                # elif self.__matrix[i][j]._char == '=':
                #     print(Fore.LIGHTBLACK_EX + self.__matrix[i][j]._char + Style.RESET_ALL, end='')
                # elif self.__matrix[i][j]._char == '|':
                #     print(Back.RED + Fore.RED + self.__matrix[i][j]._char + Style.RESET_ALL, end='')
                # elif self.__matrix[i][j]._char == ' ':
                #    print(Back.YELLOW + Fore.YELLOW + self.__matrix[i][j]._char + Style.RESET_ALL, end='')
                else:
                    # print(self.__matrix[i][j]._type, end='')
                    print(self.__matrix[i][j]._char, end = '')
            # print(Style.RESET_ALL)
            print()
    def changeType(self, type):
        self.__type = type
    
    def getType(self):
        return self.__type