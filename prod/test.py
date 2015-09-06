

	# 0. listen for new files
	newfiles = listengetnewfiles()

	# 1. load model:
	clf = joblib.load(MLPATH) 

	# 2. load files and create features:
	# 3. make prediction:
	if(len(newfiles)!=0):
		YpredSave = []
		print(len(newfiles) + "file(s) found: " + str(newfiles))
		for files in newfiles:
			features = prodfeat.extractfeatures(str(files))
			Xtest = [x[1:] for x in features]	
			Ypred = clf.predict(Xtest)
			prodfeat.savefeature(Ysave,'Ysave.csv')
			indexprediction = [x[0] for x in traindata[0]]
		updatecolors(pred2col(Ypred))
	else: 
		print("No files found")


	# print(len(indexprediction))

	for i in range(len(indexprediction)):
		Ysave.append([indexprediction[i],Ypred[i]])
		#print([indexprediction[i],Ypred[i],i])

	print(len(Ysave))