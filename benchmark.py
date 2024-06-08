import pandas as pd
import matplotlib
import pyaudio
import time
from math import log10
import audioop  
import matplotlib.pyplot as plt
import sys


p = pyaudio.PyAudio()
WIDTH = 2
RATE = int(p.get_default_input_device_info()['defaultSampleRate'])
DEVICE = p.get_default_input_device_info()['index']
rms = 1
print(p.get_default_input_device_info())

def callback(in_data, frame_count, time_info, status):
    global rms
    rms = audioop.rms(in_data, WIDTH) / 32767
    return in_data, pyaudio.paContinue


stream = p.open(format=p.get_format_from_width(WIDTH),
                input_device_index=DEVICE,
                channels=1,
                rate=RATE,
                input=True,
                output=False,
                stream_callback=callback)

stream.start_stream()

countdown = sys.argv[1] 
start = time.time()
decibelList = []
while (float(time.time()) - float(start)) <= int(countdown): 
    db = 20 * log10(rms)
    #print(f"RMS: {rms} DB: {db}")
    decibelList.append(db)
    # refresh every 0.3 seconds 
    time.sleep(0.3)

stream.stop_stream()
stream.close()

p.terminate()
print(decibelList[4])
entries = list(range(len(decibelList)))
plt.plot(entries, decibelList, marker='o', linestyle='-')

plt.xlabel("Entries")
plt.ylabel("Decibels")
plt.title("Range of Volume")
plt.show()

