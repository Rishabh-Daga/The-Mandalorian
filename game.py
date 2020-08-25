import os
import time
import random
from colorama import Fore, Back, Style
from board import obj_board , temp
from characters import obj_player,obj_boss
from things import obsta,cons,magn,bull,e_b

obj_board.create_sky()
obj_board.create_ground()
obj_player.create_player()
obsta.create_obstacle()
cons.create_coins()
magn.create_magnet()
obj_boss.create_boss(obj_player.posx)

s = 0
k = 0
tame = int(time.time())
rem = 80

while True:
	for i in range(obj_board.rows):
		for j in range(k, 137 + k):
			if obj_player.shield == 1 and (obj_board.matrix[i][j] in ['*','\\','/','|'] or (obj_board.matrix[i][j] == 'O' and i == obj_player.posx and j == obj_player.posy + 1)):
				print(Fore.GREEN + obj_board.matrix[i][j], end = '')
			elif obj_board.matrix[i][j] == 'O' and (i != obj_player.posx or j != obj_player.posy + 1):
				print(Fore.RED + obj_board.matrix[i][j], end = '')
			elif obj_board.matrix[i][j] == '$':
				print(Fore.YELLOW + obj_board.matrix[i][j], end = '')
			elif obj_board.matrix[i][j] in ['(',')']:
				print(Fore.CYAN + obj_board.matrix[i][j], end = '')
			else:
				print(Fore.WHITE + obj_board.matrix[i][j], end = '')
		print()
	if obj_boss.health == 0:
		print('You WIN !!!')
		exit()
	if obj_player.life == 0:
		print('You LOST !!!')
		exit()
	if int(rem+tame-time.time()) <= 0 and k < 1190:
		print('Time\'s up !!!')
		exit()
	elif k >= 1190:
		k -= max(1,obj_player.nitro)
		print('Lives {}			Score {}		Enemy\'s Health {}'.format(obj_player.life,obj_player.c,obj_boss.health), end = '')
	else:
		print('Lives {}			Score {}		Time Remaining {}'.format(obj_player.life,obj_player.c,int(rem+tame-time.time())),end = '')
	print('		',k)
	print('\033[0;0H')
	k += max(1,obj_player.nitro)
	s += 1
	obj_player.move_player(k)
	obj_boss.move_boss(min(obj_player.posx - 1,28))
	if k >= 1189 and s % 30 == 0:
		e_b.move_fire(obj_player.posx)
	if e_b.accelerate(k):
		obj_player.life -= 1
	if bull.move_bullet(k):
		obj_player.c += 5
	if bull.check_enemy(k):
		obj_boss.health -= 1
