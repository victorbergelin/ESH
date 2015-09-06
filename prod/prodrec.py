#!/usr/bin/python
# prodrec.py

# Sounds
import pyaudio # py27-pyaudio
import wave
import sys

# Time:
from time import strftime

def main():
	while True:
		try:
			TIMESTR = strftime("%Y-%m-%d_%H-%M-%S")

			# RECPATH = str(sys.argv(1))
			CHUNK = 8192 #1024
			FORMAT = pyaudio.paInt16 #paInt8 
			CHANNELS = 1 # MAC IS MONO: 1 channel
			RATE = 44100 #sample rate 
			RECORD_SECONDS = 60 # 5 minutes  
			WAVE_OUTPUT_FILENAME = "REC_" + TIMESTR + ".wav"

			p = pyaudio.PyAudio()
			
			# DEBUG:
			# print("Default sample rate is: " + str(p.get_device_info_by_index(0)['defaultSampleRate']))		
			# print("Rate is set to: " + str(RATE))

			try:
				stream = p.open(format=FORMAT, 
					channels=CHANNELS,
					rate=RATE,
					input=True, 
					frames_per_buffer=CHUNK) #buffer
			except IOError as ex:
				if ex[1] != pyaudio.paInputOverflowed:
					print "stream error"
					raise

			print("* recording")

			frames = []

			for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)): 
				data = stream.read(CHUNK)
				frames.append(data) # 2 bytes(16 bits) per channel

			print("* done recording: " + WAVE_OUTPUT_FILENAME)

			stream.stop_stream() 
			stream.close() 
			p.terminate()

			wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb') 
			wf.setnchannels(CHANNELS) 
			wf.setsampwidth(p.get_sample_size(FORMAT)) 
			wf.setframerate(RATE) 
			wf.writeframes(b''.join(frames)) 
			wf.close()
		except:
			print "Unexpected error:", sys.exc_info()[0]
			raise
	return

if __name__ == "__main__":
	main()

