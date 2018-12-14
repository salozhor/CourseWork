import os.path
import cv2

class img():
	defaultResolution = [8,8]
	digit = -1
	number = -1
	TEST = 'test'
	LEARN = 'learn'
	__path = ''
	content = []
	
	def __init__(self, digit, number, mode):
		self.digit = digit
		self.number = number
		if mode == self.TEST:
			self.__path = 'test/' + str(self.digit) + '-' + str(self.number) + '.png'
		elif mode == self.LEARN:
			self.__path = 'learn/' + str(self.digit) + str(self.number) + '.png'
		else:
			raise ValueError('Invalid mode! Valid modes are img.TEST and img.LEARN')
		
		
	def open(self, path):
		self.__path = path
		if self.digit >= 0 and self.number >= 0:
			if os.path.isfile():
				self.content = cv2.resize(cv2.imread(self.__path, 0),(8,8))
				return 0
			else:
				return -1
			
			
	def open(self):
		if self.digit >= 0 and self.number >= 0:
			if os.path.isfile(self.__path):
				self.content = cv2.resize(cv2.imread(self.__path, 0),(8,8))
				return 0
			else:
				return -1
