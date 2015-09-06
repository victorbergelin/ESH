#prodpred.py

import prodmaketrain, prodfeat, prodfeat, prodsend

from sklearn import svm
from sklearn.externals import joblib
import csv, os

# ***
import numpy

FEATUREFILE = 'features.csv'
MLPATH = 'ML/SVN.pkl'
RECSPATH = './recs_ESH/'

def listengetnewfiles():
	f = open('importlog','a')
	f2 = open('importlog','r')
	fr=f2.read()
	f2.close()

	newfiles=[]

	for fn in os.listdir(RECSPATH):
	    # DEBUG: print(RECSPATH+fn)
	    if os.path.isfile(RECSPATH+fn) and fn.find('.wav') != -1:
	        if fr.find(fn) == -1:
	        	newfiles.append(fn)
	        	f.write(fn + "\n")
	f.close()
	return newfiles

def main():

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

	return

	

if __name__ == "__main__":
	main()
