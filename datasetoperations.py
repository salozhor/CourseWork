import os.path
from img import img


def readLearningDataset(learning):
	for digit in range(10):
		for fileNumber in range(1000):
			if os.path.isfile(os.path.join('/media/salozhor/42A074B5A074B0D1/CurseV2/learn', str(digit) + str(fileNumber) + '.png')):
				image = img(digit, fileNumber, img.LEARN)
				image.open()
				learning.append(image)
