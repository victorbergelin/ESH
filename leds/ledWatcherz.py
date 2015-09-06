

import pyinotify
import RPi.GPIO as GPIO

FILE = "/home/pi/esh/leds/confess"
redLED = 13
yellowLED = 26  
greenLED =  19


GPIO.setmode(GPIO.BCM)
GPIO.setup(redLED,GPIO.OUT,True)
GPIO.setup(yellowLED,GPIO.OUT,True)
GPIO.setup(greenLED,GPIO.OUT,True)

print "START"
class eventHandler(pyinotify.ProcessEvent):
	def process_IN_CLOSE_WRITE(self, evt):
		button = open(FILE,'r').read(1)
		if button == "r":
			print('ledWatcherz redLED') 
			GPIO.output(redLED,False)
			GPIO.output(yellowLED,True)
			GPIO.output(greenLED,True)
		elif button == "y":
               		print('ledWatcherz yellowLED')
			GPIO.output(redLED,True)
			GPIO.output(yellowLED,False)
			GPIO.output(greenLED,True)
       		elif button == "g":
               		print('ledWatcherz greenLED') 
			GPIO.output(redLED,True)
			GPIO.output(yellowLED,True)
			GPIO.output(greenLED,False)
  
handler = eventHandler()
wm = pyinotify.WatchManager()
notifier = pyinotify.Notifier(wm, handler)
wdd = wm.add_watch(FILE, pyinotify.IN_CLOSE_WRITE)
notifier.loop()
GPIO.cleanup()
print "SLUT"
