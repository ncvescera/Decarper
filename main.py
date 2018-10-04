#!/usr/bin/python
'''
    Silence is -36, no sound -80, max sound 0
    -20 is more less a talking person [shoud test this]
    should check rate on stream
'''
import numpy
import pyaudio
import analyse
import time

# Initialize PyAudio
pyaud = pyaudio.PyAudio()

# Open input stream, 16-bit mono at 44100 Hz
stream = pyaud.open(
    format = pyaudio.paInt16,
    channels = 1,
    rate = 44100,
    input_device_index = 0,
    input = True)

runner = True   #Control variable for Loop
count = 0       #Count number of bits
bits = ""       #Final 8bit string
while runner:
    try:
        # Read raw microphone data
        rawsamps = stream.read(1024)

        # Convert raw data to NumPy array
        samps = numpy.fromstring(rawsamps, dtype=numpy.int16)

        #Convert NumPy array to db value (float and less than 0)
        sound = analyse.loudness(samps)

        #If talking record 1
        if sound > -20:
            bits += "1"
        else:
            bits += "0"

        #Format output
        if count == 7: #Reached 8 bits
            print bits
            bits = ""
            count = 0
        else:
            count += 1

        #Set some delay, maybe it is 1 sec
        stream.stop_stream();
        #time.sleep(.5)
        stream.start_stream()

    except KeyboardInterrupt:
        runner = False  #Stop script while pressing ctrl + c

#Stop stream
stream.stop_stream()
stream.close()

#Close PyAudio
pyaud.terminate()
