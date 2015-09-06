# Main script for Punkten calculations

import prodfeat, prodsend, prodmaketrain

from sklearn import svm
from sklearn.externals import joblib

BUTTONPATH = '/home/pi/esh/buttons/button.csv'
LEDPATH = '/home/pi/esh/leds/confess'
MLPATH = '/home/pi/esh/prod/ML/SVN.pkl'
PYPATH = '/home/pi/esh/prod/'
PREDLOW = 2
PREDHIGH = 4


def setbutton(prediction):
	col = ""
	if(prediction < 2):
		col = "r"
	elif(prediction < 4 and prediction >= 2):
		col = "y"
	else:
		col = "g"

	f = open(LEDPATH,'w')
	f.write(col)
	f.close()
	return 


def getdatapredict():
	allnewfeatures = prodfeat.main()
	print ("allnewfeatures: " + str(allnewfeatures))
	# make predictions
	if (allnewfeatures!=[]):
		Ysave = []
		clf = joblib.load(MLPATH)
		Xpred = [feature[1:] for feature in allnewfeatures]	
		Ypred = clf.predict(Xpred)
		

		indexprediction = [feature[0] for feature in allnewfeatures]
		for i in range(len(indexprediction)):
			Ysave.append([indexprediction[i],Ypred[i]])

		prodfeat.savefeature(Ysave,'PredSave.csv')

		# print Ysave

		# send predictions
		prodsend.sendreq(Ysave)


		# update colors
		# ***
		lastpred=Ysave[:]
		print(lastpred)
		# setbutton(lastpred)
	return

def getbuttontrain():
	fbut = open(BUTTONPATH,'r')
	# fbut = f1.read()
	# f1.close()
	fappend = open(PYPATH + 'butimportlog','a')
	f2 = open(PYPATH + 'butimportlog','r')
	fread = f2.read()
	f2.close()

	newclicks = []

	for line in fbut:
		# print fread.find(line[:10])
		if(fread.find(line[:10]) == -1):
			newclicks.append(line)
			fappend.write(line + "\n")

	fappend.close()
	if (newclicks == []):
		# print("no new clicks")
		return -1

	for click in newclicks:
		clicktime=click[:10]
		clickcol=click[11:]		
		# print(clicktime)
		# print(clickcol)
		
			
	return		

	

def main():
	while True:
		# 1. Get and save all new features if new files are available:
		# -----------------------------------
		# getdatapredict()
		
		# check for buttons
		getbuttontrain()


	return

if __name__ == "__main__":
	main()