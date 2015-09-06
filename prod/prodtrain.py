#prodtrain.py
from sklearn.externals import joblib
import prodmaketrain

from sklearn import svm
import csv

FEATUREFILE = 'features.csv'
MLLIB = 'ML/SVN.pkl'

def trainmodel(X,Y):

	clf = svm.SVR()
	clf.fit(X, Y)
	return clf

def main():
	
	# load features from file
	traindata = prodmaketrain.main()

	X = [x[1:] for x in traindata[0]]
	Y = [y[1:] for y in traindata[1]]

	clf=trainmodel(X,Y)
	joblib.dump(clf, MLLIB)

if __name__ == "__main__":
	main()
