#!/usr/bin/python
from __future__ import print_function
import os  

#	Export features:
#	- Always sample same length of data when extracting
#	- Normalize
#	- Max ampl
#	- Max Freq
#	- Average amp
#	- Sumsq < 25 percent
#	- Sumsq > 75 percent
#	- number of peaks
# 	- high peaks

# Features
import scipy
from scipy.io.wavfile import read
import numpy as np

# Time
import time
import datetime

RECSPATH = './recs_ESH/'
FEATUREPATH = 'features.csv'

# Import log:

def getnewfiles():
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
	        	f.write(fn + "\n") #writestring)
	f.close()
	return newfiles

def savefeature(newfeature,savepath):
	ff = open(savepath,'a')
	featurestr = str(newfeature)[1:-1]
	ff.write(featurestr + "\n")
	ff.close()
	print("New feature saved")
	return

def extractfeatures(filename_):
	
	# read audio samples
	input_data = read(RECSPATH+filename_)
	audio = np.abs(input_data[1])

	# Features:

	## max:
	smax=int(np.max(audio))

	## median:
	median=int(np.median(audio))
	#print("median: ",median)

	## mean:
	average=int(np.average(audio).round(decimals=3))
	#print("average: ",average)

	## sumsq:
	sumsqtot=int(np.sum(audio**2))
	#print("sumtot: ",sumtot)

	## sum sq < 25%:
	condlist1 = [audio<smax/4]
	choicelist1 = [audio]
	sumsq25 = int(np.sum(np.select(condlist1, choicelist1))) # *10000/sumtot
	#sumsq25.round(decimals=5)
	# print("sumsq25: ",sumsq25)

	## sum sq > 75%:
	condlist2 = [audio>smax/4*3]
	choicelist2 = [audio**2]
	sumsq75 = int(np.sum(np.abs(np.select(condlist2, choicelist2)))) # *10000/sumtot
	# print("sumsq75: ",sumsq75)

	## standard deviation:
	std=int(np.std(audio).round(decimals=3))
	# print("std: ",std)

	## sum diff:
	sumdiff=int(np.sum(np.abs(np.diff(audio))))
	# print("sumdiff: ",sumdiff)

	# print(np.diff(audio))
	header = ('max','median', 'average', 'sumsqtot', 'sumsq25', 'sumsq75', 'std', 'sumdiff')
	results = [smax, median, average, sumsqtot, sumsq25, sumsq75, std, sumdiff]
	#print(header)
	#print(results)
	return results

def main():
	newfiles = getnewfiles()
	if newfiles != []:
		for newfile in newfiles:
			print("Found newfile: " + newfile)
			
			newfeatures = extractfeatures(newfile)
			filedate = newfile[4:-4]

			timestamp = int(time.mktime(datetime.datetime.strptime(filedate, "%Y-%m-%d_%H-%M-%S").timetuple()))

			extractfeature = [timestamp] + newfeatures
			savefeature(extractfeature,FEATUREPATH)

	else:
		print('No files found')
	return

if __name__ == "__main__":
	main()


