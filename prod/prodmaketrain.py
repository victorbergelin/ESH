# prodmaketrain.py
import csv

BUTTONFILE = 'button.csv'
FEATUREFILE = 'features.csv'

SECSBEFORECLICK = 120
SECSAFTERCLICK = 600

def getclicks():
	results = []
	with open(BUTTONFILE, 'rb') as csvfile:
		filereader = csv.reader(csvfile, delimiter=',')
		for lines in list(filereader):
			lines = map(int, lines)
			results.append(lines)
	return results

def getfeatures():
	results = []
	with open(FEATUREFILE, 'rb') as csvfile:
		filereader = csv.reader(csvfile, delimiter=',')
		for lines in list(filereader):
			lines = map(int, lines)
			results.append(lines)
	return results

def getcleanfeatures():
	results = []
	with open(FEATUREFILE, 'rb') as csvfile:
		filereader = csv.reader(csvfile, delimiter=',')
		for lines in list(filereader):
			lines = map(int, lines)
			results.append(lines)
	return results

def maketrainingdata(featurelist,clicklist):
	resultsX = []
	resultsY = []
	for click in clicklist:
		#debug
		#print(click)
			# trainingY = []
			# trainingX = []
		for feature in featurelist:
			diff = click[0]-feature[0]
			if(diff>=-SECSBEFORECLICK and diff < SECSAFTERCLICK):
				# debug
				# print("		" + str([diff,feature[0]]))
				resultsX.append(feature)
				resultsY.append([feature[0],click[1]])

		#resultsX.append(trainingX)
		#resultsY.append(trainingY)

	return [resultsX,resultsY]

def main():

	clicklist = getclicks()
	featurelist = getfeatures()
	trainingdata = maketrainingdata(featurelist,clicklist)
	trainingsize = len(trainingdata[0])
	print("Training data size is: " + str(trainingsize))
	return trainingdata

if __name__ == "__main__":
	main()
