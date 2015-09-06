# Main script for Punkten calculations

import prodfeat, prodsend
BUTTONPATH='/home/pi/esh/buttons'
PREDLOW = 2
PREDHIGH = 4


def setbutton(prediction):
	if (prediction < PREDLOW
 	
	return

def main():
	while True:
		# 1. Get and save all new features if new files are available:
		# -----------------------------------
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


		
		# check for buttons



	return

if __name__ == "__main__":
	main()