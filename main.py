#!/usr/bin/python
import numpy
import pyaudio

#Silence is -36, no sound -80, max sound 0
#-20 is more less a talking person [shoud test this]
import analyse

import time

# Initialize PyAudio
pyaud = pyaudio.PyAudio()

# Open input stream, 16-bit mono at 44100 Hz
# On my system, device 2 is a USB microphone, your number may differ.
stream = pyaud.open(
    format = pyaudio.paInt16,
    channels = 1,
    rate = 44100,
    input_device_index = 0,
    input = True)

runner = True   #contro variable for Loop
count = 0       #count number of bits
bits = ""       #final 8bit string
while runner:
    try:
        # Read raw microphone data
        rawsamps = stream.read(1024)

        # Convert raw data to NumPy array
        samps = numpy.fromstring(rawsamps, dtype=numpy.int16)

        # Show the volume and pitch
        sound = analyse.loudness(samps)

        #If talking record 1
        if sound > -20:
            bits += "1"
        else:
            bits += "0"

        #format output
        if count == 7: #reached 8 bits
            print bits
            bits = ""
            count = 0
        else:
            count += 1

        #set some delay, maybe it is 1 sec
        stream.stop_stream();

        #time.sleep(.5)

        stream.start_stream()

    except KeyboardInterrupt:
        runner = False  #stop script while pressing ctrl + c

# stop stream
stream.stop_stream()
stream.close()

# close PyAudio
pyaud.terminate()
