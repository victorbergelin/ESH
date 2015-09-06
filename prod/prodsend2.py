# prodsend.py
import httplib, urllib

def main(inputarray[]):
	# make connection
	dataarray = []

	for array in inputarray:
		myURL = "kontoret.exceed-it.se"
		myURLParameters = "/measurements"
		ts=1441461376
		sl = 54
		conf = 23
		humidity = 45
		temp = 99
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
	return [str(response.status), str(response.reason)]

if __name__ == "__main__":
	main([1,2,3])
