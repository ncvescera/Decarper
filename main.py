#!/usr/bin/python
'''
    Silence is -36, no sound -80, max sound 0
    -20 is more less a talking person [shoud test this]
'''
import numpy
import pyaudio
import analyse
import sys
import time
import datetime
import os

from decoding import *

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
phrase = ""     #la frase di carpi che viene aggiornata runtime
tres = -20      #treshold
row = 0

#variabili per stampa formattata
bit_out = ""

while runner:
    try:
            while count < 7:
                stream.start_stream()
                rawsamps = stream.read(1024)
                samps = numpy.fromstring(rawsamps, dtype=numpy.int16)
                sound = analyse.loudness(samps)
                stream.stop_stream()

                if sound > tres:
                    bits += "1"
                else:
                    bits += "0"

                count += 1
                if(count == 7):
                    if bits == "0000000":
                        phrase += " "
                    else:
                        if bits == "1111111":
                            phrase += "!"
                        else:
                            phrase += text_from_bits(bits)

            #formattazione dell'output
            os.system('clear')

            bit_out += bits + "\t"+ text_from_bits(bits) +"\n"

            print bit_out
            print "Carpi said: " + phrase

            count = 0
            bits = ""

    except KeyboardInterrupt:
        runner = False  #stop script while pressing ctrl + c

#Writing log
file = open("log","a")

data = datetime.datetime.now()
file.write("Message from Carpi to Earth - " + str(data) + "\n")
file.write(phrase)
file.write("\n\n")

file.close()

# stop stream
stream.stop_stream()
stream.close()

# close PyAudio
pyaud.terminate()
