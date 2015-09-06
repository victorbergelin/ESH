# prodsend.py
import httplib, urllib
import numpy as np

def senddata(Ysave):
	# find and extract new predictions to send
	
	# convert
	sendreq()
	# send

	return

def sendreq(inputlist):
	# make connection
	dataarray = []

	for data in inputlist:
		myURL = "kontoret.exceed-it.se"
		myURLParameters = "/measurements"
		print data
		# 
		ts=data[0]
		sl = data[1]
		conf = 0# data[2]
		humidity = 0# data[3]
		temp = 0 #data[4]
		pid = 1
		dataarray.append({'timestamp': ts, 'study_level': sl, 'confidence': conf,'humidity': humidity,'temperature': temp,'punkt_id': pid})


	Rawparams = {'measurements':dataarray}
	print(Rawparams)

	params = urllib.urlencode(Rawparams)
	print(params)

	headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}
	conn = httplib.HTTPConnection(myURL)
	conn.request("POST", myURLParameters, params) # , headers)
	response = conn.getresponse()
	print response.status, response.reason

	data = response.read()
	conn.close()
	return response.status

#if __name__ == "__main__":
#	main(array)
