class Board:

	def __init__(self, rows, columns): # initialize values
		
		self.__rows = rows
		self.__columns = columns
		self.__matrix = [[' ' for i in range(self.__columns)] for j in range(self.__rows)]
	
	def create_sky(self):
		
		for i in range(self.__columns):
			self.__matrix[0][i] = '='
	
	def create_ground(self):

		for i in range(self.__columns):
			self.__matrix[self.__rows-1][i] = '='

	@property
	def rows(self):
		return self.__rows
	@rows.setter
	def rows(self,x):
		self.__rows=x

	@property
	def columns(self):
		return self.__columns
	@columns.setter
	def columns(self,x):
		self.__columns=x

	@property
	def matrix(self):
		return self.__matrix
	@matrix.setter
	def matrix(self,x):
		self.__matrix=x

obj_board = Board(34,1400)
temp = Board(34,1400)
