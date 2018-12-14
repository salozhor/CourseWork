import random
import cv2


class recognizer():
	winner = []
	truewinner = False
	def __init__(self, winner = None):
		
		if winner != None:
			self.winner = winner
			self.truewinner = True
		
	coef = [[[[0 for l in range(2)] for k in range(2)]for x in range(8)]for n in range(10)]
	image = []
	luckyNumber	= -1
	
	def generateCoef(self):
		if self.truewinner:
			for number in range(10):
				for dim in range(8):
					for line in range(2):
						for element in range(2):
							random.seed(random.random())
							self.coef[number][dim][line][element] = ((float(random.randint(-1000, 1000))/1000)+3*self.winner[number].coef[number][dim][line][element])/4
		else:
			for number in range(10):
				for dim in range(8):
					for line in range(2):
						for element in range(2):
							random.seed(random.random())
							self.coef[number][dim][line][element] = float(random.randint(-1000, 1000))/1000
	
	def calculate(self, image):
		self.image = image.content
		probability = [0 for number in range(10)]
		
		for number in range(10):
			
			dim = 7
			matrix7 = [[0 for alpha in range(7)] for beta in range(7)]      ###     8x8 to 7x7
			for i in range(7):
				for j in range(7):
					matrix7[i][j] = self.coef[number][dim][0][0] * self.image[i][j] + self.coef[number][dim][1][0] * self.image[i+1][j] + \
								self.coef[number][dim][0][1] * self.image[i][j+1] + self.coef[number][dim][1][1] * self.image[i+1][j+1]
					
			dim = 6
			matrix6 = [[0 for alpha in range(6)] for beta in range(6)]      ###     7x7 to 6x6
			for i in range(6):
				for j in range(6):
					matrix6[i][j] = self.coef[number][dim][0][0] * matrix7[i][j] + self.coef[number][dim][1][0] * matrix7[i+1][j] + \
								self.coef[number][dim][0][1] * matrix7[i][j+1] + self.coef[number][dim][1][1] * matrix7[i+1][j+1]
					
			dim = 5
			matrix5 = [[0 for alpha in range(5)] for beta in range(5)]      ###     6x6 to 5x5
			for i in range(5):
				for j in range(5):
					matrix5[i][j] = self.coef[number][dim][0][0] * matrix6[i][j] + self.coef[number][dim][1][0] * matrix6[i+1][j] + \
								self.coef[number][dim][0][1] * matrix6[i][j+1] + self.coef[number][dim][1][1] * matrix6[i+1][j+1]
					
			dim = 4
			matrix4 = [[0 for alpha in range(4)] for beta in range(4)]      ###     5x5 to 4x4
			for i in range(4):
				for j in range(4):
					matrix4[i][j] = self.coef[number][dim][0][0] * matrix5[i][j] + self.coef[number][dim][1][0] * matrix5[i+1][j] + \
								self.coef[number][dim][0][1] * matrix5[i][j+1] + self.coef[number][dim][1][1] * matrix5[i+1][j+1]
					
			dim = 3
			matrix3 = [[0 for alpha in range(3)] for beta in range(3)]      ###     4x4 to 3x3
			for i in range(3):
				for j in range(3):
					matrix3[i][j] = self.coef[number][dim][0][0] * matrix4[i][j] + self.coef[number][dim][1][0] * matrix4[i+1][j] + \
								self.coef[number][dim][0][1] * matrix4[i][j+1] + self.coef[number][dim][1][1] * matrix4[i+1][j+1]
					
			dim = 2
			matrix2 = [[0 for alpha in range(2)] for beta in range(2)]      ###     3x3 to 2x2
			for i in range(2):
				for j in range(2):
					matrix2[i][j] = self.coef[number][dim][0][0] * matrix3[i][j] + self.coef[number][dim][1][0] * matrix3[i+1][j] + \
								self.coef[number][dim][0][1] * \
								    matrix3[i][j+1] + \
								    self.coef[number][dim][1][1] *\
								    matrix3[i+1][j+1]
			
			dim, i, j = 1, 0, 0
			matrix1 = self.coef[number][dim][0][0] * matrix2[i][j] + self.coef[number][dim][1][0] * matrix2[i+1][j] + \
					self.coef[number][dim][0][1] * matrix2[i][j+1] + self.coef[number][dim][1][1] * matrix2[i+1][j+1]
			###     FINAL PREDICTION FOR number IN file
			probability[number] = matrix1
		sum = 0
		min = 0
		for prob in probability:
			if min>prob:
				min = prob
		for i in range(10):
			probability[i] += abs(min)
			sum+=probability[i]
		if sum!= 0:
			for i in range(10):
				probability[i] = float(probability[i])*100/sum
		return probability
