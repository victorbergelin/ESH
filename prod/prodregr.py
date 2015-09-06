#prodML.py

from sklearn import svm
import csv

FEATUREFILE = 'features.csv'

def trainmodel(X):
	return X


def getfeatures():
	results = []
	with open(FEATUREFILE, 'rb') as csvfile:
		filereader = csv.reader(csvfile, delimiter=',')
		for lines in list(filereader):
			lines = map(int, lines)
			results.append(lines)
	return results

def main():
	
	# load features from file
	X = getfeatures()
	Y = getbuttonvals()
	print(X)

	# ML()

if __name__ == "__main__":
	main()
