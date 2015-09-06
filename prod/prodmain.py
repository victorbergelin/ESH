# Main script for Punkten calculations

import prodfeat, prodsend

def main():
	while True:
		# get and save all new features:
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

		# check for new recordings, if none continue
			
		# check for buttons



	return

if __name__ == "__main__":
	main()