#!/usr/bin/python
import numpy
import pyaudio
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

while True:
    # Read raw microphone data
    rawsamps = stream.read(1024)
    #print rawsamps
    # Convert raw data to NumPy array
    samps = numpy.fromstring(rawsamps, dtype=numpy.int16)
    #print samps
    # Show the volume and pitch
    print analyse.loudness(samps)

    #print analyse.loudness(samps), analyse.musical_detect_pitch(samps)
    #time.sleep(1)
