BUTTONPATH = '/home/pi/esh/buttons'
LEDPATH = '/home/pi/esh/leds/confess'
MLPATH = '/home/pi/esh/prod/ML'
PYPATH = '/home/pi/esh/prod/'
PREDLOW = 2
PREDHIGH = 4


def main():
	f1 = open(BUTTONPATH,'r')
	fbut = f1.read()
	f1.close()
	fappend = open(PYPATH + 'butimportlog','a')
	f2 = open(PYPATH + 'butimportlog','r')
	fread = f2.read()
	f2.close()

	newclicks = []

	for line in fbut:
		print(line)

	fappend.close()

	return

if __name__ == "__main__":
	main()
