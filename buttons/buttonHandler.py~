import RPi.GPIO as GPIO
import time
import string
import csv

greenButton = 4;
yellowButton= 17;
redButton   = 27;

GPIO.setmode(GPIO.BCM)
GPIO.setup(greenButton, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(yellowButton, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(redButton, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


GPIO.add_event_detect(greenButton, GPIO.RISING, bouncetime = 1000)
GPIO.add_event_detect(yellowButton, GPIO.RISING, bouncetime = 1000)
GPIO.add_event_detect(redButton, GPIO.RISING, bouncetime = 1000)




def my_callback(channel):
	with open('/home/pi/esh/buttons/button.csv','ab') as csvfile:
                fieldnames = ['TimeStamp','ch']
		writer = csv.DictWriter(csvfile,fieldnames=fieldnames)
		if channel == redButton:
			print('Edge detected on redButton')
			writer.writerow({'TimeStamp':str(int(time.time())),'ch':"red"})
		elif channel == yellowButton:
			print('Edge detected on yellowButton')
			writer.writerow({'TimeStamp':str(int(time.time())),'ch':"yellow"})
		elif channel == greenButton:
			print('Edge detected on greenButton')
			writer.writerow({'TimeStamp':str(int(time.time())),'ch':"green"})

	with open('/home/pi/esh/leds/confess','wb') as csvfile:
                fieldnames =['button']
		writer = csv.DictWriter(csvfile,fieldnames=fieldnames)
		if channel == redButton:
			print('Edge detected on redButton')
			writer.writerow({'button':'r'})
		elif channel == yellowButton:
			print('Edge detected on yellowButton')
			writer.writerow({'button':'y'})
		elif channel == greenButton:
			print('Edge detected on greenButton')
			writer.writerow({'button':'g'})
GPIO.add_event_callback(redButton, my_callback)
GPIO.add_event_callback(yellowButton, my_callback)
GPIO.add_event_callback(greenButton, my_callback)


while True:
	time.sleep(1000)
	
GPIO.cleanup()
