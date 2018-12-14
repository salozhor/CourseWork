from imgrecognizer import recognizer
import random
from datasetoperations import readLearningDataset
import
class classroom():
	students = [recognizer() for x in range(10)]    ### first 10 coef sets are generated randomly
	best = -1
	bestresult = [-1 for num in range(10)]
	beststudent = [recognizer() for num in range(10)]
	prevbest = [-1 for num in range(10)]
	prevdigit = 0
	def lesson(self, image, winner):### generating new ones from the best one and comparing their results for drawn number
		digit = image.digit
		print(self.bestresult, self.prevdigit)
		if self.prevbest[self.prevdigit] <self.bestresult[self.prevdigit]:
			self.prevbest[self.prevdigit] = self.bestresult[self.prevdigit]
		self.bestresult[digit] = -1
		self.students = [recognizer(winner = winner) for x in range(10)] ###creating new students from previous best one
		result = [[]for x in range(10)]
		
		for st in range(10):
			self.students[st].generateCoef()
			result[st] = self.students[st].calculate(image)[image.digit]
		maxProb = max(result)
		for st in range(10):
			if result[st] == maxProb:
				self.best = st
		if self.prevbest[digit] < result[self.best]:
			self.bestresult[digit] = result[self.best]
			self.beststudent[digit] = self.students[st]
		self.prevdigit = digit
	
	def firstlesson(self, image):### comparing their results for drawn number
		digit = image.digit
		students = [recognizer() for x in range(10)]
		result = [[]for x in range(10)]
		
		for st in range(10):
			self.students[st].generateCoef()
			result[st] = self.students[st].calculate(image)[image.digit]
		maxProb = max(result)
		for st in range(10):
			if result[st] == maxProb:
				self.best = st
		self.bestresult[digit] = result[self.best]
		
	def study(self, image):
		learning = []
		readLearningDataset(learning)
		self.firstlesson(image)
		image = learning[random.randint(0,505)]
		digit = image.digit
		while self.bestresult[digit] <= 95:
			self.lesson(image, self.beststudent)
			print(self.prevbest)
			image = learning[random.randint(0,505)]
			
	#def saverecognizer(self):
		#with open('coef.txt', 'w'):
		
		
