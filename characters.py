import signal
import time
from things import obsta,bull,magn,e_b
from colorama import Fore, Back, Style
from board import obj_board
from getch import _getChUnix as getChar
from alarmexception import AlarmException

class Player:
	
	t_n = 0
	nitro = 0
	t = -60
	acc = 0
	player = [[' ','O',' '],['*','|','*'],['/',' ','\\']]
	shield = 0

	def __init__(self):
		self.__posx = 10
		self.__posy = 20
		self.__c = 0
		self.__life = 3

	def create_player(self):
	
		for i in range(3):
			for j in range(3):
				if obj_board.matrix[self.__posx+i][self.__posy+j] not in ['(',')']:
					obj_board.matrix[self.__posx+i][self.__posy+j] = self.player[i][j]

	def clear_player(self):
	
		for i in range(3):
			for j in range(3):
				if obj_board.matrix[self.__posx+i][self.__posy+j] not in ['(',')']:
					obj_board.matrix[self.__posx+i][self.__posy+j] = ' '
	
	def check_player(self):

		check = 0
		for i in range(3):
			for j in range(3+self.nitro):
				if obj_board.matrix[self.__posx+i][self.__posy+j] == 'O':
					obsta.clear_obstacle(self.__posx+i,self.__posy+j)
					self.__c += 5
					if self.shield == 0:
						check = 1
				if obj_board.matrix[self.__posx+i][self.__posy+j] == '$' or (self.nitro and obj_board.matrix[self.__posx+3][self.__posy+3] == '$'):
					self.__c += 1
		self.__life -= check
		if self.__life == 0:
			print('You LOSE !!!')
			exit()
		if check:
			return 1
		return 0

	def move_player(self,k):
	
		def alarmhandler(signum, frame):
			raise AlarmException

		def user_input(timeout=0.05):
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

		char = user_input()

		# Boundary condition 
		if self.__posy < k + 2 + self.nitro:
			self.clear_player()
			self.__posy = k + 2 + self.nitro
			self.check_player()
			self.create_player()
		
		# Press 'q' for quit.
		if char == 'q':
			quit()

		# Press 'w' for up.
		if char == 'w' and self.__posx > 4:
			self.acc = 0
			self.clear_player()
			self.__posx -= 4
			if self.check_player():
				self.__posx = 10
				self.__posy = k + 50 + self.nitro
			self.create_player()

		# Press 'a' for left.
		if char == 'a':
				# for i in range(2):
			self.clear_player()
			self.__posy -= 2 + self.nitro
			if self.check_player():
				self.__posx = 10
				self.__posy = k + 50 + self.nitro
			self.create_player()

		# Press 'd' for right.
		if char == 'd' and self.__posy < k + 131 + self.nitro:
				# for i in range(4):
			self.clear_player()
			self.__posy += 2 + self.nitro
			if self.check_player():
				self.__posx = 10
				self.__posy = k + 50 + self.nitro
			self.create_player()

		# Press 'Space' for shield
		if char == ' ' and time.time() - self.t >= 60:
			self.shield = 1
			self.t = time.time()
			
		if time.time() - self.t >= 10 and self.shield == 1:
			self.shield = 0
			self.t = time.time()

		if char == 'n':
			self.nitro = 2
			self.t_n = time.time()

		if time.time() - self.t_n >= 5:
			self.nitro = 0
			self.t_n = time.time()

		# Gravity
		self.acc += 1
		if self.__posx < 30 - self.acc:
			self.clear_player()
			self.__posx += self.acc
			if self.check_player():
				self.__posx = 10
				self.__posy = k + 50 + self.nitro
			self.create_player()
		elif self.__posx < 30:
			self.clear_player()
			self.__posx += 1
			if self.check_player():
				self.__posx = 10
				self.__posy = k + 50 + self.nitro
			# self.check_gravity(1)
			self.create_player()

		# Bullet
		if char == 'f':
			bull.det.append([self.__posx,self.__posy+3,1])
		
		# Magnet
		for i in range(3): 
			if magn.mnt[i][1] - self.__posy <= 40 and magn.mnt[i][1] - self.__posy >= 0:
				self.clear_player()
				self.__posy += 1 + self.nitro
				if self.check_player():
					self.__posx = 10
					self.__posy = k + 50 + self.nitro
				self.create_player()
			if self.__posy - magn.mnt[i][1] <= 40 and self.__posy - magn.mnt[i][1] >= 0:
				self.clear_player()
				self.__posy -= 1 - self.nitro
				if self.check_player():
					self.__posx = 10
					self.__posy = k + 50 + self.nitro
				self.create_player()

	@property
	def life(self):
		return self.__life	
	@life.setter
	def life(self,x):
		self.__life=x

	@property
	def c(self):
		return self.__c	
	@c.setter
	def c(self,x):
		self.__c=x

	@property
	def posx(self):
		return self.__posx
	@posx.setter
	def posx(self,x):
		self.__posx=x

	@property
	def posy(self):
		return self.__posy
	@posy.setter
	def posy(self,x):
		self.__posy=x

class Enemy(Player):
		
	def __init__(self,in_x,in_y):
		
		with open('boss.txt') as f:
			self.b = f.readlines()
		self.b = [row.rstrip('\n') for row in self.b]
		self.bsx = in_x
		self.health = 15
			
	def create_boss(self,bosx):
		
		for i in range(len(self.b)):    	
			for j in range(1290,1290 + len(self.b[i])):
				obj_board.matrix[bosx + i][j] = self.b[i][j-1290]
		self.bsx = bosx

	def clear_boss(self,bosx):
	
		for i in range(len(self.b)):    	
			for j in range(1290,1290 + len(self.b[i])):
				obj_board.matrix[bosx + i][j] = ' '
	
	def move_boss(self,posx):
		self.clear_boss(self.bsx)
		self.create_boss(posx)
		# if bull.move_bullet(obj_player.k,0):
			# self.health -= 1

obj_player = Player()
obj_boss = Enemy(obj_player.posx - 2,1290)