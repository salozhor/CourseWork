import numpy
import cv2
import matplotlib.pyplot as plt
import os.path
from img import img
from datasetoperations import readLearningDataset
from imgrecognizer import recognizer
from array import array
from classroom import classroom
import random
	
if __name__ == '__main__':
	learning = []
	readLearningDataset(learning)
	print(len(learning))
	cr = classroom()
	
	cr.study(learning[random.randint(0,505)])
	
	
	
	###TESTING NEW CLASS
	#r = recognizer()
	#r.generateCoef()
	#print(r.coef)
	
	###TESTING readLearningDataset FUNCTION
	#print(learning[-1].content)
	

