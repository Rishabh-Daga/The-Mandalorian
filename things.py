import random
from board import obj_board,temp

class Obstacle:

	def create_x(self):
		return random.randint(2,25)

	def create_obstacle(self):
			
		for y in range(70,1211,50):
			x = self.create_x()	
			choose = random.randint(1,4)
			# straight obstacle
			if choose == 1:
				obs = [['O'],['O'],['O'],['O'],['O'],['O']]
				for i in range(len(obs)):
					for j in range(len(obs[0])):
						obj_board.matrix[x + i][y + j] = obs[i][j]
			# right diagonal
			if choose == 2:
				obs = [[' ',' ',' ',' ',' ','O'],
					   [' ',' ',' ',' ','O',' '],
					   [' ',' ',' ','O',' ',' '],
					   [' ',' ','O',' ',' ',' '],
					   [' ','O',' ',' ',' ',' '],
					   ['O',' ',' ',' ',' ',' ']]
				for i in range(len(obs)):
					for j in range(len(obs[0])):
						obj_board.matrix[x + i][y + j] = obs[i][j]
			# left diagonal
			if choose == 3:
				obs = [['O',' ',' ',' ',' ',' '],
					   [' ','O',' ',' ',' ',' '],
					   [' ',' ','O',' ',' ',' '],
					   [' ',' ',' ','O',' ',' '],
					   [' ',' ',' ',' ','O',' '],
					   [' ',' ',' ',' ',' ','O']]
				for i in range(len(obs)):
					for j in range(len(obs[0])):
						obj_board.matrix[x + i][y + j] = obs[i][j]
			# horizontal obstacle
			if choose == 4:
				obs = ['O','O','O','O','O','O']
				for i in range(len(obs)):
					for j in range(len(obs[0])):
						obj_board.matrix[x + i][y + j] = obs[i][j]
	
	def clear_obstacle(self,cox,coy):
		for i in range(6):
			for j in range(6):
				if cox > 2 and cox < 31 and obj_board.matrix[cox][coy+j] == 'O':
					obj_board.matrix[cox][coy+j] = ' '
				if cox + i > 2 and cox + i < 31 and obj_board.matrix[cox+i][coy] == 'O':
					obj_board.matrix[cox+i][coy] = ' '
				if cox > 2 and cox < 31 and obj_board.matrix[cox][coy-j] == 'O':
					obj_board.matrix[cox][coy-j] = ' '
				if cox - i > 2 and cox - i < 31 and obj_board.matrix[cox-i][coy] == 'O':
					obj_board.matrix[cox-i][coy] = ' '
				if cox + i > 2 and cox + i < 31 and obj_board.matrix[cox+i][coy+j] == 'O':
					obj_board.matrix[cox+i][coy+j] = ' '
				if cox + i > 2 and cox + i < 31 and obj_board.matrix[cox+i][coy-j] == 'O':
					obj_board.matrix[cox+i][coy-j] = ' '
				if cox - i > 2 and cox - i < 31 and obj_board.matrix[cox-i][coy+j] == 'O':
					obj_board.matrix[cox-i][coy+j] = ' '
				if cox - i > 2 and cox - i < 31 and obj_board.matrix[cox-i][coy-j] == 'O':
					obj_board.matrix[cox-i][coy-j] = ' '

class Coins(Obstacle):

	def create_coins(self):
		for y in range(40,1211,50):
			x1 = self.create_x()
			coin = [['$' for i in range(10)] for j in range(3)]
			for i in range(len(coin)):
				for j in range(len(coin[0])):
				   obj_board.matrix[x1 + i][y + j] = coin[i][j]
				print()

class Magnet(Obstacle):
		
	mnt = []
	def create_magnet(self):
		for y in range(140,1211,400):
			x1 = self.create_x()
			self.mnt.append([x1,y])
			mag = ['(',')']
			for j in range(len(mag)):
				obj_board.matrix[x1][y + j] = mag[j]
	
class Bullet:
	det = []
	def move_bullet(self,k):
		f = 0
		for entry in bull.det:
			if entry[1] < k + 137 and entry[2]:
				for i in range(5):
					temp.matrix[entry[0]][entry[1]+1+i] = obj_board.matrix[entry[0]][entry[1]+1+i]				
				if obj_board.matrix[entry[0]][entry[1]+3] == 'O':
					obsta.clear_obstacle(entry[0],entry[1]+3)
					entry[2] = 0
					self.f = 1
				elif obj_board.matrix[entry[0]][entry[1]+2] == 'O':
					obsta.clear_obstacle(entry[0],entry[1]+2)
					entry[2] = 0
					self.f = 1
				elif obj_board.matrix[entry[0]][entry[1]+1] == 'O':
					obsta.clear_obstacle(entry[0],entry[1])
					entry[2] = 0
					self.f = 1
					# q = 1
				if entry[2]:
					obj_board.matrix[entry[0]][entry[1]+3] = '>'
					obj_board.matrix[entry[0]][entry[1]] = temp.matrix[entry[0]][entry[1]]
					entry[1] += 3
			elif entry[1] > k + 137 or entry[2] == 0:
				entry[2] = 0
				obj_board.matrix[entry[0]][entry[1]] = temp.matrix[entry[0]][entry[1]]
		return f

	def check_enemy(self,k):
		for entry in bull.det:
			if entry[1] > k + 1 and entry[2]:
				if (obj_board.matrix[entry[0]][entry[1]+3] or obj_board.matrix[entry[0]][entry[1]+2] or obj_board.matrix[entry[0]][entry[1]+1]) in ['.','-','o','(',')','|','\\','`','~','0']:
					entry[2] = 0
					return 1
		return 0
			

class Enemy_Bullet:
	dfe = []
	f1 = 0
	def move_fire(self,bosx):
		e_b.dfe.append([bosx+1,1290,1])
	def accelerate(self,k):
		self.f1 = 0
		for entry in e_b.dfe:
			print(entry)
			if entry[2] and entry[1] > 1190 and entry[1] < 1327:
				for i in range(5):
					temp.matrix[entry[0]][entry[1]+1+i] = obj_board.matrix[entry[0]][entry[1]+1+i]
				if obj_board.matrix[entry[0]][entry[1]-3] in ['\\','O','*']:
					obj_board.matrix[entry[0]][entry[1]] = ' '
					entry[2] = 0
					self.f1 = 1
					# obj_board.matrix[entry[0]][entry[1]] = ' '
				elif obj_board.matrix[entry[0]][entry[1]-2] in ['\\','O','*']:
					obj_board.matrix[entry[0]][entry[1]] = ' '
					entry[2] = 0
					self.f1 = 1
					# obj_board.matrix[entry[0]][entry[1]+1] = ' '
				elif obj_board.matrix[entry[0]][entry[1]-1] in ['\\','O','*']:
					obj_board.matrix[entry[0]][entry[1]] = ' '
					entry[2] = 0
					self.f1 = 1
					# obj_board.matrix[entry[0]][entry[1]+2] = ' '
				if entry[2]:
					obj_board.matrix[entry[0]][entry[1]-3] = '<'
					obj_board.matrix[entry[0]][entry[1]] = temp.matrix[entry[0]][entry[1]]
					entry[1] -= 3
			elif entry[1] < k + 1 or entry[2] == 0:
					entry[2] = 0
					# obj_board.matrix[entry[0]][entry[1]] = temp.matrix[entry[0]][entry[1]]
		if self.f1:
			return 1
		return 0

cons = Coins()
obsta = Obstacle()
magn = Magnet()
bull = Bullet()
e_b = Enemy_Bullet()
