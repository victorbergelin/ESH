#prodML.py
import prodmaketrain
import prodfeat

from sklearn import svm
import csv

FEATUREFILE = 'features.csv'

def trainmodel(X,Y):

	clf = svm.SVR()
	clf.fit(X, Y)
	return clf

# clf.predict(X_test)

def main():
	
	# load features from file
	res = prodmaketrain.main()

	# a[:] = [x for x in a if x != [1, 1]]

	X = [x[1:] for x in res[0]]
	Y = [y[1:] for y in res[1]]

	# clf=trainmodel(X,Y)

	res = prodmaketrain.getfeatures()
	X_test = [x[1:] for x in res]
	# Y_test = clf.predict(X_test)


	prodfeat.savefeature(X,'X.csv')
	prodfeat.savefeature(Y,'Y.csv')
	prodfeat.savefeature(X_test,'XT.csv')


if __name__ == "__main__":
	main()
